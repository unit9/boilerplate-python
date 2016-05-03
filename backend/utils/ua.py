import logging
import operator

import user_agents
import yaml


def load_browsers_list(fname="browsers.yml"):
    with open(fname) as f:
        _data = yaml.load(f)
    blacklist = _data["blacklist"]
    return blacklist


default_blacklisted_browsers = load_browsers_list()

ops = {
    "eq": operator.eq,
    "ge": operator.ge,
    "gt": operator.gt,
    "le": operator.le,
    "lt": operator.lt,
}


def _getattrs(obj, *keys):
    """
    >>> class A(object):
    ...     pass
    ...
    >>> a = A()
    >>> a.b = A()
    >>> a.b.c = 1
    >>> _getattrs(a, "b", "c")
    1
    """
    for key in keys:
        obj = getattr(obj, key)
    return obj


def _cmp(key):
    """
    >>> _cmp("foo")
    ('foo', <built-in function eq>)
    >>> _cmp("foo__eq")
    ('foo', <built-in function eq>)
    >>> _cmp("foo__ge")
    ('foo', <built-in function ge>)
    >>> _cmp("foo__bar")
    Traceback (most recent call last):
      ...
    KeyError: 'bar'
    """
    op = "eq"
    if "__" in key:
        key, op = key.split("__", 1)
    return key, ops[op]


def _match(ua, browser):
    """Match UA data structure against browser definiton.

    Returns None if the match is exact, otherwise returns a reason why
    there was a mismatch.

    >>> ua = user_agents.parse("")
    >>> _match(ua, {"os": {"family": "Other"}})
    >>> _match(ua, {"os": {"family": "Linux"}})
    ('os', 'family', <built-in function eq>)

    >>> my_ua = ("Mozilla/5.0 (X11; Linux x86_64; rv:44.0) "
    ...          "Gecko/20100101 Firefox/44.0")
    >>> ua = user_agents.parse(my_ua)
    >>> _match(ua, {"os": {"family": "Linux"}})
    >>> _match(ua, {"browser": {"family": "Firefox"}})
    >>> _match(ua, {"browser": {"family": "Chrome"}})
    ('browser', 'family', <built-in function eq>)
    >>> _match(ua, {"os":      {"family": "Linux"},
    ...             "browser": {"family": "Firefox"}})
    >>> _match(ua, {"os":      {"family": "Linux"},
    ...             "browser": {"family": "Chrome"}})
    ('browser', 'family', <built-in function eq>)
    >>> _match(ua, {"browser": {"version__ge": (42, 0)}})
    >>> _match(ua, {"browser": {"version__ge": (45, 0)}})
    ('browser', 'version', <built-in function ge>)
    >>> _match(ua, {"browser": {"version__le": (22, 0)}})
    ('browser', 'version', <built-in function le>)

    >>> my_ua = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) "
    ...          "AppleWebKit/537.78.2 (KHTML, like Gecko) "
    ...          "Version/7.0.6 Safari/537.78.2")
    >>> ua = user_agents.parse(my_ua)
    >>> _match(ua, {"browser": {"family": "Safari",
    ...                         "version__le": (7, 9999)}})
    >>> _match(ua, {"browser": {"family": "Safari", "version__lt": (8,)}})
    >>> _match(ua, {"browser": {"family": "Safari", "version__le": (7,)}})
    ('browser', 'version', <built-in function le>)

    """
    for trait in ["os", "browser", "device"]:
        for rkey in browser.get(trait, []):
            key, op = _cmp(rkey)
            left = _getattrs(ua, trait, key)
            right = browser[trait].get(rkey)
            if not op(left, right):
                return trait, key, op
    return None


def is_supported(user_agent, blacklisted_browsers=None):
    """Tell whether user_agent matches a rule on the backlist.

    >>> my_ua = ("Mozilla/5.0 (X11; Linux x86_64; rv:44.0) "
    ...          "Gecko/20100101 Firefox/44.0")
    >>> is_supported(my_ua, blacklisted_browsers=[])
    True
    >>> is_supported(my_ua,
    ...              blacklisted_browsers=[{"os": {"family": "Linux"}}])
    False
    >>> is_supported(my_ua,
    ...              blacklisted_browsers=[{"os": {"family": "OpenBSD"}}])
    True
    >>> is_supported(my_ua, blacklisted_browsers=[
    ...     {"os": {"family": "OpenBSD"},
    ...      "browsers": {"family": "Firefox"}},
    ... ])
    True
    >>> is_supported(my_ua, blacklisted_browsers=[
    ...     {"os": {"family": "Linux"},
    ...      "browsers": {"family": "Firefox", "version_string__upto": "48"}},
    ... ])
    False
    >>> is_supported(my_ua, blacklisted_browsers=[
    ...     {"os": {"family": "Windows"}},
    ...     {"os": {"family": "OpenBSD"}},
    ...     {"browser": {"family": "Chrome"}},
    ...     {"os": {"family": "Linux"}, "browser": {"family": "Opera"}},
    ... ])
    True
    """
    if blacklisted_browsers is None:
        blacklisted_browsers = default_blacklisted_browsers
    ua = user_agents.parse(user_agent)

    for browser in blacklisted_browsers:
        matched = _match(ua, browser)
        if not matched:
            logging.debug("Bad browser: ua=%r rule=%r", str(ua), browser)
            return False
    logging.debug("Good browser: ua=%r", str(ua))
    return True

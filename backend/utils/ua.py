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
    for key in keys:
        obj = getattr(obj, key)
    return obj


def _cmp(key):
    op = "eq"
    if "__" in key:
        key, op = key.split("__", 1)
    return key, ops[op]


def _match(ua, browser):
    """Match UA data structure against browser definiton.

    Returns None if the match is exact, otherwise returns a reason why
    there was a mismatch."""
    for trait in ["os", "browser", "device"]:
        for rkey in browser.get(trait, []):
            key, op = _cmp(rkey)
            left = _getattrs(ua, trait, key)
            right = browser[trait].get(rkey)
            if not op(left, right):
                return trait, key, op
    return None


def is_supported(user_agent, blacklisted_browsers=None):
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

def hack_psycopg2cffi():
    try:
        from psycopg2cffi import compat
    except ImportError:
        pass
    else:
        compat.register()
    finally:
        import psycopg2
    return


def install_hacks():
    hack_psycopg2cffi()

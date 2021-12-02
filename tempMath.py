def f_to_c(n):
    return (n-32) * 5/9


def c_to_f(n):
    return (n * 9/5) + 32


def dewpoint(t, rh):
    # https://iridl.ldeo.columbia.edu/dochelp/QA/Basic/dewpoint.html
    # Dewpoint = CelsiusTemp - ((100-RelHumid%)/5)
    return t - ((100-rh)/5)

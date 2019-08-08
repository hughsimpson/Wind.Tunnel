def slurp_auth():
    with open('.auth') as x: f = x.read()
    return f.strip()


def spurt_auth(token):
    with open(".auth", "w") as text_file: text_file.write(token)


def merge_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

def read_token(path=None):
    if None == path:
        path = 'token.txt'

    with open(path) as f:
        token = f.read()

    return token

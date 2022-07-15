from util.init import bot_init
from util.token import read_token

if __name__ == '__main__':
    bot_init().run(read_token())

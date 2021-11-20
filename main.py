#!/usr/bin/python

import database
import bot


def main():
    # database.connect()
    print("hello daft_bot")
    bot.botify()


if __name__ == "__main__":

    conn = database.connect()
    try:
        main()
    except KeyboardInterrupt:
        database.backup(conn, bot.Houses_Visited)

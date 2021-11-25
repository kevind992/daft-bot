#!/usr/bin/python

from database import sqlite
from bot import bot


def main():
    # database.connect()
    print("hello daft_bot")
    bot.botify()


if __name__ == "__main__":

    main()
    #conn = sqlite.connect()
    #try:
    #    main()
    #except KeyboardInterrupt:
    #    sqlite.backup(conn, bot.Houses_Visited)

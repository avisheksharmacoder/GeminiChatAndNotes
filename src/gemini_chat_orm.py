from pony import orm


# make Database Object.
db = orm.Database()

# make database file, for binding classes into tables.
db.bind(provider="sqlite", filename="./sqlite_db/chat.db", create_db=True)

# make Schema class for storing chats as records.

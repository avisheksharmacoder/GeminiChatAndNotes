from pony import orm
from datetime import datetime


# make Database Object.
db = orm.Database()

# make database file, for binding classes into tables.
db.bind(provider="sqlite", filename="./sqlite_db/chat.db", create_db=True)


# make Schema class for storing chats as records.
class Chat(db.Entity):
    prompt = orm.Required(str)
    prompt_response = orm.Required(str)
    prompt_time = orm.Required(datetime)


# generate the tables.
db.generate_mapping(create_tables=True)

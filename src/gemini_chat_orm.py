from pony import orm
from datetime import datetime


# We have to make Database object, to perform DB operations.
db = orm.Database()

# We have to bind database object, with db engine, file name and whether
# to create the database file or not.
db.bind(provider="sqlite", filename="./sqlite_db/chat.db", create_db=True)


# We have to make the Schema class, that will let us store rows in
# the database.
class Chat(db.Entity):
    prompt = orm.Required(str)
    prompt_response = orm.Required(str)
    prompt_time = orm.Required(datetime)


# We have to generate the tables to store data.
db.generate_mapping(create_tables=True)

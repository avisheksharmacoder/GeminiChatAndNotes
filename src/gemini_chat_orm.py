from pony import orm
from datetime import datetime
import os


# check if sqlite db is in folder or not.
def sqlite_db_exists(filename: str, folder_path: str) -> bool:
    file_path = os.path.join(folder_path, filename)
    return os.path.isfile(file_path)


# We have to make Database object, to perform DB operations.
db = orm.Database()

# This is the sqlite database file name.
filename = "chat.db"

# This is the folder path where the database file is stored.
folder_path = "./sqlite_db"


# We have to make the Schema class, that will let us store rows in
# the database.
class Chat(db.Entity):
    prompt = orm.Required(str)
    prompt_response = orm.Required(str)
    prompt_time = orm.Required(datetime)


# We have to bind database object, with db engine, file name and whether
# to create the database file or not.
if not sqlite_db_exists(filename, folder_path):
    db.bind(provider="sqlite", filename=folder_path + "/" + filename, create_db=True)
    print("database file created !!")
    # We have to generate the tables to store data.
    db.generate_mapping(create_tables=True)
else:
    print("database already exists !!")

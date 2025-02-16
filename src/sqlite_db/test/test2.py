from pathlib import Path
import os


def sqlite_db_exists(filename: str, folder_path: str) -> bool:
    file_path = Path(folder_path + "\\" + filename)
    return file_path.exists()


db_filepath = "/"
db_filename = "chat.db"
current_dir = Path.cwd()
parent_dir = os.path.dirname(current_dir)
if sqlite_db_exists(db_filename, parent_dir):
    print("db exists")
else:
    print("db not found")

# print(parent_dir + "\\chat.db")
# filepath = pathlib.Path(paths + fils)
# if filepath.exists():
#     print("file is there")
# else:
#     print("file not there")

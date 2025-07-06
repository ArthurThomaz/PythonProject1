import os
import shutil

original_path = '/users/Arthu/Videos/TWICE 07.02'
new_path = '/users/Arthu/Videos/SHOW TWICE 07.02'
try:
    os.mkdir(new_path)
except FileExistsError as e:
    pass
for root, dirs, files in os.walk(original_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)
        shutil.move(old_file_path, new_file_path)
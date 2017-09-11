import shutil
import os


class Exchange:
    def send_file(self, user_path, storage_main_path):
        shutil.copy2(user_path, storage_main_path)

    def get_file(self, user_path, storage_main_path):
        shutil.copy2(storage_main_path, user_path)

    def remove_file(self, path):
        os.remove(path)
        #os.removedirs(path)

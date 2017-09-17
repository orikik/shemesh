import shutil
import os
import threading


"""
        thread_one = threading.Thread(target=self.ori, name="proc_one")
        thread_two = threading.Thread(target=self.mar, name="proc_two")
        thread_one.start()
        thread_two.start()
        thread_one.join()
        thread_ywo.join()
"""
class Exchange:
    def send_file(self, user_path, storage_main_path):
        shutil.copy2(user_path, storage_main_path)

    def get_file(self, user_path, storage_main_path):
        shutil.copy2(storage_main_path, user_path)

    def remove_file(self, path):
        os.remove(path)
        #os.removedirs(path)

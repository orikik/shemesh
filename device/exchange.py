import shutil
import os
import threading
from flask import make_response

"""
        thread_video = threading.Thread(target=self.ori, name="proc_video")
        thread_audio = threading.Thread(target=self.mar, name="proc_audio")
        thread_video.start()
        thread_audio.start()
        thread_video.join()
        thread_audio.join()
"""
class Exchange:
    def send_file(self, user_path, storage_main_path):
        shutil.copy2(user_path, storage_main_path)

    def get_file(self, user_path, storage_main_path):
        shutil.copy2(storage_main_path, user_path)

    def remove_file(self, path):
        os.remove(path)
        #os.removedirs(path)

    def ori(self):
        shutil.copy2('C:/Users/Ори/Downloads/1.txt', 'D:/1')

    def mar(self):
        resp = make_response("logout")
        return resp

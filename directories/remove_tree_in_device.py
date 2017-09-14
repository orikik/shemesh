import shutil
from device.DB_manager import DB
from device.path_manager import Path


def remove_tree(full_path):
    for v in DB().all_dev():
        dev = v['path']
        n = Path().full_path_exist(dev=dev, full_path=full_path)
        path = dev + '/' + full_path
        if n:
            shutil.rmtree(path)
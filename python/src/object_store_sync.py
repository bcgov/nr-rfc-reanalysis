"""used to copy files that have been downloaded to object storage
"""

import os

import ObjectStore


class Sync2ObjectStore:

    def __init__(self, src_dir, dest_dir):
        self.srcDir = src_dir
        self.destDir = dest_dir
        self.ostore = ObjectStore.ObjectStoreUtil()

    def sync(self):
        src_file_list = os.listdir(self.srcDir)
        for src_file in src_file_list:
            src_file_full_path = os.path.join(self.srcDir, src_file)
            dest_file_full_path = os.path.join(self.destDir, src_file)
            if not os.path.isdir(src_file_full_path):
                self.ostore.putObject(destPath=dest_file_full_path,
                                      localPath=src_file_full_path)

if __name__ == '__main__':
    sync = Sync2ObjectStore(src_dir='./data', dest_dir="/junk")
    sync.sync()

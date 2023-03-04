import datetime
import logging
import logging.config
import os.path
import sys

import config
import get_images
import image_download_config
import object_store_sync

# setup logging
log_config_path = os.path.join(os.path.dirname(__file__), "..", "config", "logging.config")
logging.config.fileConfig(log_config_path)

LOGGER = logging.getLogger(__name__)

class Main:
    def __init__(self):
        self.cur_date_str = datetime.datetime.now().strftime("%Y%m%d")
        self.dest_dir = os.path.join(config.OBJ_STORE_DEST_FOLDER, self.cur_date_str)
        self.ostore = object_store_sync.Sync2ObjectStore(src_dir=config.FOLDER,
                                                         dest_dir=self.dest_dir)


    def get_soil_moisture_images(self):
        todays_files = self.ostore.get_todays_files()
        LOGGER.debug(f"todays files: {todays_files}")
        for config in image_download_config.ALL_CONFIG_CLASS_LIST:
            if config.output_image_file not in todays_files:
                dl = get_images.GetImageUsingConfig(config)
                dl.get()

    def upload_2_ostore(self):
        # copy data to object store
        LOGGER.debug(f"copying files to object storage folder: {self.dest_dir}")
        LOGGER.debug(f"src folder: {config.FOLDER}")
        self.ostore.sync()


if __name__ == "__main__":
    main = Main()
    main.get_soil_moisture_images()
    main.upload_2_ostore()

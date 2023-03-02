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

# download the min temp
minTempConfig = image_download_config.TempMinConfig()
dl = get_images.GetImageUsingConfig(minTempConfig)
dl.get()

# download the max temp
maxTempConfig = image_download_config.TempMaxConfig()
dl = get_images.GetImageUsingConfig(maxTempConfig)
dl.get()

precip_30day_config = image_download_config.Precip_mddb2_30day()
dl =get_images.GetImageUsingConfig(precip_30day_config)
dl.get()

precip_90day_config = image_download_config.Precip_mddb2_90day()
dl =get_images.GetImageUsingConfig(precip_90day_config)
dl.get()

precip_180day_config = image_download_config.Precip_mddb2_180day()
dl =get_images.GetImageUsingConfig(precip_180day_config)
dl.get()

soil_moisture_ECMWF_l1_config = image_download_config.Soil_moisture_l1()
dl = get_images.GetImageUsingConfig(soil_moisture_ECMWF_l1_config)
dl.get()

Soil_moisture_l1to3 = image_download_config.Soil_moisture_l1to3()
dl = get_images.GetImageUsingConfig(Soil_moisture_l1to3)
dl.get()

wecwf_24hr_config = image_download_config.WECWF_24hr_config()
dl = get_images.GetImageUsingConfig(wecwf_24hr_config)
dl.get()

wecwf_48hr_config = image_download_config.WECWF_48hr_config()
dl = get_images.GetImageUsingConfig(wecwf_48hr_config)
dl.get()

wecwf_72hr_config = image_download_config.WECWF_72hr_config()
dl = get_images.GetImageUsingConfig(wecwf_72hr_config)
dl.get()

wecwf_96hr_config = image_download_config.WECWF_96hr_config()
dl = get_images.GetImageUsingConfig(wecwf_96hr_config)
dl.get()

wecwf_120hr_config = image_download_config.WECWF_120hr_config()
dl = get_images.GetImageUsingConfig(wecwf_120hr_config)
dl.get()

ncep_soil_moisture_0to10cm = image_download_config.NCEP_Soil_moisture_0to10cm_config()
dl = get_images.GetImageUsingConfig(ncep_soil_moisture_0to10cm)
dl.get()

ncep_soil_moisture_10to100cm = image_download_config.NCEP_Soil_moisture_10to100cm_config()
dl = get_images.GetImageUsingConfig(ncep_soil_moisture_10to100cm)
dl.get()

# copy data to object store
cur_date_str = datetime.datetime.now().strftime("%Y%m%d")
dest_dir = os.path.join(config.OBJ_STORE_DEST_FOLDER, cur_date_str)
object_store_sync.Sync2ObjectStore(src_dir=config.FOLDER, dest_dir=dest_dir)
import os
import sys


class required_parameter_exception(Exception):
    def __init__(self, param_name, param_value):
        self.message = ('The process cannot run without populating the ' +
           f"environment variable: {param_name}")
        super().__init__(self.message)

thismodule = sys.modules[__name__]

RFC_ROOT_FOLDER = 'RFC_DATA'
MINIO_SECURE = False
# this is the temp folder where data will be downloaded to before it gets
# uploaded to object storeage
FOLDER = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'data'))
OBJ_STORE_DEST_FOLDER = os.path.join('RFC_REPORTING', 'soil_moisture', 'summary_data')


# these are required
params2populate = ['OBJ_STORE_BUCKET', 'OBJ_STORE_SECRET',
    'OBJ_STORE_USER', 'OBJ_STORE_HOST']

for param_name in params2populate:
    param_value = os.getenv(param_name)
    if not param_value:
        raise required_parameter_exception(param_name, param_value)
    setattr(thismodule, param_name, param_value)

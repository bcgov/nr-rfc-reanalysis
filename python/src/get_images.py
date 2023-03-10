"""
Duplicates what was done in the Reanalysis.R script
"""

import logging
import os.path

import config
import image_download_config
import jsonschema
import requests

LOGGER = logging.getLogger(__name__)


class GetImage:
    def __init__(self, url, dest_file):
        self.url = url
        self.dest_file = dest_file

    def get(self):
        r = requests.get(self.url, allow_redirects=True)
        LOGGER.debug(f"request: {r.status_code}")
        r.raise_for_status()
        with open(self.dest_file, "wb") as fh:
            fh.write(r.content)
        r.close()


class GetImageJson(GetImage):
    def __init__(self, url, dest_file):
        GetImage.__init__(self, url, dest_file)
        self.defineSuccessSchema()
        self.defineErrorSchema()

    def defineErrorSchema(self):
        """schema used to validate incomming json... autogenerated here:
        https://easy-json-schema.github.io/ using sample output from the
        api
        """
        self.error_schema = {
            "type": "object",
            "required": [],
            "properties": {
                "tracker": {"type": "string"},
                "uid": {"type": "string"},
                "error": {"type": "array", "items": {"type": "string"}},
            },
        }

    def defineSuccessSchema(self):
        """schema used to validate incomming json... autogenerated here:
        https://easy-json-schema.github.io/ using sample output from the
        api
        """
        self.success_schema = {
            "type": "object",
            "required": [],
            "properties": {
                "meta": {
                    "type": "object",
                    "required": [],
                    "properties": {
                        "terms-and-conditions": {
                            "type": "object",
                            "required": [],
                            "properties": {"href": {"type": "string"}},
                        },
                        "license": {"type": "string"},
                        "copyright": {"type": "string"},
                    },
                },
                "data": {
                    "type": "object",
                    "required": [],
                    "properties": {
                        "link": {
                            "type": "object",
                            "required": [],
                            "properties": {
                                "href": {"type": "string"},
                                "type": {"type": "string"},
                            },
                        },
                        "attributes": {
                            "type": "object",
                            "required": [],
                            "properties": {
                                "description": {"type": "string"},
                                "name": {"type": "string"},
                                "title": {"type": "string"},
                            },
                        },
                        "type": {"type": "string"},
                    },
                },
                "tracker": {"type": "string"},
                "template": {"type": "string"},
                "uid": {"type": "string"},
            },
        }

    def get(self):
        """override the default get

        :return: _description_
        """
        r = requests.get(self.url, allow_redirects=True)
        site_json = r.json()
        LOGGER.debug(f"json: {site_json}")
        if "error" in site_json:
            raise DataNotAvailableException(self.url)

        # making sure the expected structure exists, will generate a validation
        # error if problems
        jsonschema.validate(instance=site_json, schema=self.success_schema)

        if site_json["data"]["link"]["type"] != "image/png":
            raise UnexpectedLinkType(site_json["data"]["link"]["type"], "image/png")

        image_url = site_json["data"]["link"]["href"]
        r = requests.get(image_url, allow_redirects=True)
        LOGGER.debug(f"request: {r.status_code}")
        r.raise_for_status()
        with open(self.dest_file, "wb") as fh:
            fh.write(r.content)
        r.close()


class DataNotAvailableException(Exception):
    def __init__(self, url):
        self.message = (
            "the following url indicates the data is not available for the "
            + f"specified time frame: {url}"
        )
        super().__init__(self.message)


class UnexpectedLinkType(Exception):
    def __init__(self, incommingType, expectedType):
        self.message = (
            f"expected the returned json to have a type: {expectedType}"
            + f"however it had a type of {incommingType}"
        )
        super().__init__(self.message)


class GetImageUsingConfig:
    def __init__(self, download_config: image_download_config.AbstractImageDLConfig):
        self.url = self.get_url(download_config)
        LOGGER.debug(f"url: {self.url}")
        self.dest_file = self.get_dest_file(download_config)
        self.download_config = download_config

    def get(self):
        if self.download_config.url_type == image_download_config.UrlType.IMAGE:
            dl = GetImage(self.url, self.dest_file)
        else:
            dl = GetImageJson(self.url, self.dest_file)
        LOGGER.debug("getting the image...")
        if not os.path.exists(os.path.dirname(self.dest_file)):
            LOGGER.debug(f"creating the directory: {os.path.dirname(self.dest_file)}")
            os.makedirs(os.path.dirname(self.dest_file))
        dl.get()

    def get_dest_file(self, download_config):
        dest_file = os.path.join(config.FOLDER, download_config.output_image_file)
        LOGGER.debug(f"destintation file: {dest_file}")
        return dest_file

    def get_url(self, download_config):
        """_summary_

        :param download_config: _description_
        :return: _description_
        """
        # download_config.url_template.format()
        t1_year = download_config.date1.strftime("%Y")
        t1_month = download_config.date1.strftime("%m")
        t1_day = download_config.date1.strftime("%d")

        t2_year = download_config.date2.strftime("%Y")
        t2_month = download_config.date2.strftime("%m")
        t2_day = download_config.date2.strftime("%d")

        url_string = download_config.url_template.format(
            t1_year=t1_year,
            t1_month=t1_month,
            t1_day=t1_day,
            t2_year=t2_year,
            t2_month=t2_month,
            t2_day=t2_day,
        )
        return url_string

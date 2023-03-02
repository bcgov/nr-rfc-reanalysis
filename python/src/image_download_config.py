import abc
import datetime
import enum
import logging
import os.path

LOGGER = logging.getLogger(__name__)


class UrlType(enum.Enum):
    IMAGE = 1
    JSON = 2


class AbstractImageDLConfig(metaclass=abc.ABCMeta):
    """Using this class to ensure that subclasses of it posses the expected
    properties

    :param metaclass: declaring as an Abstract base class, defaults to
                      abc.ABCMeta
    """

    @property
    @abc.abstractmethod
    def url_template(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def output_image_file(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def url_type(self) -> UrlType:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def date1(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def date2(self):
        raise NotImplementedError


class TempMinConfig(AbstractImageDLConfig):
    url_template = "https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=4609&fileID=0&itype=0&variable=tmin&levelType=Surface&level_units=&level=Surface&timetype=day&fileTimetype=day&year1={t1_year}&month1={t1_month}&day1={t1_day}&hr1=00%20Z&year2={t2_year}&month2={t2_month}&day2={t2_day}&hr2=00%20Z&vectorPlot=0&contourLevel=custom&cint=4&lowr=-20&highr=20&colormap=default&reverseColormap=no&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"
    output_image_file = "Daily_MinT_CPC.png"
    url_type = UrlType.IMAGE
    date1 = datetime.datetime.now() - datetime.timedelta(days=2)
    date2 = datetime.datetime.now() - datetime.timedelta(days=2)

class TempMaxConfig(AbstractImageDLConfig):
    url_template = "https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=53407&fileID=0&itype=0&variable=tmax&levelType=Surface&level_units=&level=Surface&timetype=day&fileTimetype=day&year1={t1_year}&month1={t1_month}&day1={t1_day}&hr1=00%20Z&year2={t2_year}&month2={t2_month}&day2={t2_day}&hr2=00%20Z&vectorPlot=0&contourLevel=custom&cint=4&lowr=-20&highr=40&colormap=default&reverseColormap=no&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"
    output_image_file = "Daily_MaxT_CPC.png"
    url_type = UrlType.IMAGE
    date1 = datetime.datetime.now() - datetime.timedelta(days=2)
    date2 = datetime.datetime.now() - datetime.timedelta(days=2)


class Precip_mddb2_30day(AbstractImageDLConfig):
    url_template = "https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=2781&fileID=0&itype=0&variable=precip&levelType=Surface&level_units=&level=Surface&timetype=day&fileTimetype=day&createAverage=1&year1={t1_year}&month1={t1_month}&day1={t1_day}&hr1=00%20Z&year2={t2_year}&month2={t2_month}&day2={t2_day}&hr2=00%20Z&vectorPlot=0&contourLevel=custom&cint=2&lowr=0&highr=20&colormap=default&reverseColormap=yes&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&plotUnits=mm%2Fday&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"
    output_image_file = "Daily_Precipitation_30-day_mm_per_day_CPC.png"
    url_type = UrlType.IMAGE
    date1 = datetime.datetime.now() - datetime.timedelta(days=2 + 29)
    date2 = datetime.datetime.now() - datetime.timedelta(days=2)

class Precip_mddb2_90day(Precip_mddb2_30day):
    output_image_file = "Daily_Precipitation_90-day_mm_per_day_CPC.png"
    date1 = datetime.datetime.now() - datetime.timedelta(days=2 + 89)
    date2 = datetime.datetime.now() - datetime.timedelta(days=2)

class Precip_mddb2_180day(Precip_mddb2_30day):
    output_image_file = "Daily_Precipitation_180-day_mm_per_day_CPC.png"
    date1 = datetime.datetime.now() - datetime.timedelta(days=2 + 179)
    date2 = datetime.datetime.now() - datetime.timedelta(days=2)

class Soil_moisture_l1(AbstractImageDLConfig):
    url_template = "https://charts.ecmwf.int/opencharts-api/v1/products/w_soil_moisture/?valid_time={t1_year}-{t1_month}-{t1_day}T00%3A00%3A00Z&base_time={t2_year}-{t2_month}-{t2_day}T00%3A00%3A00Z&area=North+America"
    output_image_file = 'Soil_level1_ECMWF.png'
    url_type = UrlType.JSON
    date1 = datetime.datetime.now()
    date2 = datetime.datetime.now()

class Soil_moisture_l1to3(Soil_moisture_l1):
    url_template = "https://charts.ecmwf.int/opencharts-api/v1/products/w_soil_moisture/?valid_time={t1_year}-{t1_month}-{t1_day}T00%3A00%3A00Z&area=North+America&base_time={t2_year}-{t2_month}-{t2_day}T00%3A00%3A00Z&level=Layer+1+2+3"
    output_image_file = 'Soil_level1-3_ECMWF.png'

class WECWF_24hr_config(AbstractImageDLConfig):
    url_template = "https://charts.ecmwf.int/opencharts-api/v1/products/medium-rain-acc/?valid_time={t1_year}-{t1_month}-{t1_day}T00%3A00%3A00Z&base_time={t2_year}-{t2_month}-{t2_day}T00%3A00%3A00Z&projection=opencharts_north_america"
    output_image_file = '24-hour_accumulated_P_ECMWF.png'
    url_type = UrlType.JSON
    date1 = datetime.datetime.now() + datetime.timedelta(days=1)
    date2 = datetime.datetime.now()

class WECWF_48hr_config(WECWF_24hr_config):
    output_image_file = "48-hour_accumulated_P_ECMWF.png"
    date1 = datetime.datetime.now() + datetime.timedelta(days=2)

class WECWF_72hr_config(WECWF_24hr_config):
    output_image_file = "72-hour_accumulated_P_ECMWF.png"
    date1 = datetime.datetime.now() + datetime.timedelta(days=3)

class WECWF_96hr_config(WECWF_24hr_config):
    output_image_file = "96-hour_accumulated_P_ECMWF.png"
    date1 = datetime.datetime.now() + datetime.timedelta(days=4)

class WECWF_120hr_config(WECWF_24hr_config):
    output_image_file = "120-hour_accumulated_P_ECMWF.png"
    date1 = datetime.datetime.now() + datetime.timedelta(days=5)

class NCEP_Soil_moisture_0to10cm_config(AbstractImageDLConfig):
    url_template = "https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=156115&fileID=0&itype=0&variable=soilw&levelType=Between%200-10%20cm%20BGL&level_units=&level=Between%200-10%20cm%20BGL&timetype=4x&fileTimetype=4x&year1={t1_year}&month1={t1_month}&day1={t1_day}&hr1=00%20Z&year2={t2_year}&month2={t2_month}&day2={t2_day}&hr2=00%20Z&vectorPlot=0&contourLevel=auto&cint=4&lowr=0&highr=200&colormap=default&reverseColormap=yes&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"
    output_image_file = 'Soil_0-10cm_NCEP1.png'
    url_type = UrlType.IMAGE
    date1 = datetime.datetime.now() - datetime.timedelta(days=2)
    date2 = datetime.datetime.now()

class NCEP_Soil_moisture_10to100cm_config(NCEP_Soil_moisture_0to10cm_config):
    url_template = "https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=156110&fileID=0&itype=0&variable=soilw&levelType=Between%2010-200%20cm%20BGL&level_units=&level=Between%2010-200%20cm%20BGL&timetype=4x&fileTimetype=4x&year1={t1_year}&month1={t1_month}&day1={t1_day}&hr1=00%20Z&year2={t2_year}&month2={t2_month}&day2={t2_day}&hr2=00%20Z&vectorPlot=0&contourLevel=auto&cint=0.02&lowr=0.12&highr=0.42&colormap=default&reverseColormap=yes&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"
    output_image_file = "Soil_10-100cm_NCEP1.png"




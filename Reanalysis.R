library(EBImage)
library(curl)


today <- Sys.Date() # Local date
latest_d <- today - 2 
latest_d <- as.character(latest_d)

last_d_30 <- today - 2 - 29
last_d_30 <- as.character(last_d_30)

last_d_90 <- today - 2 - 89
last_d_90 <- as.character(last_d_90)

last_d_180 <- today - 2 - 179
last_d_180 <- as.character(last_d_180)

latest_d_e <- today 
latest_d_e <- as.character(latest_d_e)

t1 <- today + 1
t1 <- as.character(t1)
t2 <- today + 2
t2 <- as.character(t2)
t3 <- today + 3
t3 <- as.character(t3)
t4 <- today + 4
t4 <- as.character(t4)
t5 <- today + 5
t5 <- as.character(t5)

year <- substr(latest_d,1,4) 
month <- substr(latest_d,6,7) 
day <- substr(latest_d,9,10) 

year_l30 <- substr(last_d_30,1,4) 
month_l30 <- substr(last_d_30,6,7) 
day_l30 <- substr(last_d_30,9,10) 

year_l90 <- substr(last_d_90,1,4) 
month_l90 <- substr(last_d_90,6,7) 
day_l90 <- substr(last_d_90,9,10)

year_l180 <- substr(last_d_180,1,4) 
month_l180 <- substr(last_d_180,6,7) 
day_l180 <- substr(last_d_180,9,10)

year_e <- substr(latest_d_e,1,4) 
month_e <- substr(latest_d_e,6,7) 
day_e <- substr(latest_d_e,9,10) 

year_t1 <- substr(t1,1,4)
month_t1 <- substr(t1,6,7) 
day_t1 <- substr(t1,9,10) 

year_t2 <- substr(t2,1,4)
month_t2 <- substr(t2,6,7) 
day_t2 <- substr(t2,9,10) 

year_t3 <- substr(t3,1,4)
month_t3 <- substr(t3,6,7) 
day_t3 <- substr(t3,9,10) 

year_t4 <- substr(t4,1,4)
month_t4 <- substr(t4,6,7) 
day_t4 <- substr(t4,9,10) 

year_t5 <- substr(t5,1,4)
month_t5 <- substr(t5,6,7) 
day_t5 <- substr(t5,9,10) 


#path <- "E:\\Shared\\Reanalysis_data\\"
#path <- "V:\\Reanalysis_data\\"
path <- "Reanalysis_data"


# Tmin
tryCatch({  
img = readImage(paste0("https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=4609&fileID=0&itype=0&variable=tmin&levelType=Surface&level_units=&level=Surface&timetype=day&fileTimetype=day&year1=",year,"&month1=",month,"&day1=",day,"&hr1=00%20Z&year2=",year,"&month2=",month,"&day2=",day,"&hr2=00%20Z&vectorPlot=0&contourLevel=custom&cint=4&lowr=-20&highr=20&colormap=default&reverseColormap=no&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"))
display(img, method = "raster")

f1 = "Daily_MinT_CPC.png"
dev.print(png, filename = paste0(path,f1) , width = dim(img)[1], height = dim(img)[2])
dev.off()
},error = function(e){paste("No data for Tmin CPC")}) #Try catch

# Tmax
tryCatch({  
img_Tmax = readImage(paste0("https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=53407&fileID=0&itype=0&variable=tmax&levelType=Surface&level_units=&level=Surface&timetype=day&fileTimetype=day&year1=",year,"&month1=",month,"&day1=",day,"&hr1=00%20Z&",year,"year2=",year,"&month2=",month,"&day2=",day,"&hr2=00%20Z&vectorPlot=0&contourLevel=custom&cint=4&lowr=-20&highr=40&colormap=default&reverseColormap=no&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"))
display(img_Tmax, method = "raster")

f_Tmax = "Daily_MaxT_CPC.png"
dev.print(png, filename = paste0(path,f_Tmax) , width = dim(img_Tmax)[1], height = dim(img_Tmax)[2])
dev.off()
},error = function(e){paste("No data for Tmax CPC")}) #Try catch

# 30 day precipitation mm/day
tryCatch({   # I just don't change the variable names for convenience.
  img_Tmax = readImage(paste0("https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=2781&fileID=0&itype=0&variable=precip&levelType=Surface&level_units=&level=Surface&timetype=day&fileTimetype=day&createAverage=1&year1=",year_l30,"&month1=",month_l30,"&day1=",day_l30,"&hr1=00%20Z&year2=",year,"&month2=",month,"&day2=",day,"&hr2=00%20Z&vectorPlot=0&contourLevel=custom&cint=2&lowr=0&highr=20&colormap=default&reverseColormap=yes&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&plotUnits=mm%2Fday&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"))
  display(img_Tmax, method = "raster")
  
  f_Tmax = "Daily_Precipitation_30-day_mm_per_day_CPC.png"
  dev.print(png, filename = paste0(path,f_Tmax) , width = dim(img_Tmax)[1], height = dim(img_Tmax)[2])
  dev.off()
},error = function(e){paste("No data for Precipitation CPC")}) #Try catch

# 90 day precipitation mm/day
tryCatch({   # I just don't change the variable names for convenience.
  img_Tmax = readImage(paste0("https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=2781&fileID=0&itype=0&variable=precip&levelType=Surface&level_units=&level=Surface&timetype=day&fileTimetype=day&createAverage=1&year1=",year_l90,"&month1=",month_l90,"&day1=",day_l90,"&hr1=00%20Z&year2=",year,"&month2=",month,"&day2=",day,"&hr2=00%20Z&vectorPlot=0&contourLevel=custom&cint=2&lowr=0&highr=20&colormap=default&reverseColormap=yes&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&plotUnits=mm%2Fday&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"))
  display(img_Tmax, method = "raster")
  
  f_Tmax = "Daily_Precipitation_90-day_mm_per_day_CPC.png"
  dev.print(png, filename = paste0(path,f_Tmax) , width = dim(img_Tmax)[1], height = dim(img_Tmax)[2])
  dev.off()
},error = function(e){paste("No data for Precipitation CPC")}) #Try catch


# 18 day precipitation mm/day
tryCatch({   # I just don't change the variable names for convenience.
  img_Tmax = readImage(paste0("https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=2781&fileID=0&itype=0&variable=precip&levelType=Surface&level_units=&level=Surface&timetype=day&fileTimetype=day&createAverage=1&year1=",year_l180,"&month1=",month_l180,"&day1=",day_l180,"&hr1=00%20Z&year2=",year,"&month2=",month,"&day2=",day,"&hr2=00%20Z&vectorPlot=0&contourLevel=custom&cint=2&lowr=0&highr=20&colormap=default&reverseColormap=yes&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&plotUnits=mm%2Fday&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"))
  display(img_Tmax, method = "raster")
  
  f_Tmax = "Daily_Precipitation_180-day_mm_per_day_CPC.png"
  dev.print(png, filename = paste0(path,f_Tmax) , width = dim(img_Tmax)[1], height = dim(img_Tmax)[2])
  dev.off()
},error = function(e){paste("No data for Precipitation CPC")}) #Try catch
# # # ECMWF soil moisture
# Layer 1
tryCatch({  
req <- curl::curl_fetch_memory(paste0("https://charts.ecmwf.int/opencharts-api/v1/products/w_soil_moisture/?valid_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&base_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&area=North+America"))
test <- jsonlite::prettify(rawToChar(req$content))

ending_1 <- unlist(gregexpr(".png", test))[1]
beginning_1 <- unlist(gregexpr("https://", test))[2]
linknumber <- ending_1 - beginning_1 

link_s1 <- substr(test,beginning_1,beginning_1 + linknumber + 3)

  img_S1_ECMWF = readImage(paste0(link_s1))
  display(img_S1_ECMWF, method = "raster")
# # 
  f_s_ecmwf1 = "Soil_level1_ECMWF.png"
  dev.print(png, filename = paste0(path,f_s_ecmwf1) , width = dim(img_S1_ECMWF)[1], height = dim(img_S1_ECMWF)[2])

  dev.off()
  },error = function(e){paste("No data for Layer1 ECMWF")}) #Try catch
  
  tryCatch({  
  # Layer 1-3
  req <- curl::curl_fetch_memory(paste0("https://charts.ecmwf.int/opencharts-api/v1/products/w_soil_moisture/?valid_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&area=North+America&base_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&level=Layer+1+2+3"))
  test <- jsonlite::prettify(rawToChar(req$content))
  
  ending_2 <- unlist(gregexpr(".png", test))[1]
  beginning_2 <- unlist(gregexpr("https://", test))[2]
  linknumber <- ending_2 - beginning_2 
  
  link_s2 <- substr(test,beginning_2,beginning_2 + linknumber + 3)
  
  img_S2_ECMWF = readImage(paste0(link_s2))
  display(img_S2_ECMWF, method = "raster")
  # # 
  f_s_ecmwf2 = "Soil_level1-3_ECMWF.png"
  dev.print(png, filename = paste0(path,f_s_ecmwf2) , width = dim(img_S2_ECMWF)[1], height = dim(img_S2_ECMWF)[2])
  
  dev.off()
  },error = function(e){paste("No data for Layer1-3 ECMWF")}) #Try catch

##########################################################################
# WECWF 24-hour accumulated precipitation

tryCatch({  
  # 24-hour
  req <- curl::curl_fetch_memory(paste0("https://charts.ecmwf.int/opencharts-api/v1/products/medium-rain-acc/?valid_time=",year_t1,"-",month_t1,"-",day_t1,"T00%3A00%3A00Z&base_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&projection=opencharts_north_america"))
  test <- jsonlite::prettify(rawToChar(req$content))
  
  ending_2 <- unlist(gregexpr(".png", test))[1]
  beginning_2 <- unlist(gregexpr("https://", test))[2]
  linknumber <- ending_2 - beginning_2 
  
  link_s2 <- substr(test,beginning_2,beginning_2 + linknumber + 3)
  
  img_S2_ECMWF = readImage(paste0(link_s2))
  display(img_S2_ECMWF, method = "raster")
  # # 
  f_s_ecmwf2 = "24-hour_accumulated_P_ECMWF.png"
  dev.print(png, filename = paste0(path,f_s_ecmwf2) , width = dim(img_S2_ECMWF)[1], height = dim(img_S2_ECMWF)[2])
  
  dev.off()
},error = function(e){paste("No data for 24-hour accumulated P from ECMWF")}) #Try catch


######################################################################################


##########################################################################
# WECWF 48-hour accumulated precipitation

tryCatch({  
  # 48-hour
  req <- curl::curl_fetch_memory(paste0("https://charts.ecmwf.int/opencharts-api/v1/products/medium-rain-acc/?valid_time=",year_t2,"-",month_t2,"-",day_t2,"T00%3A00%3A00Z&base_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&projection=opencharts_north_america"))
  test <- jsonlite::prettify(rawToChar(req$content))
  
  ending_2 <- unlist(gregexpr(".png", test))[1]
  beginning_2 <- unlist(gregexpr("https://", test))[2]
  linknumber <- ending_2 - beginning_2 
  
  link_s2 <- substr(test,beginning_2,beginning_2 + linknumber + 3)
  
  img_S2_ECMWF = readImage(paste0(link_s2))
  display(img_S2_ECMWF, method = "raster")
  # # 
  f_s_ecmwf2 = "48-hour_accumulated_P_ECMWF.png"
  dev.print(png, filename = paste0(path,f_s_ecmwf2) , width = dim(img_S2_ECMWF)[1], height = dim(img_S2_ECMWF)[2])
  
  dev.off()
},error = function(e){paste("No data for 48-hour accumulated P from ECMWF")}) #Try catch


######################################################################################

##########################################################################
# WECWF 72-hour accumulated precipitation

tryCatch({  
  # 72-hour
  req <- curl::curl_fetch_memory(paste0("https://charts.ecmwf.int/opencharts-api/v1/products/medium-rain-acc/?valid_time=",year_t3,"-",month_t3,"-",day_t3,"T00%3A00%3A00Z&base_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&projection=opencharts_north_america"))
  test <- jsonlite::prettify(rawToChar(req$content))
  
  ending_2 <- unlist(gregexpr(".png", test))[1]
  beginning_2 <- unlist(gregexpr("https://", test))[2]
  linknumber <- ending_2 - beginning_2 
  
  link_s2 <- substr(test,beginning_2,beginning_2 + linknumber + 3)
  
  img_S2_ECMWF = readImage(paste0(link_s2))
  display(img_S2_ECMWF, method = "raster")
  # # 
  f_s_ecmwf2 = "72-hour_accumulated_P_ECMWF.png"
  dev.print(png, filename = paste0(path,f_s_ecmwf2) , width = dim(img_S2_ECMWF)[1], height = dim(img_S2_ECMWF)[2])
  
  dev.off()
},error = function(e){paste("No data for 72-hour accumulated P from ECMWF")}) #Try catch


# WECWF 96-hour accumulated precipitation

tryCatch({  
  # 96-hour
  req <- curl::curl_fetch_memory(paste0("https://charts.ecmwf.int/opencharts-api/v1/products/medium-rain-acc/?valid_time=",year_t4,"-",month_t4,"-",day_t4,"T00%3A00%3A00Z&base_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&projection=opencharts_north_america"))
  test <- jsonlite::prettify(rawToChar(req$content))
  
  ending_2 <- unlist(gregexpr(".png", test))[1]
  beginning_2 <- unlist(gregexpr("https://", test))[2]
  linknumber <- ending_2 - beginning_2 
  
  link_s2 <- substr(test,beginning_2,beginning_2 + linknumber + 3)
  
  img_S2_ECMWF = readImage(paste0(link_s2))
  display(img_S2_ECMWF, method = "raster")
  # # 
  f_s_ecmwf2 = "96-hour_accumulated_P_ECMWF.png"
  dev.print(png, filename = paste0(path,f_s_ecmwf2) , width = dim(img_S2_ECMWF)[1], height = dim(img_S2_ECMWF)[2])
  
  dev.off()
},error = function(e){paste("No data for 96-hour accumulated P from ECMWF")}) #Try catch


# WECWF 120-hour accumulated precipitation

tryCatch({  
  # 120-hour
  req <- curl::curl_fetch_memory(paste0("https://charts.ecmwf.int/opencharts-api/v1/products/medium-rain-acc/?valid_time=",year_t5,"-",month_t5,"-",day_t5,"T00%3A00%3A00Z&base_time=",year_e,"-",month_e,"-",day_e,"T00%3A00%3A00Z&projection=opencharts_north_america"))
  test <- jsonlite::prettify(rawToChar(req$content))
  
  ending_2 <- unlist(gregexpr(".png", test))[1]
  beginning_2 <- unlist(gregexpr("https://", test))[2]
  linknumber <- ending_2 - beginning_2 
  
  link_s2 <- substr(test,beginning_2,beginning_2 + linknumber + 3)
  
  img_S2_ECMWF = readImage(paste0(link_s2))
  display(img_S2_ECMWF, method = "raster")
  # # 
  f_s_ecmwf2 = "120-hour_accumulated_P_ECMWF.png"
  dev.print(png, filename = paste0(path,f_s_ecmwf2) , width = dim(img_S2_ECMWF)[1], height = dim(img_S2_ECMWF)[2])
  
  dev.off()
},error = function(e){paste("No data for 120-hour accumulated P from ECMWF")}) #Try catch

######################################################################################


# NCEP observed soil moisture
# 0-10 cm
tryCatch({
img_s1 = readImage(paste0("https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=156115&fileID=0&itype=0&variable=soilw&levelType=Between%200-10%20cm%20BGL&level_units=&level=Between%200-10%20cm%20BGL&timetype=4x&fileTimetype=4x&year1=",year,"&month1=",month,"&day1=",day,"&hr1=00%20Z&year2=",year,"&month2=",month,"&day2=",day,"&hr2=00%20Z&vectorPlot=0&contourLevel=auto&cint=4&lowr=0&highr=200&colormap=default&reverseColormap=yes&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"))
display(img_s1, method = "raster")

f_s1 = "Soil_0-10cm_NCEP1.png"
dev.print(png, filename = paste0(path,f_s1) , width = dim(img_s1)[1], height = dim(img_s1)[2])
dev.off()


},error = function(e){paste("No data for 0-10 cm NCEP1")}) #Try catch

# 10-100 cm
tryCatch({
img_s2 = readImage(paste0("https://psl.noaa.gov/cgi-bin/mddb2/plot.pl?doplot=1&varID=156110&fileID=0&itype=0&variable=soilw&levelType=Between%2010-200%20cm%20BGL&level_units=&level=Between%2010-200%20cm%20BGL&timetype=4x&fileTimetype=4x&year1=",year,"&month1=",month,"&day1=",day,"&hr1=00%20Z&year2=",year,"&month2=",month,"&day2=",day,"&hr2=00%20Z&vectorPlot=0&contourLevel=auto&cint=0.02&lowr=0.12&highr=0.42&colormap=default&reverseColormap=yes&contourlines=1&colorlines=1&contourfill=1&contourlabels=1&removezonal=0&boundary=AllBoundaries&projection=CylindricalEquidistant&region=Custom&area_north=61&area_west=-140&area_east=-112&area_south=45&centerLat=0.0&centerLon=270.0&mapfill=0.png"))
display(img_s2, method = "raster")

f_s2 = "Soil_10-100cm_NCEP1.png"
dev.print(png, filename = paste0(path,f_s2) , width = dim(img_s2)[1], height = dim(img_s2)[2])
dev.off()

},error = function(e){paste("No data for 10-100 cm NCEP1")}) #Try catch



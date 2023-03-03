# Overview

misc notes that help when testing various docker/podman options for building
and running docker images with the R code.

# Actions / Todo

* testing to see if the r-base w/ manual install of bioconductor is smaller than
  the massive bioconductor image

# Docker / Podman notes
The following does work, and allows running of the script, however something
is going wrong with the script as it continuously reports the data is not
available for all the various sources it attempts to download from.

Build the image:
`podman image build -t r-bioc -f Dockerfile.bioc .`

Create a volume
`podman volume create rvol`

Run image with the volume mount
`podman run  --mount 'type=volume,src=rvol,dst=/Reanalysis_data' r-bioc`

# Description of R script
The script downloads images from various sources.  Some of the urls provide a
json file that then identifies the location of an image, other urls are direct
to image.  All the urls include date ranges.

An example of a url that returns a json data struct is the soil moisture data

* example url:
https://charts.ecmwf.int/opencharts-api/v1/products/w_soil_moisture/?valid_time=2023-02-28T00%3A00%3A00Z&base_time=2023-02-28T00%3A00%3A00Z&area=North+America


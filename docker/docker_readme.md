misc notes re: building docker images

* testing to see if the r-base w/ manual install is smaller than

# build
podman image build -t r-bioc -f Dockerfile.bioc .

aa) create the directory
mkdir Reanalysis_data 

a) create a volume
podman volume create rvol

b) 
# using a volume
podman run  --mount 'type=volume,src=rvol,dst=/Reanalysis_data' r-bioc

# using directory mount
podman run  -v ./Reanalysis_data:/Reanalysis_data r-bioc

# functionality

## looks like it downloads various images

little complex, is the soil moiture that reads a json file to determine
what data is available

* example url:
https://charts.ecmwf.int/opencharts-api/v1/products/w_soil_moisture/?valid_time=2023-02-28T00%3A00%3A00Z&base_time=2023-02-28T00%3A00%3A00Z&area=North+America

https://charts.ecmwf.int/opencharts-api/v1/products/w_soil_moisture/?valid_time=2023-03-01T00%3A00%3A00Z&base_time=2023-03-01T00%3A00%3A00Z&area=North+America

## should cache the data in object store
* ideally every day goes into its own folder

## put together a separate app to display it.
* could be simple app with date picker, for days with data



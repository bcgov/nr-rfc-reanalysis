# trying to get the script working in a gha

* still working on what's required to get bio conductor installed 

# working


got the docker/podman working

### docker/podman build

`docker image build -t r-bioc-test .`

### docker/podman run

`docker run r-bioc-test`

# notes:
the bioconductor docker image is 4.1 Gigs!  bioconductor is only used for very
simple image processing.  Can convert to something that runs with a fraction 
that size.


# Overview

Originally the repository contained the script in `r/r/Reanalysis.R`.  The idea
was to get that script running as a github action.

Attempted to package using docker/podman, however ran into issues when trying
to install bioconductor on top of the r-base image.

Pivoted at that point to using the bioconductor docker image, however that
image is very large (almost 5gigs).

After various attempts to dissect and install only what was required, looked at
what the script is actually doing.  At that point realize the functionality
could be assembled in python or bash with a significantly smaller build step.

# Description

The original R script downloads various images related to soil moisture, and
displays them.

The python code builds on that functionality, adding:
* json schema checks
* config that ties all related image download information together
* functionality to download the available data



### docker/podman build

`docker image build -t r-bioc-test .`

### docker/podman run

`docker run r-bioc-test`

# notes:
the bioconductor docker image is 4.1 Gigs!  bioconductor is only used for very
simple image processing.  Can convert to something that runs with a fraction
that size.


# Plan / Objectives / Idea

* for now download the data to object store
* configure the data as publically accessible
* reference the data in a summary web page
    * could be github pages
    * could wrap it up wiht R-shiny / streamlit / pure JS

Longer term idea
* app with datepicker
* datepicker allows viewing data
* potentially more configuration
* a frontend app that pulls the data directly from the sources, instead of downloading to object store
  first and then storing.

#chooseCRANmirror() 
#install.packages("BiocManager")
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("Biobase")
BiocManager::install("EBImage")
install.packages("curl")

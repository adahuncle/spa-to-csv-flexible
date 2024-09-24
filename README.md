When working with a Nicolet spectrophotometer, the files created are in spa format. While these files can be saved as a csv from the Omnic software, when saving multiple (thousands) of spectra from a split series experiment, it can get tedious to save them manually one at a time as csv. Thus, I created these python scripts to convert them to csv. Due to power limitations, when saving multiple files as a single csv file, instead of saving all the spectra directly into a single file I decided to first convert each spa file individually and then to export them into a joint csv file, where the first column shows the wavenumbers. 
Notice that I specified the wavenumbers that I work with, you may need to change that. When trying to read the wavenumbers from the spa file instead, the computer crashed, so I incorporated them manually.

You will need to install spectrochempy, which works with python 3.9 and 3.10

**Added variable data frame detection so that different IR instruments can be used with this script** -Adahuncle

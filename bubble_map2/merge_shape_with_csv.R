library(raster)
# read data    
p <- shapefile("gadm36_PAK_3.SHP")
# d <- read.csv("path/file.csv")

View(P)
print(p[,c('NAME_3')])
print(names(p))

# merge on common variable, here called 'key'
#m <- merge(p, d, by='key')

# perhaps save as shapefile again
#shapefile(m, "path/merged.shp")


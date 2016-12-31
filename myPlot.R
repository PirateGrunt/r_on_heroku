myFile <- file.path(Sys.getenv('R_SCRIPT_FOLDER_PREFIX'), 'static', 'myPlot.png')
png(filename=myFile)

hist(rnorm(100), main = Sys.time())

invisible(dev.off())

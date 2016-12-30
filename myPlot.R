png(filename="static/myPlot.png")

hist(rnorm(100), main = Sys.time())

invisible(dev.off())

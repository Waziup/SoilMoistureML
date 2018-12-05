set timefmt '%Y-%m-%dT%H:%M:%S'
set xdata time
set datafile sep ','
set terminal pngcairo
set output filename . ".png" 
plot (filename . ".csv") using 2:3 w lines

set terminal wxt
set title "Delta Time for each Request"
set xlabel "# Requests"
set ylabel "Delta Time (s)"
#set xrange [0:500]
plot "data" using 1 title "RTT" with lines,\
"data" using 2 title "Average RTT" with lines
pause 1
reread
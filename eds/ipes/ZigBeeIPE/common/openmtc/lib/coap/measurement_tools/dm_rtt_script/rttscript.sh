#!/bin/sh
# Computes the response time from a pcap file with coap
# Takes retransmit into account !!!!!!

tshark -Tfields -e frame.time_relative -e udp.srcport -e udp.dstport -e data.data -R 'udp.srcport < 38000' -r $1 |cut -d':' -f1,3,4 | sed 's/\(.*\)..:\(..:..\)/\1\2/' |sort -k4,4 -k1,1n | while read a; do
msgid=`echo $a | cut -d' ' -f4`
t=`echo $a | cut -d' ' -f1`
port=`echo $a | cut -d' ' -f2`

if [ "$msgid" = "$previd" ]; then
lasttime=$t
dstport=`echo $a | cut -d' ' -f3`
	if [ "$port1" = "$dstport" ]; then
		echo -n $port1 ' '
		echo -n $previd ' '
		echo -n $lasttime-$firsttime "  "
		echo $lasttime - $firsttime | bc 
	fi 
continue
fi
port1=$port

firsttime=$t
previd=$msgid

done | while read b; do
port=`echo $b | cut -d' ' -f1`
time=`echo $b | cut -d' ' -f4`
if [ "$port" = "$preport" ]; then
	sum=`echo $sum + $time | bc`
	continue
fi
echo -n $preport ' '
echo $sum

sum=0
preport=$port
sum=$time
done



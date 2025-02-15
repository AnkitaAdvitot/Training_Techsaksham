#!/bin/bash
echo -n Enter number
read a
while [ $a -lt 10 ]
do
	echo $a
	a=`expr $a + 1`
done

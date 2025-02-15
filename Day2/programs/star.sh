read -p "Enter number " num
for ((i=0;i<num;i++))
do
	for ((k=0;k<num-i;k++))
	do
		echo -n " "
	done
	for ((k=0;k<i+1;k++))
	do
		echo -n "* "
	done
	echo 
done

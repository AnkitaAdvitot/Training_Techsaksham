read -p "Enter number " num
for ((i=1;i<=num;i++))
do
	for ((k=0;k<num-i;k++))
	do
		echo -n " "
	done
	for ((k=0;k<i;k++))
	do
		echo -n "$i "
	done
	echo 
done

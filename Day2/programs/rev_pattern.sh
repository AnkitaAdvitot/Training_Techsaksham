read -p "Enter number " num
for ((i=num;i>0;i--))
do
	for ((k=0;k<num-i;k++))
	do
		echo -n " "
	done
	for ((k=i;k>0;k--))
	do
		echo -n "$k "
	done
	echo ""
done

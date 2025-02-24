read -p "Enter number " num
i=1
for ((j=2;j<=num/2;j++))
do
	if [ $((num % 2)) -eq 0 ]
	then
		echo "$num is not prime number "
		i=0
		break;
		fi
done
if [ $i -eq 1 ]
then
	echo "$num is prime number"
fi


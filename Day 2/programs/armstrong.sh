read -p "Enter number " num
len=0
temp=$num
t1=$num
sum=0
while [ $num -ne 0 ]
do
	num=$((num/10))
	((len++))
done
while [ $temp -ne 0 ]
do
	digit=$((temp%10))
	digit=$((digit**len))
	sum=`expr $sum + $digit`
	temp=$((temp/10))
done
if [ $t1 -eq $sum ]
then
	echo "$t1 is armstrong "
else
	echo "$t1 is not armstrong"
fi


read -p "Enter number " num
function fibo(){
	a=0
	b=1
	echo -n "$a "
	echo -n  "$b "
	sum=$((a + b ))
	while [ $sum -lt $1 ]
	do 
		sum=$((a + b))
		echo -n "$sum "
		a=$b
		b=$sum
	done
}
fibo num

function odd(){
	for ((i=1;i<=n;i++))
	{
		if [ $(($i % 2)) -ne 0 ]
		then
			echo -n  "$i "
		fi
	}
}
read -p "Enter value of n " n
odd n

function inv(){
	for ((i=$1;i>0;i--))
	do
		for ((j=$i;j>0;j--))
		do
			echo -n "$i "
		done
		echo ""
	done
}
read -p "Enter value of n " n
inv n

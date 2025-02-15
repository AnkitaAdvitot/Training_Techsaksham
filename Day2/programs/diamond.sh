
function upper(){
	n=$1
	for ((i=1;i<=n;i++))
	do
		for ((k=0;k<n-i;k++))
		do
			echo -n " "
		done
		for ((k=0;k<i;i++))
		do
			echo -n "* "
		done
		echo ""
	done
}
function lower(){
	n=$1
	for ((i=n;i>0;i--))
	do
		for ((k=0;k<n-i;k++))
		do
			echo -n " "
		done
		for ((k=0;k<i;k++))
		do
			echo -n "* "
		done
		echo ""
	done
}

read -p "Enter number " n
upper $n
lower $n




for ((i=1;i<=10;i++))
do 
if [ $i -eq 3 ]
then 
continue
fi 
echo $i
done

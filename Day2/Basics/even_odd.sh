echo -n “enter num”
read a
if [ $((a % 2)) -eq 0 ]
then
echo “num is even”
else
echo “num is odd”
fi

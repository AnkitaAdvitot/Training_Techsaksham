#!/bin/bash
function welcome(){
	echo "Welcome to function"
}
welcome
echo "Function with arguments"
function addition(){
	rel=$(( $1 + $2 ))
	echo "Addition of $1 and $2 is $rel"
}
addition 10 20 
echo "Multiplication function "
function multi(){
	mul=$(( $1 * $2 ))
	echo "Multiplication of $1 and $2 is $mul"
}
multi 10 20

echo "Function with return"
function Return(){
	return "My name is $1 , my age is $2 and i live in $3"
}
Return Ankita 20 Akkalkot
echo "$?"

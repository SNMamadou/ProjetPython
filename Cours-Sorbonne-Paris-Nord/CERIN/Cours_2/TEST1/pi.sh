#!/bin/sh

#
# Estimation de pi par une methode de Monte-Carlo
# DÃ©pendences logicielles :
#     bc
# Exemple d'execution a distance :
#     cerin@lipn-ssh:~$ ssh cerin@ankara '/bin/sh public_html/pi.sh'
#     cerin@ankara's password: 
#     3.14400000000000000000
#     cerin@lipn-ssh:~$ 
#

START=1
END=1000

TOTAL=0
INSIDE=0

while [[ $START -le $END ]]
do
	 
    x=$RANDOM
    x=`echo "$x / 32767"| bc -l`

    y=$RANDOM
    y=`echo $y / 32767 | bc -l`

    #echo "Coordonnee $c : ($x, $y)"

    xxyy=`echo "($x * $x + $y * $y) <= 1 " | bc -l`

    if [[ $xxyy -eq 1 ]]; then
	INSIDE=$((INSIDE+1))
    fi

    TOTAL=$((TOTAL+1))
    
    START=$(($START + 1))

done

#echo "$INSIDE $TOTAL"
echo "$INSIDE*4/$TOTAL" | bc -l

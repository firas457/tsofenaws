

export sum=0

for FILE in *;
do sum=$(($sum +${#FILE}));
 done

echo $sum

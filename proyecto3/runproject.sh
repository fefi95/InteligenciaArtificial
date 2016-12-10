#! /bin/bash

echo "Compiling minisat..."
# export MROOT=minisat
cd minisat/simp
make rs
cp minisat_static ../..
cd ../..

echo "done!"
echo "Compiling encode.cpp"
make

echo "done!"
echo "Running encoding..."

rm -f output.txt

while read line || [[ -n "$line" ]]; 
do
	# Add the actual game state to the file.
	echo $line
	echo $line > gameState.txt

	# Encode the file.
	./encode gameState.txt

	# Use minisat.
	./minisat_static encode.cnf decode.txt -no-luby -rinc=1.5 -phase-saving=0 -rnd-freq=0.02
	
	# Decore the result
	echo $line >> output.txt
	./decode decode.txt $line[0] $line[1] 
	echo >> output.txt
done < input.txt

# Delete the aux file.
rm -f aux.txt decode.txt
make clean



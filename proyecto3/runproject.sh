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
./encode input.txt
./minisat_static encode.cnf decode.txt -no-luby -rinc=1.5 -phase-saving=0 -rnd-freq=0.02

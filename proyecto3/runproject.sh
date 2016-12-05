#! /bin/bash

echo "Compiling minisat..."
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

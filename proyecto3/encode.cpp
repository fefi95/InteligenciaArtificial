/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-11121
    Stefani Castellanos 11-11394

    This file contains the encoding for the SAT problem especified
    It outputs a file in SATLIB format to be use with minisat
*/

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, const char **argv) {
    if( argc < 2 ) {
        std::cout << "input file missing!" << std::endl;
        return 1;
    }
    ifstream input; // input file
    ofstream encode; // output encode SAT file

    input.open(argv[1]);
    encode.open("encode.cnf");
    int N, M; // dimesions (row, colmuns) of the problem
    input >> N;
    input >> M;
    // std::cout << N << M << std::endl;
    char cell;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            input >> cell;
            // std::cout << "cell:" << cell << std::endl;
        }
    }


    input.close();
    encode.close();
    return 0;
}

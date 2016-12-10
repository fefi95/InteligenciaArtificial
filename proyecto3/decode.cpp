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
#include <string>

using namespace std;

int main(int argc, const char **argv) {
    if( argc < 2 ) {
        std::cout << "input file missing!" << std::endl;
        return 1;
    }
    ifstream input; // solution to the problem file
    ofstream output; // output output SAT file

    input.open(argv[1]);
    output.open("output.txt", std::ios::app);
    string sol; // dimensions (row, colmuns) of the problem
    input >> sol;
    int N = atoi(argv[2]);
    int M = atoi(argv[3]);
    int segment;

    // reading horizontal segments from input file
    string hor[N + 1], horTemp;
    for (int i = 0; i < N + 1; i++) {
        horTemp = "";
        for (int j = 0; j < M; j++) {
            input >> segment;
            if (segment < 0) {
                horTemp += "0";
            }
            else {
                horTemp += "1";
            }
        }
        hor[i] = horTemp;
        // std::cout << i+1 << " " << hor[i] << std::endl;
    }
    // std::cout << "vertical:" << std::endl;
    // reading vertical segments from input file
    string ver[M], verTemp;
    for (int i = 0; i < M; i++) {
        verTemp = "";
        for (int j = 0; j < M + 1; j++) {
            input >> segment;
            if (segment < 0) {
                verTemp += "0";
            }
            else {
                verTemp += "1";
            }
        }
        ver[i] = verTemp;
        // std::cout << i+1 << " " << ver[i] << std::endl;
    }

    // write to output
    output << N << " " << M << " ";
    for (int i = 0; i < N; i++) {

        output << hor[i] << " ";
        output << ver[i] << " ";
    }
    output << hor[N] << " ";
    input.close();
    output.close();
    return 0;
}

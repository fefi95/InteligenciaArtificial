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
    ifstream input; // input file
    ofstream encode; // output encode SAT file

    input.open(argv[1]);
    encode.open("encode.cnf");
    int N, M; // dimensions (row, colmuns) of the problem
    input >> N;
    input >> M;

    //WARNING: NUMBER OF VARIABLES AND CLAUSES WITHOUT CONSIDERING THAT IS A COMPLETE CYCLE. FIX
    int numVar = (N + 1) * N * 2;
    int numClauses = 0;

    encode << "p cnf " << numVar << " " << numClauses << std::endl;
    // std::cout << N << M << std::endl;
    char cell;
    int val;
    string clause; // all clauses represents a CNF problem.
    string up, dw, lt, rt; // every segment that surrounds one cell

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            input >> cell;
            val = (i - 1) * M + j;
            switch (cell) {
                // case ' ': break;
                case '.':
                    break;
                case '0':
                        // all surrounding segments are false
                        up = std::to_string(-val);
                        dw = std::to_string(-(i * M + j));
                        lt = std::to_string(-(val + i + N * (M + 1) - 1));
                        rt = std::to_string(-(val + i + N * (M + 1)));
                        clause  =  up + " 0\n";
                        clause +=  dw + " 0\n";
                        clause +=  lt + " 0\n";
                        clause +=  rt + " 0\n";
                    break;
                case '1':
                    break;
                case '2':
                    break;
                case '3':
                    break;
                case '4':
                        // all surrounding segments are true
                        up = std::to_string(val);
                        dw = std::to_string(i * M + j);
                        lt = std::to_string(val + i + N * (M + 1) - 1);
                        rt = std::to_string(val + i + N * (M + 1));
                        clause  =  up + " 0\n";
                        clause +=  dw + " 0\n";
                        clause +=  lt + " 0\n";
                        clause +=  rt + " 0\n";
                    break;
            }
            // std::cout << "cell:" << cell << std::endl;
            encode << clause << std::endl;
            clause = "";
        }
    }


    input.close();
    encode.close();
    return 0;
}

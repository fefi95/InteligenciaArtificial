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
    string clause = ""; // all clauses represents a CNF problem.
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
                        encode << "c rules for 0:" << std::endl;
                        // all surrounding segments are false
                        up = std::to_string(-val);
                        dw = std::to_string(-(i * M + j));
                        lt = std::to_string(-(val + i + N * (M + 1) - 1));
                        rt = std::to_string(-(val + i + N * (M + 1)));
                        clause  =  up + " 0\n";
                        clause +=  dw + " 0\n";
                        clause +=  lt + " 0\n";
                        clause +=  rt + " 0\n";
                        encode << clause;
                    break;
                case '1':
                        up = std::to_string(val);
                        dw = std::to_string(i * M + j);
                        lt = std::to_string(val + i + N * (M + 1) - 1);
                        rt = std::to_string(val + i + N * (M + 1));

                        encode << "c rules for 1:" << std::endl;
                        clause  =  up + " " + dw +  " " + lt +  " " + rt + " 0\n";

                        // up segment is true and the rest are false
                        clause +=  "-" + up + " -" + dw + " 0\n";
                        clause +=  "-" + up + " -" + lt + " 0\n";
                        clause +=  "-" + up + " -" + rt + " 0\n";

                        // down segment is true and the rest are false
                        clause +=  "-" + dw + " -" + lt + " 0\n";
                        clause +=  "-" + dw + " -" + rt + " 0\n";

                        // left segment is true and the rest are false
                        clause +=  "-" + lt + " -" + rt + " 0\n";
                        encode << clause;
                    break;
                case '2':

                        up = std::to_string(val);
                        dw = std::to_string(i * M + j);
                        lt = std::to_string(val + i + N * (M + 1) - 1);
                        rt = std::to_string(val + i + N * (M + 1));

                        encode << "c rules for 2:" << std::endl;

                        // up and down segment are true and the rest are false
                        clause +=  "-" + up + " -" + dw + " -"+ lt + " 0\n";
                        clause +=  "-" + up + " -" + dw + " -"+ rt + " 0\n";
                        clause +=  rt + " " + lt + " " + dw + " 0\n";
                        clause +=  rt + " " + lt + " " + up + " 0\n";

                        // up and left segment are true and the rest are false
                        // clause +=  "-" + up + " -" + lt + " -"+ dw + " 0\n";
                        clause +=  "-" + up + " -" + lt + " -"+ rt + " 0\n";
                        // clause +=  rt + " " + dw + " " + lt + " 0\n";
                        clause +=  rt + " " + dw + " " + up + " 0\n";

                        // up and right segment are true and the rest are false
                        // clause +=  "-" + up + " -" + rt + " -"+ dw + " 0\n";
                        // clause +=  "-" + up + " -" + rt + " -"+ lt + " 0\n";
                        // clause +=  lt + " " + dw + " " + rt + " 0\n";
                        clause +=  lt + " " + dw + " " + up + " 0\n";

                        // down and left segment are true and the rest are false
                        // clause +=  "-" + dw + " -" + lt + " -"+ up + " 0\n";
                        clause +=  "-" + dw + " -" + lt + " -"+ rt + " 0\n";
                        // clause +=  up + " " + rt + " " + dw + " 0\n";
                        clause +=  up + " " + rt + " " + lt + " 0\n";

                        // down and right segment are true and the rest are false
                        // clause +=  "-" + dw + " -" + rt + " -"+ up + " 0\n";
                        // clause +=  "-" + dw + " -" + rt + " -"+ lt + " 0\n";
                        // clause +=  up + " " + lt + " " + dw + " 0\n";
                        // clause +=  up + " " + lt + " " + rt + " 0\n";

                        // left and right segment are true and the rest are false
                        // clause +=  "-" + lt + " -" + rt + " -"+ up + " 0\n";
                        // clause +=  "-" + lt + " -" + rt + " -"+ dw + " 0\n";
                        // clause +=  up + " " + dw + " " + lt + " 0\n";
                        // clause +=  up + " " + dw + " " + rt + " 0\n";
                        encode << clause;
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
                        encode << clause;
                    break;
            }
            // std::cout << "cell:" << cell << std::endl;
            clause = "";
        }
    }


    input.close();
    encode.close();
    return 0;
}

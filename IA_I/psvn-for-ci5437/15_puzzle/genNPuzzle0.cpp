#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>

using namespace std;

string convertInt(int number)
{
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}

int main(int argc, char *argv[])
{

  /*******            VARIABLES           ************/
  int N, M;        // Numbers of rows and columns for the board.
  string boardS;   // String with the board size.
  string title;    // String for the title.
  string ant1,cons1; // Antecedent and consecuence of the rule 1.
  string ant2,cons2; // Antecedent and consecuence of the rule 2.
  string ant3,cons3; // Antecedent and consecuence of the rule 3.
  string ant4,cons4; // Antecedent and consecuence of the rule 4.
  ofstream file;   // The PSVN file with the N-Puzzle's rules.
  string nameFile; // Name for the PSVN file with the rules.

  cout << "ENTER THE NUMBER OF ROWS AND COLUMNS FOR THE BOARD: ";
  cin >> N >> M;   // We obtain the numbers of rows and columns.
  boardS = convertInt(N * M);
  title = convertInt(N * M - 1);
  // TODO: Verify the input.

  /*******       CREATE THE PSVN FILE     ************/
  nameFile = title + "_Puzzle.psvn";
  file.open(nameFile.c_str());

  file << "# " + title + "-puzzle " + "(" + convertInt(N) + "x" + convertInt(M)
          + ") \n\n";

  // Define the domain of the game.
  file << "# Define a domain called 'tile' consisting of 16 constants \n";
  file << "# B is for the blank 'tile' \n";
  file << "DOMAIN tile " + boardS + "\n";
  file << "       B";
  for (int i = 0; i < N*M; ++i)
  {
    file << " " << i;
    if (i == N*M-1) file << "\n\n";
  }

  // Define the number of state variables.
  file << "# number of state variables \n";
  file << boardS + "\n\n";

  for (int i = 0; i < N * M; i++)
  {
    file << "tile ";
    if (i == N*M-1) file << "\n\n";
  }

  // Create the rules.
  for(int i = 0; i < N*M; i++)
  {
    // BASE CASE:
    // If we are in a corner...
    if (i == 0){                    // Upper left corner.
        // ans1 and cons1 are for the right rule.
        // ans2 and cons2 are for the down rule.
        for (int j = 0; j < N*M; j++){
          if (j == 0){
            ant1 = "B X";
            cons1 = "X B";
            ant2 = "B";
            cons2 = "X";
          }else if (j == 1){
            ant2 += " -";
            cons2 += " -";
          }else if (j == N){
            ant1 += " -";
            cons1 += " -";
            ant2 += " X";
            cons2 += " B";
          }else{
            ant1 += " -";
            ant2 += " -";
            cons1 += " -";
            cons2 += " -";
          }
        }

        file << ant1 + " => " + cons1 + " LABEL RIGHT \n";
        file << ant2 + " => " + cons2 + " LABEL DOWN \n";
        continue;
    }
    else if (i == N-1){             // Upper right corner.
      // ans1 and cons1 are for the left rule.
      // ans2 and cons2 are for the down rule.
      ant1 = ant2 = "-";
      cons1 = cons2 = "-";
      for (int j = 1; j < N*M; j++){
        if (j == N - 2){
          ant1 += " B";
          ant2 += " -";
          cons1 += " X";
          cons2 += " -";
        }
        else if (j == N - 1){
          ant1 += " X";
          ant2 += " B";
          cons1 += " B";
          cons2 += " X";
        }else if (j == N+M-1) {
          ant1 += " -";
          ant2 += " X";
          cons1 += " -";
          cons2 += " B";
        }else{
          ant1 += " -";
          ant2 += " -";
          cons1 += " -";
          cons2 += " -";
        }
      }

      file << ant1 + " => " + cons1 + " LABEL RIGHT \n";
      file << ant2 + " => " + cons2 + " LABEL DOWN \n";
      continue;
    }
    else if (i == N*(M-1)){         // Lower left corner.
      // ans1 and cons1 are for the up rule.
      // ans2 and cons2 are for the right rule.
      ant1 = ant2 = "-";
      cons1 = cons2 = "-";
      for (int j = 1; j < N*M; j++){
        // Tile upwards to the blank.
        if ((j == N*(M -2) && M==N) ||
            (j == N*(M -1)-N && M!=N)){
          ant1 += " X";
          ant2 += " -";
          cons1 += " B";
          cons2 += " -";
        }
        // Tile of the blank.
        else if (j == N*(M -1)){
          ant1 += " B";
          ant2 += " B";
          cons1 += " X";
          cons2 += " X";
        }
        // Tile next to the blank.
        else if (j == N*(M -1) + 1){
          ant1 += " -";
          ant2 += " X";
          cons1 += " -";
          cons2 += " B";
        }else{
          ant1 += " -";
          ant2 += " -";
          cons1 += " -";
          cons2 += " -";
        }
      }

      file << ant1 + " => " + cons1 + " LABEL UP \n";
      file << ant2 + " => " + cons2 + " LABEL RIGHT \n";
      continue;
    }
    else if (i == N*M-1){           // Lower right corner.
      // ans1 and cons1 are for the left rule.
      // ans2 and cons2 are for the up rule.
      ant1 = ant2 = "-";
      cons1 = cons2 = "-";
      for (int j = 1; j < N*M; j++){
        // Tile upwards to the blank.
        if (j == N*M-N-1){
          ant2 += " X";
          ant1 += " -";
          cons2 += " B";
          cons1 += " -";
        }
        // Tile of the blank.
        else if (j == N*M -1){
          ant1 += " B";
          ant2 += " B";
          cons1 += " X";
          cons2 += " X";
        }
        // Tile behind to the blank.
        else if (j == N*M-2){
          ant2 += " -";
          ant1 += " X";
          cons2 += " -";
          cons1 += " B";
        }else{
          ant1 += " -";
          ant2 += " -";
          cons1 += " -";
          cons2 += " -";
        }
      }

      file << ant1 + " => " + cons1 + " LABEL LEFT \n";
      file << ant2 + " => " + cons2 + " LABEL UP \n";
      continue;
    }
  }

  // If we are in the borders.

  file << "GOAL B 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15";
  file.close();
  return 0;
}

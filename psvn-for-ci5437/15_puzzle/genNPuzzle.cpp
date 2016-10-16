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
  ofstream file;   // The PSVN file with the N-Puzzle's rules.
  string nameFile; // Name for the PSVN file with the rules.

  cout << "ENTER THE NUMBER OF ROWS AND COLUMNS FOR THE BOARD: ";
  cin >> N >> M;   // We obtain the numbers of rows and columns.
  boardS = convertInt(N * M);
  title = convertInt(N * M - 1);
  // TODO: Verify the input.

  /*******       CREATE THE PSVN FILE     ************/
  nameFile = boardS + "_Puzzle.psvn";
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
    if (i == 15) file << "\n\n";
  }

  file << "# number of state variables \n";
  file << boardS + "\n";


  file << "GOAL B 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15";


  file.close();
  return 0;

}

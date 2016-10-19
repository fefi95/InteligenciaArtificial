#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>


using namespace std;

// Let you convert an integer to string.
string convertInt(int number){
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}

// Let you obtain the total nodes on the actual label.
unsigned long long int bounded_dfs_visit(state_t* state, int deep, int bound, int history){
  int ruleid;
  state_t child;
  unsigned long long int numNodoAct = 0;
  ruleid_iterator_t iter;

  if (deep == bound) return 1;
  else{

    init_bwd_iter(&iter, state);

    if (is_goal(state)) {
        // print the distance then the state
        //printf("the cost of the path is: %d\n",);
        return numNodoAct + 1;
    }

    while( (ruleid = next_ruleid(&iter)) >= 0 ){

      if (bwd_rule_valid_for_history(history, ruleid) != 0){
        apply_bwd_rule(ruleid, state, &child);
        int nextHistory = next_bwd_history(history, ruleid);

        unsigned long long int totalAux = bounded_dfs_visit(&child, deep + 1, bound, nextHistory);
        numNodoAct += totalAux;
      }
    }
  }

  return numNodoAct + 1;
}

// Let you use the Iterative Deepening DFS.
void iterative_deepening_depth_first_search(int bound, state_t* state)
{
  //int goal_num;                               // ID of the goal condition.
  unsigned long long int totalNodes = 0;       // Total nodes on the actual bound.
  unsigned long long int oldTotalNodes = 0;    // Total nodes on the last bound.
  int cost = 0;


  // Perform depth-bounded searches with increasing depth bounds.
  for (int i = 0; i <= bound; i++){
      int history = init_history;
      totalNodes = bounded_dfs_visit(state, 0, i, history);
      cout << "Deep " + convertInt(i) + ": ";
      cout << convertInt(totalNodes - oldTotalNodes) + '\n';
      oldTotalNodes = totalNodes;
  }

  // Print the total nodes of every label.

}

int main(int argc, char **argv){

  char const* const fileName = argv[1]; /* should check that argc > 1 */
  FILE* fileIn = fopen(fileName, "r"); /* should check the result */
  char state_line[500];

  // Output file
  ofstream fileOut;
  fileOut.open(argv[2]);

  ssize_t nchars;
  state_t state; // state_t is defined by the PSVN API. It is the type used for individual states.

  // Perform depth-bounded searches with increasing depth bounds.

  int bound = 0;
  char buffer[1000];
  fileOut << "grupo, algorithm, domain, instance, cost, generated, time, gen_per_sec";
  while (fgets(state_line, sizeof(state_line), fileIn))  {
      bound = 0;
      sprintf(buffer, "El estado inicial es: %s \n", state_line);
      cout << buffer;
      nchars = read_state(state_line, &state);
      while(1){
        if (is_goal(&state)) {
            // print the distance then the state
            //printf("the cost of the path is: %d\n",);
            cout << "SALI!";
            break;
        }
        iterative_deepening_depth_first_search(bound, &state);
        bound++;
      }
  }

  fclose(fileIn);
}

#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>
#include <ctime>

using namespace std;

int cost = -1;

// Let you convert an integer to string.
string convertInt(int number){
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}

// Let you obtain the total nodes on the actual label.
int64_t bounded_dfs_visit(state_t* state, int deep, int bound, int history){

  int ruleid;
  state_t child;
  ruleid_iterator_t iter;
  int64_t numNodoAct = 0;
  cost = -1;

  if (deep > bound) return numNodoAct + 1;
  if (is_goal(state)){
    cost = deep;
    return numNodoAct + 1;
  }

  init_bwd_iter(&iter, state);
  while( (ruleid = next_ruleid(&iter)) >= 0 ){
    if (bwd_rule_valid_for_history(history, ruleid) != 0){
      apply_bwd_rule(ruleid, state, &child);
      int nextHistory = next_bwd_history(history, ruleid);
      int64_t totalAux = bounded_dfs_visit(&child, deep + 1, bound, nextHistory);
      numNodoAct += totalAux;
      if (cost != -1) return numNodoAct + 1;
    }
  }

  return numNodoAct + 1;
}

// Let you use the Iterative Deepening DFS.
int64_t iterative_deepening_depth_first_search(state_t* state)
{
  //int goal_num;                               // ID of the goal condition.
  int bound = 0;
  //int cost = -1;
  clock_t start_t, end_t, total_t;

  start_t = clock();
  end_t = clock() + 30;

  int64_t totalNodes = 0;

  // Perform depth-bounded searches with increasing depth bounds.
  while (start_t < end_t){
      int history = init_history;
      totalNodes += bounded_dfs_visit(state, 0, bound, history);
      if (cost != -1) return totalNodes;
      bound += 1;
  }

  return totalNodes;
}

int main(int argc, char **argv){

  // Input file.
  char const* const fileName = argv[1]; /* should check that argc > 1 */
  FILE* fileIn = fopen(fileName, "r");
  char state_line[500];                 /* The state to use. */

  // Output file
  ofstream fileOut;
  fileOut.open(argv[2]);

  ssize_t nchars;     /* Char amount readed */
  state_t state;      /* Initial State. */

  int bound;          /* Limit deep. */
  char buffer[1000];  /* FOR TESTING. */
  //int cost;

  /* Header for the out file. */
  fileOut << "grupo, algorithm, domain, instance, cost, generated, time, gen_per_sec\n";

  /* While exist states to read... */
  while (fgets(state_line, sizeof(state_line), fileIn))  {
      cost = 0;
      sprintf(buffer, "%s", state_line);
      cout << buffer;

      /* Convert the string to an actual state. */
      nchars = read_state(state_line, &state);
      bound = 0;

      // fileOut << "X, dfid, pancake16, \"";
      // fileOut << buffer;
      // fileOut << "\",";

      cout << "------------------------------------------------ \n";
      int64_t totalNodes = iterative_deepening_depth_first_search(&state);
      cout << "cost: " + convertInt(cost) + "\n";
      cout << "totalNodes: " + convertInt(totalNodes) + "\n";
  }

  fclose(fileIn);
  fileOut.close();
}

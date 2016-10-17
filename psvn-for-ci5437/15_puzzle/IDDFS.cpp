#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>

using namespace std;

string convertInt(int number){
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}

int64_t bounded_dfs_visit(state_t state, int deep, int bound, int history){
  int64_t numNodoAct = 0;
  int ruleid;
  state_t child;
  ruleid_iterator_t iter;

  if (deep == bound - 1) return 1;
  else{

    init_fwd_iter(&iter, &state);
    while( (ruleid = next_ruleid(&iter)) >= 0 ){
      if (fwd_rule_valid_for_history( history, ruleid) != 0){
        int nextHistory = next_fwd_history(history, ruleid);
        apply_fwd_rule(ruleid, &state, &child);
        numNodoAct = bounded_dfs_visit(state, deep + 1, bound, nextHistory);
      }
    }
  }

  return numNodoAct + 1;
}

void iterative_deepening_depth_first_search()
{
  state_t state;
  int goal_num;  // ID of the goal condition.
  int bound = 11; // The deep bound.
  int64_t totalNodes = 0;
  int64_t oldTotalNodes = 0;

  // Add the goal state.
  first_goal_state(&state, &goal_num);

  // Perform depth-bounded searches with increasing depth bounds.
  for (int i = 0; i < bound; i++){
      int history = init_history;
      int64_t numNodoAct = bounded_dfs_visit(state, i, bound, history);
      cout << "El nivel " + convertInt(bound - i - 1) + " tiene " + convertInt(numNodoAct) + " nodos.\n";
      oldTotalNodes = numNodoAct;
  }
}

int main(int argc, char **argv){
  iterative_deepening_depth_first_search();
}

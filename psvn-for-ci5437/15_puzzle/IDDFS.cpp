
int iterative_deepening_depth_first_search()
{
  state_t state, child;
  int goal_num;  // ID of the goal condition.
  int bound = 1; // The deep bound.
  int ruleid;
  int64_t totalNodes = 0;
  ruleid_iterator_t iter;

  // Add the goal state.
  first_goal_state(&state, &goal_num);

  // Perform depth-bounded searches with increasing depth bounds.
  for (int i = 0; i < bounds; i++){
      int history = init_history;
      int64_t numNodoAct = bounded_dfs_visit(state, i, bounds, history);
      cout << "El nivel " + i + " tiene " + numNodoAct + " nodos."
  }
}

int64_t bounded_dfs_visit(state_t state, int deep, int bounds, int history){
  int64_t numNodoAct = 0;

  if deep == bounds - 1 return 1
  else{

    init_fwd_iter(&iter, &state);
    while( (ruleid = next_ruleid(&iter)) >= 0 ){
      if (fwd_rule_valid_for_history( history, ruleid) != 0){
        int nextHistory = next_fwd_history(history, ruleid);
        apply_fwd_rule(ruleid, &state, &child);

        numNodoAct = bounded_dfs_visit(state, int deep + 1, int bounds, nextHistory);
      }
    }
  }

  return numNodoAct + 1;
}

int main(int argc, char **argv){
  iterative_deepening_depth_first_search();

}

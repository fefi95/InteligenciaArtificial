/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-...
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for A* algorithm
*/
#include <vector>
#include "priority_queue.hpp"

int main(int argc, char **argv) {

    int d;
    // Priority Queue ordered by f-value: f (n) = g(n) + h(s)
    PriorityQueue<state_t> open;
    state_map_t *map = new_state_map(); // contains the cost-to-goal for all states that have been generated
    /*
    set-color(init(), Gray)
    set-distance(init(), 0)
    q.insert(make-root-node(init()), h(init()))
    */

    // add goal states
    first_goal_state(&state, &d);
    do {
        state_map_add(map, &state, 0);
        int cost = h(&state);
        open.Add(cost, cost, state);
    } while( next_goal_state(&state, &d) );

    // search
    while (!open.empty()){
        // remove top state from priority state
        state = open.Top();
        open.Pop();
        d = open.CurrentPriority();

        if (is_goal(&state)) {
            // print the distance then the state
            printf("%d  ", d);
            print_state(stdout, &state);
            printf(" \n");
        }

        // check if we already expanded this state.
        // (entries on the open list are not deleted if a cheaper path to a state is found)
        const int *best_dist = state_map_get(map, &state);
        assert(best_dist != NULL);
        if( *best_dist < d ) continue;

        // expand node look at all predecessors of the state
        init_bwd_iter(&iter, &state);
        while( (ruleid = next_ruleid(&iter) ) >= 0 ) {
            apply_bwd_rule(ruleid, &state, &child);
            const int child_d = d + get_bwd_rule_cost(ruleid) + h(&child);

            // check if either this child has not been seen yet or if
            // there is a new cheaper way to get to this child.
            const int *old_child_d = state_map_get(map, &child);
            if( (old_child_d == NULL) || (*old_child_d > child_d) ) {
                // add to open with the new distance
                state_map_add(map, &child, child_d);
                open.Add(child_d, child_d, child);
            }
        }
    }
    /*
    while !q.empty() {
        Node n = q.pop()
        % check for goal
        if n.state.is-goal() return n
        % expand node
        best-first-search-expansion(n, q)
        set-color(n.state, Black)
        return null
    */
}


/*
Node best-first-search-expansion(Node n, PriorityQueue q):
    foreach <s,a> in n.state.successors()
    if h(s) == ∞ continue
    % assumes safe heuristic
    g = n.g + c(n.state, a)
    % first time encountered
    if get-color(s) == White
    set-color(s, Gray)
    set-distance(s, g)
    q.insert(n.make-node(s, a), g + h(s))

    % a shorter path was found
    else if g < get-distance(s)
        set-distance(s, g)
        if get-color(s) == Gray
        % re-order and re-link parent
        s.node.parent = n
        s.node.action = a
        s.node.g = g
        q.decrease-priority(s.node, g+h(s))
    else
        % node is black: re-open state!
        set-color(s, Gray)
        q.insert(n.make-node(s, a), g + h(s))
*/

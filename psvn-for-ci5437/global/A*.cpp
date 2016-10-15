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
#include "gap_heuristic.hpp"

#define  MAX_LINE_LENGTH 999

int main(int argc, char **argv) {

    // VARIABLES FOR INPUT
    char str[MAX_LINE_LENGTH + 1];
    ssize_t nchars;
    state_t state; // state_t is defined by the PSVN API. It is the type used for individual states.

    // VARIABLES FOR ITERATING THROUGH state's SUCCESSORS
    state_t child;
    ruleid_iterator_t iter; // ruleid_terator_t is the type defined by the PSVN API successor/predecessor iterators.
    int ruleid; // an iterator returns a number identifying a rule

    int d; //distance to a state

    PriorityQueue<state_t> open; // Priority Queue ordered by f-value: f (n) = g(n) + h(s)
    state_map_t *map = new_state_map(); // contains the cost-to-goal for all states that have been generated

    /*
    set-color(init(), Gray)
    set-distance(init(), 0)
    q.insert(make-root-node(init()), h(init()))
    */

    // READ A LINE OF INPUT FROM stdin
    printf("Please enter a state followed by ENTER: ");
    if( fgets(str, sizeof str, stdin) == NULL ) {
        printf("Error: empty input line.\n");
        return 0;
    }

    // CONVERT THE STRING TO A STATE
    nchars = read_state(str, &state);
    if( nchars <= 0 ) {
        printf("Error: invalid state entered.\n");
        return 0;
    }

    // initial state's cost
    d = gap_heuristic(&state);
    open.Add(d, d, state);

    // search
    while (!open.Empty()){
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

        // expand node look at all sucessors of the state
        init_fwd_iter(&iter, &state);  // initialize the child iterator
        while( (ruleid = next_ruleid(&iter)) >= 0 ) {
            apply_fwd_rule(ruleid, &state, &child);
            print_state(stdout, &child);

            // child's cost using the heuristic
            const int child_d = d + get_bwd_rule_cost(ruleid) + gap_heuristic(&child);

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

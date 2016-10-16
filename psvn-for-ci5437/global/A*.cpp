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
    FILE *file; // the final state_map is written to this file if it is provided (command line argument)

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
    int h0 = d;
    open.Add(d, d, state);
    state_map_add(map, &state, d);

    // search
    while (!open.Empty()){
        // get current distance from goal; since operator costs are
        // non-negative this distance is monotonically increasing
        d = open.CurrentPriority();

        // remove top state from priority state
        state = open.Top();
        open.Pop();

        if (is_goal(&state)) {
            // print the distance then the state
            printf("the cost of the path is: %d\n", d);
            break;
        }

        // check if we already expanded this state.
        // (entries on the open list are not deleted if a cheaper path to a state is found)
        const int *best_dist = state_map_get(map, &state);
        assert(best_dist != NULL);
        if( *best_dist < d ) continue;

        // print state
        printf("State: ");
        print_state(stdout, &state);
        printf("cost: %d\n", d);

        // expand node look at all sucessors of the state
        init_fwd_iter(&iter, &state);  // initialize the child iterator
        while( (ruleid = next_ruleid(&iter)) >= 0 ) {
            apply_fwd_rule(ruleid, &state, &child);

            // child's cost using the heuristic
            const int child_d = d + get_fwd_rule_cost(ruleid) + gap_heuristic(&child);

            // print state
            printf("State: ");
            print_state(stdout, &child);
            printf("costc: %d\n", child_d);

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
    // write the state map to a file
    if( argc >= 3 ) {
        file = fopen(argv[2], "w");
        if( file == NULL ) {
            fprintf(stderr, "could not open %s for writing\n", argv[2]);
            exit(-1);
        }
        char buffer[MAX_LINE_LENGTH] = "grupo, algorithm, heuristic, domain, instance, cost, h0, generated, time, gen_per_sec\n";
        fwrite (buffer , sizeof(char), sizeof(buffer), file);
        strcpy(buffer, "X, A*, gap, pancake28,");
        print_state(file, &state);
        memset(buffer, 0, MAX_LINE_LENGTH);
        sprintf(buffer, ", %d, %d, ", d, h0);
        fwrite (buffer , sizeof(char), sizeof(buffer), file);
        fclose(file);
    }
}

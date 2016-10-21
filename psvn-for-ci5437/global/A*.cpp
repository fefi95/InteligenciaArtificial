/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-...
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for A* algorithm
*/
#include <vector>
#include <time.h>
#include "priority_queue.hpp"
#include "heuristic.hpp"

#define  MAX_LINE_LENGTH 999

int main(int argc, char **argv) {

    // VARIABLES FOR INPUT
    ssize_t nchars;
    state_t state; // state_t is defined by the PSVN API. It is the type used for individual states.

    // VARIABLES FOR ITERATING THROUGH state's SUCCESSORS
    state_t child;
    ruleid_iterator_t iter; // ruleid_terator_t is the type defined by the PSVN API successor/predecessor iterators.
    int ruleid; // an iterator returns a number identifying a rule
    int history = init_history;

    int g = 0; //cost of path to a state

    PriorityQueue<state_t> open; // Priority Queue ordered by f-value: f (n) = g(n) + h(s)
    state_map_t *map = new_state_map(); // contains the cost-to-goal for all states that have been generated
    state_map_t *historyMap = new_state_map(); // contains the history of each node
    FILE *file; // the final state_map is written to this file if it is provided (command line argument)

    // READ A LINE OF INPUT FROM stdin
    // printf("Please enter a state followed by ENTER: ");
    if( argc < 3) {
        printf("USAGE:...\n");
        exit(-1);
    }

    // CONVERT THE STRING TO A STATE
    nchars = read_state(argv[2], &state);
    if( nchars <= 0 ) {
        printf("Error: invalid state entered.\n");
        exit(-1);
    }
    printf("Solving :");
    print_state(stdout, &state);
    printf("...\n");

    // variables needed for information in output file
    int generated = 1;
    clock_t clockStart;
    clock_t clockEnd;
    time_t timeStart;
    time_t timeEnd;
    double timeElapsed;

    // initial state's cost
    int h0 = heuristic(&state);
    open.Add(h0, h0, state);
    state_map_add(map, &state, g);
    state_map_add(historyMap, &state, history);

    /*******************************   file handling    ********************************/
    char problemName[30];
    char nameFile[30];
    int k = 2;

    //getting the name form the entry
    while (argv[0][k] != '.') {
        // printf("%c\n", argv[0][k]);
        problemName[k - 2] = argv[0][k];
        k++;
    }
    problemName[k - 2] = '\0';
    sprintf(nameFile, "%s_A*_result.csv", problemName); // argv[0]

    file = fopen(nameFile, "a");
    char buffer[MAX_LINE_LENGTH];

    if( file == NULL ) {
        fprintf(stderr, "could not open %s for writing\n", nameFile);
        exit(-1);
    }

    // write to file
    memset(buffer, 0, MAX_LINE_LENGTH);
    sprintf(buffer, "X, A*, %s, %s, \" ", argv[1], problemName);
    fwrite (buffer , sizeof(char), sizeof(buffer), file);
    print_state(file, &state);

    /**********************************   A* search   **********************************/
    clockStart = clock();
    timeStart = time(0);

    while (!open.Empty()){

        // remove top state from priority state
        state = open.Top();
        open.Pop();
        const int *state_g = state_map_get(map, &state);
        g = *state_g;
        const int *state_hist = state_map_get(historyMap, &state);
        history = *state_hist;

        if (is_goal(&state)) {
            // print the distance then the state
            printf("the cost of the path is: %d and h0 is: %d\n", g, h0);
            memset(buffer, 0, MAX_LINE_LENGTH);
            sprintf(buffer, "\", %d, ", g);
            fwrite (buffer , sizeof(char), sizeof(buffer), file);
            break;
        }

        // print state
        // printf("State: ");
        // print_state(stdout, &state);
        // printf("path's cost: %d\n", g);

        // break;
        // expand node
        init_fwd_iter(&iter, &state);  // initialize the child iterator
        while( (ruleid = next_ruleid(&iter)) >= 0 ) {
            // 300 seconds limit (5 min)
            timeEnd = time(0);
            timeElapsed = difftime(timeEnd, timeStart);
            if (timeElapsed > 300){
                printf("Time limit exceeded. Aborted...\n");
                strcpy(buffer, "na, na, na, na\n");
                fwrite (buffer , sizeof(char), sizeof(buffer), file);
                fclose(file);
                exit(-1);
            }

            if (fwd_rule_valid_for_history(history, ruleid) != 0){
                apply_fwd_rule(ruleid, &state, &child);
                int child_history = next_fwd_history(history, ruleid);

                // child's cost using the heuristic
                const int child_g = g + get_fwd_rule_cost(ruleid);
                const int child_f = child_g + heuristic(&child);

                // print state
                // printf("State: ");
                // print_state(stdout, &child);
                // printf("cost: %d\n", child_f);

                // check if either this child has not been seen yet or if
                // there is a new cheaper way to get to this child.
                const int *old_child_g = state_map_get(map, &child);
                if( (old_child_g == NULL) || (*old_child_g > child_g) ) {
                    // add to open with the new cost
                    state_map_add(map, &child, child_g);
                    state_map_add(historyMap, &child, child_history);
                    open.Add(child_f, child_f, child);
                }
                generated++;
            }
        }
    }
    
    clockEnd = clock();
    timeElapsed = double(clockEnd - clockStart) / CLOCKS_PER_SEC;
    memset(buffer, 0, MAX_LINE_LENGTH);
    sprintf(buffer, "%d, %d, %.7f, %.4f\n", h0, generated, timeElapsed, generated/timeElapsed);
    fwrite (buffer , sizeof(char), sizeof(buffer), file);
    fclose(file);
}

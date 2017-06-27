#include <iostream>
#include <utility>   // vector<>
#include <algorithm> // min, max
#include "struc.h"
#include <limits>

//#define _DEBUG

state_t state;
char *str;

static int64_t numNodos=0;
double inf = std::numeric_limits<double>::infinity();


void getintstate(){
    string line;
    ifstream initFile ("initstate");
    if(initFile.is_open()){

        getline(initFile,line);
        initFile.close();
    } else {
        cout << "No se pudo cargar el Archivo de estado inicial.\n";
    }
    str = const_cast<char*>(line.c_str());
}


std::pair<bool,unsigned> f_bounded_dfs(state_t s, unsigned bound,unsigned g){
    std::pair<bool,unsigned> p;

    //Variables
    ruleid_iterator_t iter;
    int ruleid;
    state_t child;
    //Caso base
    const unsigned f = g + H(s);

#ifdef _DEBUG
    //printf("s|e ->");
    //print_state(stdout,(state_t *) &s);
    //printf("<- f=%d g=%d boun=%d\n",f,g,bound);
#endif // _DEBUG


    if (f > bound){
        p.first = false;
        p.second = f;
        return p;
    }

    if(is_goal(&s)){
        printf("<<<<GOAL>>>>\n");
        print_state(stdout,(state_t *) &s);
        printf("\n");
        p.first = true;
        p.second = g;
        return p;
    }
    //***********************************************
    int t = 10000; //  t = inf

    init_fwd_iter(&iter, &s);
    while( (ruleid = next_ruleid(&iter)) >= 0 ) {
        apply_fwd_rule(ruleid, &s, &child);

        g = g + get_fwd_rule_cost(ruleid);
        p = f_bounded_dfs(child, bound, g);
        ++numNodos;

        if(p.first) return p;

        t = Min(t, p.second);
        p.second = t;

#ifdef _DEBUG
        printf("f=%d g=%d boun=%d: ",f,g,bound);
        print_state(stdout, &child);
        printf("[t=%d]  %s (cost %d), goal=%d\n",t, get_fwd_rule_label(ruleid), get_fwd_rule_cost(ruleid), is_goal(&child));
#endif // _DEBUG

    }
    p.first = false;
    p.second = t;
    return p;
}


int main (int argc, char **argv){
    //Variables
    std::pair<bool, unsigned> p;
    int nchars,d, bound ;
    state_t state;

    getintstate(); // Se carga el estado inicial

    //
    char abst_fname[] = "hanoi4p03d.igual.abst";
    printf("Cargando pdb en memoria: abst=%s\n", abst_fname);
    abstraction_t *abst = read_abstraction_from_file(abst_fname);

    print_abstraction(abst);
    printf("\n");

    nchars = read_state(str, &state);
    if( nchars <= 0 ) {
        printf("Error: Estado invalido introducido.\n");
        return 0;
    }

    int g=0;

    //compute PDB value for state
    state_t abst_state;
    abstract_state(abst, &state, &abst_state);

    bound = H(state);


#ifdef _DEBUG
    printf("H(init())=%d  g=%d |",bound,g);
    print_state(stdout, &(state));
    printf("| [%d  ", g);
    //print_state(stdout, &abst_state);
    printf("]\n");
#endif // _DEBUG


    for(int i=0;i<=0;++i){
        numNodos=0;
        p = f_bounded_dfs(state, bound, g);
        printf("(i=%d) | numNodos=%i\n",i,(int)numNodos);
        bound = p.second;
        if(p.first){
            break;
        }
    }

}

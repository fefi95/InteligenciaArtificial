CC = gcc
CXX = g++
OPT = -g -Wall -O3 -Wno-unused-function -Wno-unused-variable
PSVNOPT = --state_map --no_abstraction --backwards_moves --history_len=1

heuristic.hpp:
	cp ./manhattan_heuristic.hpp ../../global/heuristic.hpp

psvn2c_core.c:
	cp ../../src/psvn2c_core.c ./psvn2c_core.c

psvn2c_state_map.c:
	cp ../../src/psvn2c_state_map.c ./psvn2c_state_map.c

psvn2c_abstraction.c:
	cp ../../src/psvn2c_abstraction.c ./psvn2c_abstraction.c

%.c: %.psvn psvn2c_core.c psvn2c_state_map.c psvn2c_abstraction.c
	../../bin/psvn2c $(PSVNOPT) --name=$(*F) < $< > $@
	rm -f ./psvn2c_core.c ./psvn2c_state_map.c ./psvn2c_abstraction.c

.PRECIOUS: %.c

%.succ: %.c ../../global/succ.c
	$(CC) $(OPT) ../../global/succ.c -include $< -o $@
	rm -f $*.c

%.dist: %.c ../../global/dist.cpp
	$(CXX) $(OPT) ../../global/dist.cpp -include $< -o $@
	rm -f $*.c

%.distSummary: %.c ../../global/distSummary.cpp
	$(CXX) $(OPT) ../../global/distSummary.cpp -include $< -o $@
	rm -f $*.c

%.IDDFS2: %.c ../../global/IDDFS2.cpp
	$(CXX) $(OPT) ../../global/IDDFS2.cpp -include $< -o $@
	rm -f $*.c

%.A*: %.c heuristic.hpp ../../global/A*.cpp
	$(CXX) $(OPT) ../../global/A*.cpp -include $< -o $@
	rm -f $*.c ../../global/heuristic.hpp

abstractor:
	$(CXX) $(OPT) ../../src/abstractor.cpp ../../src/psvn.cpp -o $@

%.pdb: abstractor
	@rm -f `basename $*`.abst `basename $*`.pdb `basename $*`.psvn
	./abstractor `dirname $*`.psvn `basename $*` < `basename $*`.txt
	make `basename $*`.distSummary
	echo Calculating `basename $*.pdb` ...
	@./`basename $*`.distSummary `basename $*`.pdb

%.dist_pdb: %.c ../../global/dist_pdb.cpp
	$(CXX) $(OPT) ../../global/dist_pdb.cpp -include $< -o $@
	rm -f $*.c

.PHONY: clean
clean:
	rm -fr *.succ *.dist *.distSummary *.A* *.dist_pdb psvn2c_core.c psvn2c_state_map.c psvn2c_abstraction.c abstractor *.dSYM *.o *~

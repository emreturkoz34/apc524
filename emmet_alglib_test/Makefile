ALGLIB	= alglibinternal alglibmisc ap dataanalysis diffequations fasttransforms integration interpolation linalg optimization solvers specialfunctions statistics
TEST	= test

OBJ	= $(addsuffix .o,$(ALGLIB)) $(addsuffix .o,$(TEST))
TARGETS	= test

all:	$(OBJ) $(TARGETS)

$(addsuffix .o,%): $(addsuffix .cpp,%)
	g++ -c $^ -o $@

$(addsuffix .o,$(TEST)): $(addsuffix .cc,$(TEST))
	g++ -c $^ -o $@

test: $(OBJ)
	g++ $^ -o $@

clean:
	rm -f *.o

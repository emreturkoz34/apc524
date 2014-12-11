CXX	= g++ -I/home/pismire/ndarray/include
CXXFLAG	= -g -Wall -Wextra -pedantic -O3
INCLUDE	= -I/home/pismire/ndarray/include
targets	= test

all: $(targets)

test : test.o
	$(CXX) -o $(INCLUDE) $@ $^

clean:
	$(RM) *.o
	$(RM) .depend

depend:
	$(CXX) $(INCLUDE) -MM $(CXXFLAGS) *.cc > .depend

-include .depend

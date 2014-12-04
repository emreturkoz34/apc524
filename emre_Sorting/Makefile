CXXFLAGS = -Wall -O3 -g

TARGETS = brute_sort

all: $(TARGETS)

brute_sort: sort_test.o brute_sort.o matrix.o
	$(CXX) -o $@ $^

clean:
	$(RM) *.o
	$(RM) .depend

depend: 
	$(CXX) -MM $(CXXFLAGS) *.cc > .depend

-include .depend
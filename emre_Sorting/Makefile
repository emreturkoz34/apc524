CXXFLAGS = -Wall -O3 -g

TARGETS = brute_sort standard_sort quick_sort bubble_sort

all: $(TARGETS)

brute_sort: sort_test.o brute_sort.o matrix.o
	$(CXX) -o $@ $^

standard_sort: sort_test.o standard_sort.o matrix.o
	$(CXX) -o $@ $^

quick_sort: sort_test.o quick_sort.o matrix.o
	$(CXX) -o $@ $^

bubble_sort: sort_test.o bubble_sort.o matrix.o
	$(CXX) -o $@ $^

clean:
	$(RM) *.o
	$(RM) .depend

depend: 
	$(CXX) -MM $(CXXFLAGS) *.cc > .depend

-include .depend
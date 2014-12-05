monoObjects = monocheck_tester.o monocheck.o matrix.o linregression.o

CXXFLAGS = -g -O3 -Wall -lm

all: check_monotonic

check_monotonic : $(monoObjects)
	$(CXX) -o $@ $^

clean:
	$(RM) *.o
	$(RM) .depend

depend:
	$(CXX) -MM $(CXXFLAGS) *.cc > .depend

-include .depend

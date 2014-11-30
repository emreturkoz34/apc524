CXX	= g++
CXXFLAG	= -g -Wall -Wextra -pedantic
objects	= deltaPDF.o betaPDF.o convolute.o trapz.o simpson.o convolute_tester.o


all: convolute_tester

convolute_tester : $(objects)
	$(CXX) -o $@ $^

clean:
	$(RM) *.o
	$(RM) .depend

depend:
	$(CXX) -MM $(CXXFLAGS) *.cc > .depend

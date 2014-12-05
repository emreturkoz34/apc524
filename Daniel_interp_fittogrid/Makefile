interpolators = lininterp.o
matrices = matrix.o
matrices_all = matrix.o matrix3d.o matrix4d.o
objects1 = interp_tester.o $(interpolators) $(matrices)
objects2 = fittogrid_tester.o $(interpolators) $(matrices_all) fittogrid.o

CXXFLAGS = -g -Wall -O3

all: interp_tester fittogrid_tester

interp_tester : $(objects1)
	$(CXX) -o $@ $^

fittogrid_tester : $(objects2)
	$(CXX) -o $@ $^

clean:
	$(RM) *.o
	$(RM) .depend

depend:
	$(CXX) -MM $(CXXFLAGS) *.cc > .depend

-include .depend

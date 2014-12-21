MATRIX	= vector matrix matrix3d matrix4d
INTERP = lininterp
TARGET     = $(MATRIX) $(INTERP) helper deltaPDF betaPDF trapz convolute bubble_sort monocheck linregression endpointslope fittogrid
CXX        = g++
CXXFLAGS     = -O3 -fPIC
PYLIB	   = -I/usr/include/python2.7


.PHONY	: all clean

all	: $(addsuffix .o,$(TARGET)) $(addsuffix _wrap.cxx,$(TARGET)) $(addsuffix _wrap.o,$(TARGET)) $(patsubst %,_%.so,$(TARGET))

%_wrap.cxx: %.i
	swig -c++ -python $^

%.o: %.cc
	$(CXX) $(CXXFLAGS) $^ -c

%_wrap.o: %_wrap.cxx
	$(CXX) $(CXXFLAGS) -c $^ $(PYLIB)

_%.so: %_wrap.o %.o $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

clean:
	rm -f *.o *_wrap.cxx $(addsuffix .py,$(TARGET)) *.pyc

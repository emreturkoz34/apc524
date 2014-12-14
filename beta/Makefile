MATRIX	= vector matrix matrix3d matrix4d
INTERP = lininterp
TARGET     = $(MATRIX) $(INTERP) helper deltaPDF betaPDF trapz convolute bubble_sort monocheck linregression endpointslope
TARGETSO	= $(addprefix _,$(TARGET))
TARGETWRAP	= $(addsuffix _wrap,$(TARGET))
MATRIXOBJ  = vector.o matrix.o matrix3d.o matrix4d.o
CXX        = g++
CXXFLAGS     = -O3 -fPIC
PYLIB	   = -I/usr/include/python2.7


.PHONY	: all clean
all	: $(addsuffix .o,$(TARGET)) $(addsuffix _wrap.cxx,$(TARGET)) $(addsuffix .o,$(TARGETWRAP)) $(addsuffix .so,$(TARGETSO))

%_wrap.cxx: %.i
	swig -c++ -python $^

%.o: %.cc
	$(CXX) $(CXXFLAGS) $^ -c

%_wrap.o: %_wrap.cxx
	$(CXX) $(CXXFLAGS) -c $^ $(PYLIB)

_%.so: %_wrap.o %.o $(MATRIXOBJ)
	$(CXX) -shared $^ -o $@

clean:
	rm -f *.o *_wrap.cxx $(addsuffix .py,$(TARGET)) *pyc

MATRIX	= vector matrix matrix3d
TARGET     = $(MATRIX) helper deltaPDF betaPDF trapz convolute
TARGETSO	= $(addprefix _,$(TARGET))
TARGETWRAP	= $(addsuffix _wrap,$(TARGET))
MATRIXOBJ  = vector.o matrix.o matrix3d.o
CXX        = g++
CXXFLAGS     = -O3 -fPIC
PYLIB	   = -I/usr/include/python2.7

all	: $(addsuffix .o,$(TARGET)) $(addsuffix .py,$(TARGET)) $(addsuffix .o,$(TARGETWRAP)) $(addsuffix .so,$(TARGETSO))

_%.so: %_wrap.o %.o $(MATRIXOBJ)
	$(CXX) -shared $(addsuffix .o,$(TARGET)) $(addsuffix _wrap.o,$(TARGET)) -o $@

%_wrap.o: %_wrap.cxx
	$(CXX) $(CXXFLAGS) -c $^ $(PYLIB)

%.py: %.i
	swig -c++ -python $^

%.o: %.cc
	$(CXX) $(CXXFLAGS) $^ -c



clean:
	rm -f *o *_wrap.cxx *.so $(addsuffix .py,$(TARGET)) *pyc

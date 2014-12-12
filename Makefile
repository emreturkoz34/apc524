TARGET     = helper deltaPDF
WRAPPER	   = $(TARGET)_wrap.cxx
SRC	   = $(TARGET).cc 
MATRIXOBJ  = vector.o matrix.o matrix3d.o
OBJ	   = $(SRC:.cc=.o) $(WRAPPER:.cxx=o) $(MATRIXOBJ) 
CXX        = g++
CXXFLAGS     = -O3 -fPIC
INTERFACE  = $(TARGET).i
SWIGOPT    =
SWIG       = swig
PYLIB	   = -I/usr/include/python2.7

SO	   = so

all	: helper.o deltaPDF.o deltaPDF.py helper.py helper_wrap.o deltaPDF_wrap.o _helper.so _deltaPDF.so


%.o: %.cc
	$(CXX) $(CXXFLAGS) $^ -c

%.py: %.i
	swig -c++ -python $^

%_wrap.o: %_wrap.cxx
	$(CXX) $(CXXFLAGS) -c $^ $(PYLIB)

_%.so: %_wrap.o %.o $(MATRIXOBJ)
	$(CXX) -shared $(OBJ) -o $^
#python_clean:
#	rm -f *_wrap* *.o *~ *$(SO) mypython *.pyc .~* core

depend:
	$(CXX) -MM $(CXXFLAGS) *.cc > .depend

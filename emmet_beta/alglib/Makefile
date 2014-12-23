include ../Makefile.in
#CXX		= g++
#CXXFLAGS	= -O3 -fPIC
#PYLIB		= -I/usr/include/python2.7


ALGOBJ	= $(addsuffix .o,$(ALGLIB))

all: $(ALGOBJ)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@

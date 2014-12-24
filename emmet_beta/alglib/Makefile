include ../Makefile.in

ALGOBJ	= $(addsuffix .o,$(ALGLIB))

all: $(ALGOBJ)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@

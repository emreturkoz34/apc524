include ../Makefile.in
vpath %.cc ../src
vpath %.cxx ../src

# SWIG Interface files
SWIGINT	= $(addsuffix _wrap.cxx,$(ABSCLS)) \
	$(addsuffix _wrap.cxx,$(OTHER)) \
	$(addsuffix _wrap.cxx,$(MATRIX))

# All objects
OBJ	= $(addsuffix .o,$(SRC)) $(SWIGINT:.cxx=.o)

all: $(SWIGINT) $(OBJ)

%_wrap.o: %_wrap.cxx $(addsuffix: .o,$(PDFS))
	$(CXX) $(CXXFLAGS) -c $^ $(PYLIB) -o $@

%.o: %.cc
	$(CXX) $(CXXFLAGS) -c $^ -o $@


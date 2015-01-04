include ../Makefile.in

vpath %.o ../obj

TARGET	= $(patsubst %,_%.so,$(SO))

all: $(TARGET)

# Matrix/Other shared objects
_%.so: %_wrap.o %.o $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

# MaxSlope shared object
_maxslope.so: maxslope_wrap.o $(addsuffix .o,$(MAXSLOPE)) $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

# LeastNonMono shared object
_leastnonmono.so: leastnonmono_wrap.o $(addsuffix .o,$(LNM)) $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

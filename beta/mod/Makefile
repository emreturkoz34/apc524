include ../Makefile.in

vpath %.o ../obj
vpath %.o ../alglib

TARGET	= $(patsubst %,_%.so,$(SO))

all: $(TARGET)

# Matrix/Other shared objects
_%.so: %_wrap.o %.o $(addsuffix .o,$(MATRIX))
	$(CXX) -fopenmp -shared $^ -o $@

# Fittogrid shared objects
_fittogrid.so: fittogrid_wrap.o fittogrid.o $(addsuffix .o,$(SORT)) $(addsuffix .o,$(MATRIX))
	$(CXX) -fopenmp -shared $^ -o $@

# MaxSlope shared object
_maxslope.so: maxslope_wrap.o $(addsuffix .o,$(SLOPE)) $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

# NonMono shared object
_leastnonmono.so: leastnonmono_wrap.o $(addsuffix .o,$(NONMONO)) $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

# Interpolator shared object
_interpolator.so: interpolator_wrap.o $(addsuffix .o,$(INTRP)) \
	$(addsuffix .o,$(MATRIX)) $(addsuffix .o,$(ALGLIB))
	$(CXX) -shared $^ -o $@

# PDF shared object
_pdf.so: pdf_wrap.o $(addsuffix .o,$(PDFS)) $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

# Sort shared object
_sorting.so: sorting_wrap.o $(addsuffix .o,$(SORT)) $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

# Integrator shared object
_integrator.so: integrator_wrap.o $(addsuffix .o,$(INTGR)) \
	$(addsuffix .o,$(MATRIX)) $(addsuffix .o,$(ALGLIB))
	$(CXX) -shared $^ -o $@

include ../Makefile.in

vpath %.o ../obj
vpath %.o ../alglib

TARGET	= $(patsubst %,_%.so,$(SO))

all: $(TARGET)

# Matrix/Other shared objects
_%.so: %_wrap.o %.o $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

# PDF shared object
_pdf.so: pdf_wrap.o $(addsuffix .o,$(PDFS)) $(addsuffix .o,$(MATRIX))
	$(CXX) -shared $^ -o $@

# Integrator shared object
_integrator.so: integrator_wrap.o $(addsuffix .o,$(INTGR)) \
	$(addsuffix .o,$(MATRIX)) $(addsuffix .o,$(ALGLIB))
	$(CXX) -shared $^ -o $@

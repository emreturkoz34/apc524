include ../Makefile.in

# SWIG Interface files
SWIGINT	= $(addsuffix _wrap.cxx,$(ABSCLS)) \
	$(addsuffix _wrap.cxx,$(OTHER)) \
	$(addsuffix _wrap.cxx,$(MATRIX))

all: $(SWIGINT)

%_wrap.cxx: %.i
	swig -c++ -python $^



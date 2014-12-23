include ../Makefile.in

# SWIG Interface files
SWIGINT	= $(addsuffix _wrap.cxx,$(ABSCLS)) \
	$(addsuffix _wrap.cxx,$(CLASS))\
	$(addsuffix _wrap.cxx,$(OTHER))


all: $(SWIGINT)

%_wrap.cxx: %.i
	swig -c++ -python $^

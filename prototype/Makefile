CXX	= g++
CXXFLAG	= -g -Wall -Wextra -pedantic -O3
pdfs	= deltaPDF.o betaPDF.o
intgr	= trapz.o simpson.o convolute.o
matrix	= matrix.o matrix3d.o matrix4d.o
interp 	= lininterp.o
sort	= brute_sort.o
mono	 = monocheck.o linregression.o
interpObj = interp_tester.o $(interp) $(matrix)
fitObj = fittogrid_tester.o $(interp) $(matrix) fittogrid.o
pdfObj = pdf_convolute_test.o $(pdfs) $(intgr) $(matrix)
sortObj = sort_test.o $(sort) $(matrix)
monoObj = monocheck_tester.o $(mono) $(matrix)
targets	= interp_tester fittogrid_tester pdf_convolute_test brute_sort check_monotonic

all: $(targets)

interp_tester : $(interpObj)
	$(CXX) -o $@ $^

fittogrid_tester : $(fitObj)
	$(CXX) -o $@ $^

pdf_convolute_test : $(pdfObj)
	$(CXX) -o $@ $^

brute_sort: $(sortObj)
	$(CXX) -o $@ $^

check_monotonic : $(monoObj)
	$(CXX) -o $@ $^


clean:
	$(RM) *.o
	$(RM) .depend

depend:
	$(CXX) -MM $(CXXFLAGS) *.cc > .depend

-include .depend

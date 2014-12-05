CXX	= g++
CXXFLAG	= -g -Wall -Wextra -pedantic
pdfs	= deltaPDF.o betaPDF.o
intgr	= trapz.o simpson.o convolute.o
matrix	= matrix.o matrix3d.o matrix4d.o
object	= pdf_convolute_test.o

all: pdf_convolute_test

pdf_convolute_test : $(pdfs) $(intgr) $(matrix) $(object)
	$(CXX) -o $@ $^

clean:
	$(RM) *.o
	$(RM) .depend

depend:
	$(CXX) -MM $(CXXFLAGS) *.cc > .depend

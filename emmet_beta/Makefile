include Makefile.in

all: Makefile Makefile.in
	cd $(ALGDIR); make
	cd $(SRCDIR); make
	cd $(OBJDIR); make
	cd $(MODDIR); make
	cp $(SRCDIR)/*.py $(MODDIR)

cleanall: clean cleanlib

clean:
	rm -f $(SRCDIR)/*.cxx $(SRCDIR)/*.py
	rm -f $(OBJDIR)/*.o
	rm -f $(MODDIR)/*.so $(MODDIR)/*.py $(MODDIR)/*.pyc

cleanlib:
	rm -f $(ALGDIR)/*.o



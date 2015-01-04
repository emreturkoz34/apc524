include Makefile.in

all: Makefile Makefile.in
	$(MAKE) -C $(ALGDIR)
	$(MAKE) -C $(SRCDIR)
	$(MAKE) -C $(OBJDIR)
	$(MAKE) -C $(MODDIR)
	cp $(SRCDIR)/*.py $(MODDIR)

cleanall: clean cleanlib

clean:
	rm -f $(SRCDIR)/*.cxx $(SRCDIR)/*.py
	rm -f $(OBJDIR)/*.o
	rm -f $(MODDIR)/*.so $(MODDIR)/*.py $(MODDIR)/*.pyc
	rm -f $(PYDIR)/*.pyc 

cleanlib:
	rm -f $(ALGDIR)/*.o

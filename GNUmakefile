# =======================================================================================
#  Makefile for hydrodynamic causality checks     Christopher Plumberg, September 8, 2015
# =======================================================================================
##
##  Environments :	MAIN	= 	main sourcefile	
##
##  Usage : 	(g)make	[all]		compile the whole project		
##			install	make all and copy binary to $INSTPATH
##			distclean	remove all binaries
##  

# Set compiler and flags
CC := g++
CFLAGS= -std=c++11 -lgsl -lgslcblas -lm

# Various directories and definitions
RM          =   rm -f
O           =   .o
LDFLAGS     =   -L/usr/local/src/gsl/2.5/lib
INCFLAGS    =   -I/usr/local/src/gsl/2.5/include
SYSTEMFILES =   $(SRCGNU)


# --------------- Files involved ------------------

ifeq "$(MAIN)" ""
MAIN		=	check_causality
endif
ifeq "$(MAIN2)" ""
MAIN2		=	check_causality_3_plus_1D
endif

MAINSRC     =   check_causality.cpp
MAIN2SRC    =   check_causality_3_plus_1D.cpp

INC		= 	necessary_conditions.h sufficient_conditions.h

# -------------------------------------------------

TARGET		=	$(MAIN)
TARGET2		=	$(MAIN2)
INSTPATH	=	..

# --------------- Pattern rules -------------------

$(TARGET):
	$(CC) $(MAINSRC) -o $(TARGET) $(CFLAGS) $(INCFLAGS)  $(LDFLAGS)

$(TARGET2):
	$(CC) $(MAIN2SRC) -o $(TARGET2) $(CFLAGS) $(INCFLAGS)  $(LDFLAGS)

# -------------------------------------------------

.PHONY:		all distclean distclean install

all:		$(TARGET) $(TARGET2)

help:
		@grep '^##' GNUmakefile

distclean:	
		-rm $(TARGET) $(TARGET2)

install:	$(TARGET) $(TARGET2)
		cp $(TARGET) $(INSTPATH)
		cp $(TARGET2) $(INSTPATH)

# --------------- Dependencies -------------------
check_causality.cpp:             necessary_conditions.h sufficient_conditions.h
check_causality_3_plus_1D.cpp:   necessary_conditions.h sufficient_conditions.h

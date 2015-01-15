%module sorting
%{
#define SWIF_FILE_WITH_INIT
#include "sorting.h"
#include "bubblesort.h"
#include "standardsort.h"
#include "brutesort.h"
%}

%include "sorting.h"
%include "bubblesort.h"
%include "standardsort.h"
%include "brutesort.h"

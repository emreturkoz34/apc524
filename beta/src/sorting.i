%module sorting
%{
#define SWIF_FILE_WITH_INIT
#include "sorting.h"
#include "bubble_sort.h"
#include "standard_sort.h"
#include "brute_sort.h"
%}

%include "sorting.h"
%include "bubble_sort.h"
%include "standard_sort.h"
%include "brute_sort.h"

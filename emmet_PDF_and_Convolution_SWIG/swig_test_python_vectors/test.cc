#include "test.h"

void print_line(std::vector< double > myline)
{
  for (int i = 0; i < 10; i++) 
    printf("[%d] = [%f]\n", i, myline[i]);
}


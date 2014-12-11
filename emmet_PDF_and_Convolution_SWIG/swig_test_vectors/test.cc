#include "test.h"

void print_array(std::vector< std::vector < double > > myarray)
{
  for (int i=0; i<2; i++)
    for (int j=0; j<2; j++)
      printf("[%d][%d] = [%f]\n", i, j, myarray[i][j]);
}

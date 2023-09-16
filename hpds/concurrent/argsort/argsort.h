#include <parallel/algorithm>

void argsort(unsigned long *pidx, const double *parr, unsigned long length)
{
    unsigned long *pidx2 = pidx + length;
    __gnu_parallel::sort(pidx, pidx2,[parr](size_t i1, size_t i2)
    {return *(parr + i1) < *(parr + i2);});
}
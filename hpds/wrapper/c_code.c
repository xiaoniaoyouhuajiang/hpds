/* Small C file creating an array to demo C -> Python data passing 
 * 
 * Author: Gael Varoquaux
 * License: BSD 3 clause
 */

#include <stdlib.h>

float *compute(int size)
{
    int* array;
    array = malloc(sizeof(int)*size);
    int i;
    for (i=0; i<size; i++)
    {
	array[i] = i;
    }
    return array;
}
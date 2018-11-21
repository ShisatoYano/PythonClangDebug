#ifndef __CLANG_SAMPLE_H__
#define __CLANG_SAMPLE_H__

#include <stdio.h>

typedef struct{
    int a;
    int b;
}Pair;

extern Pair make_pair(int a, int b);

extern int add(int c, int d);

#endif // __CLANG_SAMPLE_H__
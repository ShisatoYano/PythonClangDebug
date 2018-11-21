#include "ClangSample.h"

int main(void)
{
    printf("%d + %d = %d\n", 3, 4, add(3, 4));
    return 0;
}

int add(int c, int d)
{
    return c + d;
}

Pair make_pair(int a, int b)
{
    Pair p;

    p.a = a;
    p.b = b;

    return p;
}
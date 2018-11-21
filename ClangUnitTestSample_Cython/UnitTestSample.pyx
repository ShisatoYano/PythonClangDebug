# -*- coding: utf-8 -*-
"""
Cython code for using function in Clang.
These functions can be called by Python.
Last update: 2018/11/18
"""

# define function from Clang header file
cdef extern from "ClangSample.h":
    ctypedef struct Pair:
        int a
        int b
    
    Pair make_pair(int a, int b)
    
    int add(int c, int d)

# define function executed by Python
def py_add(c, d):
    return add(c, d)

def py_make_pair(a, b):
   return make_pair(a, b)
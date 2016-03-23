#!/usr/bin/env python
# -*- coding: utf-8 -*-

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    s = bar('1')
    print s

main()
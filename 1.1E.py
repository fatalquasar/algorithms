#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/06/2017 21:48

#(欧几里得算法) 给定两个正整数m和n，求他们的最大公因数，即同时整除m和n的最大正整数。
#E1. 【求余数】用n除m，令r为余数。（我们将有0<=r<n）
#E2. 【余数为0？】如果r=0，算法终止。n为答案。
#E3. 【减少】置m<-n,n<-r,然后返回步骤E1


def greatest_common_factor(n, m):
    if m % n == 0:
        return n
    else:
        return greatest_common_factor(m % n, n)

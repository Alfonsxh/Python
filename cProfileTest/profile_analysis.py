#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#=============================================================================
# FileName: profile_analysis.py
# Desc:
# Author: chenhui.shang
# Email: chenhui.shang@woqutech.com
# HomePage: www.woqutech.com
# Version: 0.0.1
# LastChange:  2020/4/11 15:33
# History:
#=============================================================================
"""
import pstats


def analysis(prof_file):
    p = pstats.Stats(prof_file)
    p.strip_dirs().sort_stats("cumtime").print_stats(20)


if __name__ == '__main__':
    analysis(prof_file="./qbo_2.prof")

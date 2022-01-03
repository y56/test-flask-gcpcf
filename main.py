#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:39:11 2021

@author: y56
"""

from flask import abort

def main(request):
    path = request.path

    if path == "/test":
        return "test page"
    elif path == "/home" or path == "/":
        return "ḧome page"
    else:
        abort(404)


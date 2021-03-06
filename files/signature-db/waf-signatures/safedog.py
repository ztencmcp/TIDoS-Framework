#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID (Modified version from wascan)
#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework

from re import search,I

def safedog(headers,content):
    detect = False
    for header in headers.items():
        detect |= search(r'safedog',header[1],I) is not None
        detect |= search(r'waf/2\.0',header[1],I) is not None
        if detect:break
    if detect :
        return "Safedog Web Application Firewall (Safedog)"

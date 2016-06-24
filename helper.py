#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" uploader helper for KindleEar
It will modify AppId and some other items for you automatically.
Configure file 'custom.txt' format (encoding of the file must be ascii):
application: YourAppId
email: YourEmail
timezone: 8
If it not exist, this script will create it in same directory of __file__.
"""
import os, re, codecs, locale
__Author__ = 'cdhigh'
__Version__ = '1.3.1'
__Date__ = '2015-08-20'

CUSTOM_FILE = 'custom.txt'
KE_DIR = 'KindleEar'
KE_MASTER_DIR = 'KindleEar-master'
PAT_APP = r"^application:\s*([\w\-]+)"
PAT_EMAIL = r"^SRC_EMAIL\s*=\s*[\"\']([\w@\.\-]+)[\"\'](.*)"
PAT_DOMAIN = r"^DOMAIN\s*=\s*[\"\']([\w:/\.\-]+)[\"\'](.*)"
PAT_TZ = r"^TIMEZONE\s*=\s*?(-{0,1}\d+)(.*)"


#(re)move chinese books to a subdirectory (donot display in webpage) 
def RemoveChineseBooks(ke_dir):
    lang = 'zh_CN'
    cn_books = []
    loc = locale.getdefaultlocale()
    if loc and len(loc) > 1:
        lang = loc[0]
    if lang.startswith('zh'):
        return

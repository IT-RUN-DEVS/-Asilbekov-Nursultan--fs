import os
import os.path
import shutil
from pathlib import Path
from commands import*
import sys
if sys.argv[1]=='create':
        if len(sys.argv)==2:
                print('Введите название файла')
        elif len(sys.argv)==3:
                create(sys.argv[2])
        elif len(sys.argv)==4:
                create(sys.argv[2],sys.argv[3])
if sys.argv[1]=='copy':
        if len(sys.argv)==2:
                print('Введите название файла')
        elif len(sys.argv)==3:
                copy(sys.argv[2])
        elif len(sys.argv)==4:
                copy(sys.argv[2],sys.argv[3])
if sys.argv[1]=='init':
        if len(sys.argv)==2:
                print('Введите название папки')
        elif len(sys.argv)==3:
                init(sys.argv[2])
        elif len(sys.argv)==4:
                init(sys.argv[2],sys.argv[3])
if sys.argv[1]=='list_':
        if len(sys.argv)==2:
                list_()
        elif len(sys.argv)==3:
                list(sys.argv[2])
if sys.argv[1]=='move':
        if len(sys.argv)==2:
                print('Введите название папки')
        elif len(sys.argv)==3:
                print('Введите название директории')
        elif len(sys.argv)==4:
                move(sys.argv[2],sys.argv[3])
if sys.argv[1]=='backup':
        if len(sys.argv)==2:
                backup()
        elif len(sys.argv)==3:
                backup(sys.argv[2])
if sys.argv[1]=='snapshot':
        if len(sys.argv)==2:
                snapshot()
        elif len(sys.argv)==3:
                snapshot(sys.argv[2])



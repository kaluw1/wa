# -*- coding: utf-8 -*-
"""
Authors: Gonzalo Espinoza
         UNESCO-IHE 2016
Contact: g.espinoza@unesco-ihe.org
Repository: https://github.com/wateraccounting/wa
Module: Sheets

Description:
This can be used to create the WA+ standard sheets (www.wateraccounting.org).

Examples:
from wa.Sheets import *
create_sheet1(basin='Incomati', period='2005-2010', units='km3/year',
              data=r'C:\Sheets\csv\Sample_sheet1.csv',
              output=r'C:\Sheets\sheet_1.jpg')
create_sheet2(basin='Nile Basin', period='2010', units='km3/year',
              data=r'C:\Sheets\csv\Sample_sheet2.csv',
              output=r'C:\Sheets\sheet_2.jpg')
create_sheet7(basin='Sample data', period='2006-2016', units='Mm3/yr',
              data=r'C:\Sheets\csv\Sample_sheet7.csv',
              output=r'C:\Sheets\sheet_7.jpg')
"""


from .sheet1 import create_sheet1
from .sheet2 import create_sheet2
from .sheet7 import create_sheet7

__all__ = ['create_sheet1', 'create_sheet2', 'create_sheet7']

__version__ = '0.1'

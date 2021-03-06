# -*- coding: utf-8 -*-
"""
Authors: Tim Hessels and Gonzalo Espinoza
         UNESCO-IHE 2016
Contact: t.hessels@unesco-ihe.org
         g.espinoza@unesco-ihe.org
Repository: https://github.com/wateraccounting/wa
Module: Collect/DEM


Description:
This module downloads DEM data from http://earlywarning.usgs.gov/hydrodata/.
Use the DEM functions to download and create DEM images in Gtiff format.

Examples:
from wa.Collect import DEM
DEM.HydroSHED(Dir='C:/TempDEM/', latlim=[-10, 30], lonlim=[-20, 120], Resample=0)
"""

from .HydroSHED import main as HydroSHED

__all__ = ['HydroSHED']

__version__ = '0.1'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math 
import numpy
import matplotlib.pyplot as mpp # связываемся с данными библиотеками

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #файл запускается как основная программа
    arguments = numpy.r_[0:200:0.1] # присваиваем аргументу значение из библиотеки
    mpp.plot( # запуск графиков с помощью библиотеки
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] # присваиваем значения аргументам из библиотек
    )
    mpp.show()
    
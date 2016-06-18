#!/usr/bin/env python
#! -*- coding: utf-8 -*-

from distutils.core import setup

setup(
	name='sistema-canaima',
	version='0.1',
	description='sistema para el registro y control de los equipos canaima',
	url='https://github.com/laar19/sistema-canaima',
	packages=['conexiondb',],
	license='MIT',
	long_description=open('README').read(),
)

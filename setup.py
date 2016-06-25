#!/usr/bin/env python
#! -*- coding: utf-8 -*-

# Copyright (C) 2016 Luis Acevedo
#
# This file is part of registro-canaima.
#
# registro-canaima is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# registro-canaima is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(
	name='registro-canaima',
	version='0.1',
	description='sistema para el registro y control de los equipos canaima',
	url='https://github.com/laar19/registro-canaima',
	packages=['conexiondb',],
	license='GPL-3',
	long_description=open('README').read(),
)

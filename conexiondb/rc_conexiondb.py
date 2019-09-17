#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import getpass

#librería de conexión con la base de datos
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#librería de errores de la base de datos
from psycopg2 import IntegrityError, DatabaseError, DataError, InternalError, Error, OperationalError, connect

################################################## begin conexion base de datos ##################################################
global con, cur
#abrir conexion con la base de datos
def conexion_open(var):
	try:
		#conexión con la base de datos
		con = psycopg2.connect(var)
		cur = con.cursor()

	except OperationalError as e:
		pass
	finally:
		try:
			return con, cur
		except UnboundLocalError:
			pass
################################################## end conexion base de datos ####################################################

################################################## begin crear base de datos #####################################################
def createdb():
	con, cur = conexion_open(conexion1)
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur.execute("create database db_canaima")
	cur.execute("alter role %s with superuser" % (usuario,))
	cur.close()
	con.close()

	con, cur = conexion_open(conexion2)
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

	db_canaima_file = open('db_canaima.sql', 'r')
	sqlfile  = db_canaima_file.read()
	cur.execute(sqlfile)
################################################## end crear base de datos #######################################################

################################################## begin main ####################################################################
print "registro-canaima Copyright (C) 2016 Luis Acevedo\nregistro-canaima comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; type `show c' for details.\n"
usuario = getpass.getpass("Nombre usuario postgresql: ")
password = getpass.getpass("Contraseña postgresql: ")

conexion1 = "dbname=postgres user=%s password=%s" % (usuario, password)
conexion2 = "dbname=db_canaima user=%s password=%s" % (usuario, password)

try:
	con, cur = conexion_open(conexion1)
	cur.execute("select datname from pg_database where datname = (%s)", ("db_canaima",))
	row = cur.fetchall()
	con.close()
except (NameError, TypeError):
	pass
finally:
	try:
		if len(row) == 1:
			print "Conectado"
		else:
			print "Creando db_canaima"
			createdb()
			print "db_canaima creada"
	except NameError:
		pass
################################################## end main #####################################################################

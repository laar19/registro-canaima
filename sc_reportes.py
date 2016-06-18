#!/usr/bin/env python
#! -*- coding: utf-8 -*-

#librería visuales
from Tkinter import*
import tkMessageBox
import ttk

#conexión con la base de datos
from conexiondb.sc_conexiondb import conexion_open, conexion2

global con, cur
try:
	con, cur = conexion_open(conexion2)
except TypeError:
	pass

################################################## inicio class Appselect ##################################################

class Appselect:
	def __init__(self):

		#ventana principal
		self.root = Tk()
		#self.root.config(bg = "grey")
		#self.root.geometry("830x430")
		self.root.title("sistema-canaima-reportes")
		
		################################################## self.labelframe_select0 ##################################################
		#global self.labelframe_select0
		self.labelframe_select0 = LabelFrame(self.root, text = "Total de equipos por entidad")
		self.labelframe_select0.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 5)

		################################################## inicio self.labelframe_select0 ##################################################
		#municipio_centro. Municipio de ubicación del plantel
		self.label1 = Label(self.labelframe_select0, text = "Municipios o centros")
		self.label1.grid(row = 1, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		municipio_centro = StringVar()
		def municipio_centro_mayuscula(self):
			municipio_centro.set(municipio_centro.get().upper())

		self.municipio_centro_combobox1 = ttk.Combobox(self.labelframe_select0, textvariable = municipio_centro, values = ["ARISMENDI", "DIAZ", "MARCANO", "TUBORES", "PENINSULA DE MACANAO", "GARCIA", "MARINO", "MANEIRO", "ANTOLIN DEL CAMPO", "VILLALBA", "GOMEZ"])
		self.municipio_centro_combobox1.bind("<KeyRelease>", municipio_centro_mayuscula)
		self.municipio_centro_combobox1.configure(width = 18)
		self.municipio_centro_combobox1.grid(row = 1, column = 1)

		#institución
		self.label2 = Label(self.labelframe_select0, text = "Institución")
		self.label2.grid(row = 2, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		institucion_c = StringVar()
		def institucion_c_mayuscula(self):
			institucion_c.set(institucion_c.get().upper())

		self.institucion_c_entry1 = Entry(self.labelframe_select0, textvariable = institucion_c)
		self.institucion_c_entry1.bind("<KeyRelease>", institucion_c_mayuscula)
		self.institucion_c_entry1.grid(row = 2, column = 1)

		#fecha rango de la busqueda
		#fec_re_re
		self.label2 = Label(self.labelframe_select0, text = "Desde")
		self.label2.grid(row = 1, column = 2)
		self.fec_re_re_1_entry2 = Entry(self.labelframe_select0)
		self.fec_re_re_1_entry2.grid(row = 1, column = 3)
		#fec_en_re
		self.label3 = Label(self.labelframe_select0, text = "Hasta")
		self.label3.grid(row = 1, column = 4)
		self.fec_re_re_2_entry3 = Entry(self.labelframe_select0)
		self.fec_re_re_2_entry3.grid(row = 1, column = 5)
		#act_re
		act_re_entry_var = StringVar()
		self.label4 = Label(self.labelframe_select0, text = "Actualizadas")
		self.label4.grid(row = 3, column = 0)
		self.act_re_entry4 = Entry(self.labelframe_select0, textvariable = act_re_entry_var, state = DISABLED)
		self.act_re_entry4.grid(row = 3, column = 1)
		#entregada_re
		entregada_re_entry_var = StringVar()
		self.label5 = Label(self.labelframe_select0, text = "Entregadas")
		self.label5.grid(row = 4, column = 0)
		self.entregada_re_entry5 = Entry(self.labelframe_select0, textvariable = entregada_re_entry_var, state = DISABLED)
		self.entregada_re_entry5.grid(row = 4, column = 1)
		#cambio_re
		cambio_re_entry_var = StringVar()
		self.label6 = Label(self.labelframe_select0, text = "Cambio")
		self.label6.grid(row = 5, column = 0)
		self.cambio_re_entry6 = Entry(self.labelframe_select0, textvariable = cambio_re_entry_var, state = DISABLED)
		self.cambio_re_entry6.grid(row = 5, column = 1)
		#diagnositacas
		diagnosticadas_var = StringVar()
		self.labeldiag1 = Label(self.labelframe_select0, text = "Diagnosticos")
		self.labeldiag1.grid(row = 2, column = 2)
		self.diagnosticadas_entry7 = Entry(self.labelframe_select0, textvariable = diagnosticadas_var, state = DISABLED)
		self.diagnosticadas_entry7.grid(row = 2, column = 3)
		#equipos_recibidos
		recibidos_var = StringVar()
		self.labelre = Label(self.labelframe_select0, text = "Equipos")
		self.labelre.grid(row = 3, column = 2)
		self.recibidos_entry8 = Entry(self.labelframe_select0, textvariable = recibidos_var, state = DISABLED)
		self.recibidos_entry8.grid(row = 3, column = 3)

		#Boton
		self.boton1 = Button(self.labelframe_select0, text = " Buscar", cursor = "circle", command = self.total_equipos, bg = "grey", activebackground = "grey")
		self.boton1.grid(row = 2, column = 6, columnspan = 1)
		self.boton2 = Button(self.labelframe_select0, text = "Limpiar", cursor = "pirate", command = self.limpiar, bg = "grey", activebackground = "grey")
		self.boton2.grid(row = 3, column = 6, columnspan = 1)


		################################################## fin self.labelframe_select0 ##################################################

	################################################## inicio consultas ##################################################

	############################################# inicio total de equipos por municipios o centros #############################################
	def total_equipos(self):
		municipio_centro = str(self.municipio_centro_combobox1.get())#variable que guarda el argumento de búsqueda (municipio o centro de actualización)
		#variables que guardan las fechas ingresadas para el rango de búsqueda
		fec_re_re_1 = str(self.fec_re_re_1_entry2.get())
		fec_re_re_2 = str(self.fec_re_re_2_entry3.get())

		institucion_c = str(self.institucion_c_entry1.get())#institución donde fue entregado el equipo

		##################################################
		#inicio# si no se especifica ninguna institución, municipio o centro, se muestran todos los equipos
		##################################################
		if len(municipio_centro) == 0 and len(institucion_c) == 0:
			##################################################
			#inicio# si no se especifica ninguna fecha, se muestran los equipos de todas las instituciones, municipios o centros
			##################################################
			if len(fec_re_re_1) == 0 or len(fec_re_re_2) == 0:
				#se muestran todos los equipos diagnosticadados de todas las instituciones, municipios o centros, sin fecha
				con, cur = conexion_open(conexion2)
				#cur.execute("SELECT id_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n")
				cur.execute("select id_re from tab_reparacion_re")
				row_total_diagnosticadas_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.diagnosticadas_entry7.config(state = NORMAL)
				self.diagnosticadas_entry7.delete(0, "end")
				self.diagnosticadas_entry7.insert(0, len(row_total_diagnosticadas_municipio_centro))
				self.diagnosticadas_entry7.config(state = DISABLED)

				#se muestran todos los equipos actualizados de todas las instituciones, municipios o centros, sin fecha
				con, cur = conexion_open(conexion2)
				#cur.execute("SELECT act_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE act_re = (%s)", ("1",))
				cur.execute("select act_re from tab_reparacion_re where act_re = (%s)", ("1",))
				row_total_act_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.act_re_entry4.config(state = NORMAL)
				self.act_re_entry4.delete(0, "end")
				self.act_re_entry4.insert(0, len(row_total_act_re_municipio_centro))
				self.act_re_entry4.config(state = DISABLED)

				#se muestran todos los equipos entregados de todas las instituciones, municipios o centros, sin fecha
				con, cur = conexion_open(conexion2)
				#cur.execute("SELECT entregada_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE entregada_re = (%s)", ("1",))
				cur.execute("select entregada_re from tab_reparacion_re where entregada_re = (%s)", ("1",))
				row_total_entregada_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.entregada_re_entry5.config(state = NORMAL)
				self.entregada_re_entry5.delete(0, "end")
				self.entregada_re_entry5.insert(0, len(row_total_entregada_re_municipio_centro))
				self.entregada_re_entry5.config(state = DISABLED)

				#se muestran todos los equipos para cambio de todas las instituciones, municipios o centros, sin fecha
				con, cur = conexion_open(conexion2)
				#cur.execute("SELECT cambio_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE cambio_re = (%s)", ("1",))
				cur.execute("select cambio_re from tab_reparacion_re where cambio_re = (%s)", ("1",))
				row_total_cambio_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.cambio_re_entry6.config(state = NORMAL)
				self.cambio_re_entry6.delete(0, "end")
				self.cambio_re_entry6.insert(0, len(row_total_cambio_re_municipio_centro))
				self.cambio_re_entry6.config(state = DISABLED)

				#se muestran todos los equipos recibidos de todas las instituciones, municipios o centros, sin fecha
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT serial_c FROM tab_canaima_c")
				row_total_equipos_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.recibidos_entry8.config(state = NORMAL)
				self.recibidos_entry8.delete(0, "end")
				self.recibidos_entry8.insert(0, len(row_total_equipos_municipio_centro))
				self.recibidos_entry8.config(state = DISABLED)
			##################################################
			#fin# si no se especifica ninguna fecha, se muestran todos los equipos de las instituciones, municipios o centros
			##################################################

			##################################################
			#inicio# se filtran los equipos por fecha
			##################################################
			else:
				#se muestran todos los equipos diagnosticadados de todas las instituciones, municipios o centros, por fecha
				con, cur = conexion_open(conexion2)
				#cur.execute("SELECT id_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE fec_re_re BETWEEN (%s) AND (%s)", (fec_re_re_1, fec_re_re_2,))
				cur.execute("select id_re from tab_reparacion_re where fec_re_re between (%s) and (%s)", (fec_re_re_1, fec_re_re_2,))
				row_total_diagnosticadas_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.diagnosticadas_entry7.config(state = NORMAL)
				self.diagnosticadas_entry7.delete(0, "end")
				self.diagnosticadas_entry7.insert(0, len(row_total_diagnosticadas_municipio_centro))
				self.diagnosticadas_entry7.config(state = DISABLED)

				#se muestran todos los equipos actualizados de todas las instituciones, municipios o centros, por fecha
				con, cur = conexion_open(conexion2)
				#cur.execute("SELECT act_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE act_re = (%s) AND fec_re_re BETWEEN (%s) AND (%s)", ("1", fec_re_re_1, fec_re_re_2,))
				cur.execute("select act_re from tab_reparacion_re where act_re = (%s) and fec_re_re between (%s) and (%s)", ("1", fec_re_re_1, fec_re_re_2,))
				row_total_act_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.act_re_entry4.config(state = NORMAL)
				self.act_re_entry4.delete(0, "end")
				self.act_re_entry4.insert(0, len(row_total_act_re_municipio_centro))
				self.act_re_entry4.config(state = DISABLED)

				#se muestran todos los equipos entregados de todas las instituciones, municipios o centros, por fecha
				con, cur = conexion_open(conexion2)
				#cur.execute("SELECT entregada_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE entregada_re = (%s) AND fec_re_re BETWEEN (%s) AND (%s)", ("1", fec_re_re_1, fec_re_re_2,))
				cur.execute("select entregada_re from tab_reparacion_re where entregada_re = (%s) and fec_re_re between (%s) and (%s)", ("1", fec_re_re_1, fec_re_re_2,))
				row_total_entregada_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.entregada_re_entry5.config(state = NORMAL)
				self.entregada_re_entry5.delete(0, "end")
				self.entregada_re_entry5.insert(0, len(row_total_entregada_re_municipio_centro))
				self.entregada_re_entry5.config(state = DISABLED)

				#se muestran todos los equipos para cambio de todas las instituciones, municipios o centros, por fecha
				con, cur = conexion_open(conexion2)
				#cur.execute("SELECT cambio_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE cambio_re = (%s) AND fec_re_re BETWEEN (%s) AND (%s)", ("1", fec_re_re_1, fec_re_re_2,))
				cur.execute("select cambio_re from tab_reparacion_re where cambio_re = (%s) and fec_re_re between (%s) and (%s)", ("1", fec_re_re_1, fec_re_re_2,))
				row_total_cambio_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.cambio_re_entry6.config(state = NORMAL)
				self.cambio_re_entry6.delete(0, "end")
				self.cambio_re_entry6.insert(0, len(row_total_cambio_re_municipio_centro))
				self.cambio_re_entry6.config(state = DISABLED)

				#se muestran todos los equipos recibidos de todas las instituciones, municipios o centros, por fecha
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT serial_c FROM tab_reparacion_re WHERE fec_re_re BETWEEN (%s) AND (%s)", (fec_re_re_1, fec_re_re_2,))
				row_lista_reparaciones = cur.fetchall()
				cur.close()
				con.close()

				#debido a que pueden existir varios registros de un mismo equipo se procede a filtrar sólo los equipos por fecha
				total_equipos_municipio_centro = []
				for i in row_lista_reparaciones:
					if i not in total_equipos_municipio_centro:
						total_equipos_municipio_centro.append(i)

				self.recibidos_entry8.config(state = NORMAL)
				self.recibidos_entry8.delete(0, "end")
				self.recibidos_entry8.insert(0, len(total_equipos_municipio_centro))
				self.recibidos_entry8.config(state = DISABLED)
			##################################################
			#fin# se filtran los equipos por fecha
			##################################################

		##################################################
		#fin# si no se especifica ninguna institución, municipio o centro, se muestran todos los equipos
		##################################################

		##################################################
		#inicio# se muestran los equipos por municipios o centros, sin institución ni fecha
		##################################################
		elif len(municipio_centro) > 0 and len(institucion_c) == 0:
			##################################################
			#inicio# si no se especifica ninguna fecha, se muestran todos los equipos por municipios o centros sin institución ni fecha
			##################################################
			if len(fec_re_re_1) == 0 or len(fec_re_re_2) == 0:			
				#se muestran todos los equipos diagnosticadados por municipios o centros sin institución ni fecha
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT id_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE municipio_n = (%s) OR centro_re = (%s)", (municipio_centro, municipio_centro,))
				row_total_diagnosticadas_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.diagnosticadas_entry7.config(state = NORMAL)
				self.diagnosticadas_entry7.delete(0, "end")
				self.diagnosticadas_entry7.insert(0, len(row_total_diagnosticadas_municipio_centro))
				self.diagnosticadas_entry7.config(state = DISABLED)

				#se muestran todos los equipos actualizados por municipios o centros sin institución ni fecha
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT act_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE (municipio_n = (%s) OR centro_re = (%s)) AND act_re = (%s)", (municipio_centro, municipio_centro, "1",))
				row_total_act_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.act_re_entry4.config(state = NORMAL)
				self.act_re_entry4.delete(0, "end")
				self.act_re_entry4.insert(0, len(row_total_act_re_municipio_centro))
				self.act_re_entry4.config(state = DISABLED)

				#se muestran todos los equipos entregados por municipios o centros sin institución ni fecha
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT entregada_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE (municipio_n = (%s) OR centro_re = (%s)) AND entregada_re = (%s)", (municipio_centro, municipio_centro, "1",))
				row_total_entregada_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.entregada_re_entry5.config(state = NORMAL)
				self.entregada_re_entry5.delete(0, "end")
				self.entregada_re_entry5.insert(0, len(row_total_entregada_re_municipio_centro))
				self.entregada_re_entry5.config(state = DISABLED)

				#se muestran todos los equipos para cambio por municipios o centros sin institución ni fecha
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT cambio_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE (municipio_n = (%s) OR centro_re = (%s)) AND cambio_re = (%s)", (municipio_centro, municipio_centro, "1",))
				row_total_cambio_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.cambio_re_entry6.config(state = NORMAL)
				self.cambio_re_entry6.delete(0, "end")
				self.cambio_re_entry6.insert(0, len(row_total_cambio_re_municipio_centro))
				self.cambio_re_entry6.config(state = DISABLED)

				#se muestran todos los equipos recibidos por municipios o centros sin institución ni fecha
				lista_municipios = ["ARISMfinI", "DIAZ", "MARCANO", "TUBORES", "PENINSULA DE MACANAO", "GARCIA", "MARINO", "MANEIRO", "ANTOLIN DEL CAMPO", "VILLALBA", "GOMEZ"]
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT c.serial_c FROM (tab_canaima_c AS a INNER JOIN tab_nino_n AS b ON a.ci_n = b.ci_n) INNER JOIN tab_reparacion_re AS c ON a.serial_c = c.serial_c WHERE (municipio_n = (%s) OR centro_re = (%s))", (municipio_centro, municipio_centro,))
				row_lista_reparaciones = cur.fetchall()
				cur.close()
				con.close()

				#debido a que pueden existir varios registros de un mismo equipo se procede a filtrar sólo los equipos sin fecha
				total_equipos_municipio_centro = []
				for i in row_lista_reparaciones:
					if i not in total_equipos_municipio_centro:
						total_equipos_municipio_centro.append(i)

				self.recibidos_entry8.config(state = NORMAL)
				self.recibidos_entry8.delete(0, "end")
				self.recibidos_entry8.insert(0, len(total_equipos_municipio_centro))
				self.recibidos_entry8.config(state = DISABLED)
			##################################################
			#fin# si no se especifica ninguna fecha, se muestran todos los equipos por municipios o centros sin institución ni fecha
			##################################################

			##################################################
			#inicio# si se especifica alguna fecha
			##################################################
			else:
				#se muestran todos los equipos diagnosticadados por municipios o centros, filtrados por fecha sin institución
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT id_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE (municipio_n = (%s) OR centro_re = (%s)) AND fec_re_re BETWEEN (%s) AND (%s)", (municipio_centro, municipio_centro, fec_re_re_1, fec_re_re_2,))
				row_total_diagnosticadas_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.diagnosticadas_entry7.config(state = NORMAL)
				self.diagnosticadas_entry7.delete(0, "end")
				self.diagnosticadas_entry7.insert(0, len(row_total_diagnosticadas_municipio_centro))
				self.diagnosticadas_entry7.config(state = DISABLED)

				#se muestran todos los equipos actualizados por municipios o centros, filtrados por fecha sin institución
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT act_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE ((municipio_n = (%s) OR centro_re = (%s)) AND act_re = (%s)) AND fec_re_re BETWEEN (%s) AND (%s)", (municipio_centro, municipio_centro, "1", fec_re_re_1, fec_re_re_2,))
				row_total_act_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.act_re_entry4.config(state = NORMAL)
				self.act_re_entry4.delete(0, "end")
				self.act_re_entry4.insert(0, len(row_total_act_re_municipio_centro))
				self.act_re_entry4.config(state = DISABLED)

				#se muestran todos los equipos entregados de por municipios o centros, filtrados por fecha sin institución
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT entregada_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE ((municipio_n = (%s) OR centro_re = (%s)) AND entregada_re = (%s)) AND fec_re_re BETWEEN (%s) AND (%s)", (municipio_centro, municipio_centro, "1", fec_re_re_1, fec_re_re_2,))
				row_total_entregada_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.entregada_re_entry5.config(state = NORMAL)
				self.entregada_re_entry5.delete(0, "end")
				self.entregada_re_entry5.insert(0, len(row_total_entregada_re_municipio_centro))
				self.entregada_re_entry5.config(state = DISABLED)

				#se muestran todos los equipos para cambio por municipios o centros, filtrados por fecha sin institución
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT cambio_re FROM (tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c) INNER JOIN tab_nino_n AS c ON c.ci_n = b.ci_n WHERE ((municipio_n = (%s) OR centro_re = (%s)) AND cambio_re = (%s)) AND fec_re_re BETWEEN (%s) AND (%s)", (municipio_centro, municipio_centro, "1", fec_re_re_1, fec_re_re_2,))
				row_total_cambio_re_municipio_centro = cur.fetchall()
				cur.close()
				con.close()

				self.cambio_re_entry6.config(state = NORMAL)
				self.cambio_re_entry6.delete(0, "end")
				self.cambio_re_entry6.insert(0, len(row_total_cambio_re_municipio_centro))
				self.cambio_re_entry6.config(state = DISABLED)

				#se muestran todos los equipos recibidos por municipios o centros, filtrados por fecha sin institución
				lista_municipios = ["ARISMfinI", "DIAZ", "MARCANO", "TUBORES", "PENINSULA DE MACANAO", "GARCIA", "MARINO", "MANEIRO", "ANTOLIN DEL CAMPO", "VILLALBA", "GOMEZ"]
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT c.serial_c FROM (tab_canaima_c AS a INNER JOIN tab_nino_n AS b ON a.ci_n = b.ci_n) INNER JOIN tab_reparacion_re AS c ON a.serial_c = c.serial_c WHERE (municipio_n = (%s) OR centro_re = (%s)) AND fec_re_re BETWEEN (%s) AND (%s)", (municipio_centro, municipio_centro, fec_re_re_1, fec_re_re_2,))
				row_lista_reparaciones = cur.fetchall()
				cur.close()
				con.close()

				#debido a que pueden existir varios registros de un mismo equipo se procede a filtrar sólo los equipos
				total_equipos_municipio_centro = []
				for i in row_lista_reparaciones:
					if i not in total_equipos_municipio_centro:
						total_equipos_municipio_centro.append(i)

				self.recibidos_entry8.config(state = NORMAL)
				self.recibidos_entry8.delete(0, "end")
				self.recibidos_entry8.insert(0, len(total_equipos_municipio_centro))
				self.recibidos_entry8.config(state = DISABLED)
			##################################################
			#fin# si se especifica alguna fecha se muestran todos los equipos por municipios o centros, filtrados por fecha sin institución
			##################################################

		##################################################
		#fin# se muestran los equipos por municipio
		##################################################

		##################################################
		#inicio# se muestran los equipos por institución sin fecha ni municipios o centros
		##################################################
		elif len(municipio_centro) == 0 and len(institucion_c) > 0:

			#se verifica la institución ingresada
			con, cur = conexion_open(conexion2)
			cur.execute("SELECT institucion_c FROM tab_canaima_c WHERE institucion_c LIKE '%%' || %s || '%%'", (institucion_c,))
			row_institucion = cur.fetchall()
			cur.close()
			con.close()

			#evitar duplicados en la institución ingresada
			row_instituciones = []
			for i in row_institucion:
				if i not in row_instituciones:
					row_instituciones.append(i)

			if len(row_instituciones) > 1:
				#se crea una lista con las instituciones que coincidieron con la búsqueda
				lista = Tk()
				lista.title("Instituciones encontradas en la búsqueda")
				listbox = Listbox(lista, width = "50")
				listbox.pack()
				#se llena el listbox con las insituciones encontradas
				#se prevee no llenar el listbox con instituciones duplicadas
				instituciones = []
				for i in row_institucion:
					if i not in instituciones:
						instituciones.append(i)
						listbox.insert(END, str(i).strip("[('',)]"))

			elif len(row_instituciones) == 1:
				##################################################
				#inicio# si no se especifica ninguna fecha, se muestran todos los equipos por institución, sin municipios o centros
				##################################################
				if len(fec_re_re_1) == 0 or len(fec_re_re_2) == 0:
					#se muestran todos los equipos diagnosticadados por institución, sin fecha ni municipios o centros
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%'", (institucion_c,))
					row_total_diagnosticadas_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.diagnosticadas_entry7.config(state = NORMAL)
					self.diagnosticadas_entry7.delete(0, "end")
					self.diagnosticadas_entry7.insert(0, len(row_total_diagnosticadas_institucion))
					self.diagnosticadas_entry7.config(state = DISABLED)

					#se muestran todos los equipos actualizados por institución, sin fecha ni municipios o centros
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND act_re = (%s)", (institucion_c, "1",))
					row_total_act_re_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.act_re_entry4.config(state = NORMAL)
					self.act_re_entry4.delete(0, "end")
					self.act_re_entry4.insert(0, len(row_total_act_re_institucion))
					self.act_re_entry4.config(state = DISABLED)

					#se muestran todos los equipos entregados por institución, sin fecha ni municipios o centros
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND entregada_re = (%s)", (institucion_c, "1",))
					row_total_entregada_re_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.entregada_re_entry5.config(state = NORMAL)
					self.entregada_re_entry5.delete(0, "end")
					self.entregada_re_entry5.insert(0, len(row_total_entregada_re_institucion))
					self.entregada_re_entry5.config(state = DISABLED)

					#se muestran todos los equipos para cambio por institución, sin fecha ni municipios o centros
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND cambio_re = (%s)", (institucion_c, "1",))
					row_total_cambio_re_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.cambio_re_entry6.config(state = NORMAL)
					self.cambio_re_entry6.delete(0, "end")
					self.cambio_re_entry6.insert(0, len(row_total_cambio_re_institucion))
					self.cambio_re_entry6.config(state = DISABLED)

					#se muestran todos los equipos recibidos por institución, sin fecha ni municipios o centros
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_canaima_c WHERE institucion_c LIKE '%%' || %s || '%%'", (institucion_c,))
					row_total_equipos_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.recibidos_entry8.config(state = NORMAL)
					self.recibidos_entry8.delete(0, "end")
					self.recibidos_entry8.insert(0, len(row_total_equipos_institucion))
					self.recibidos_entry8.config(state = DISABLED)
				##################################################
				#fin# se muestran los equipos por institución sin fecha ni municipios o centros
				##################################################

				##################################################
				#inicio# se muestran los equipos por institución, fecha sin municipios o centros
				##################################################
				else:
					#se muestran todos los equipos diagnosticadados por institución, filtrados por fecha sin municipio o centro
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND fec_re_re BETWEEN (%s) AND (%s)", (institucion_c, fec_re_re_1, fec_re_re_2,))
					row_total_diagnosticadas_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.diagnosticadas_entry7.config(state = NORMAL)
					self.diagnosticadas_entry7.delete(0, "end")
					self.diagnosticadas_entry7.insert(0, len(row_total_diagnosticadas_institucion))
					self.diagnosticadas_entry7.config(state = DISABLED)

					#se muestran todos los equipos actualizados por institución, filtrados por fecha sin municipio o centro
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND act_re = (%s) AND fec_re_re BETWEEN (%s) AND (%s)", (institucion_c, "1", fec_re_re_1, fec_re_re_2,))
					row_total_act_re_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.act_re_entry4.config(state = NORMAL)
					self.act_re_entry4.delete(0, "end")
					self.act_re_entry4.insert(0, len(row_total_act_re_institucion))
					self.act_re_entry4.config(state = DISABLED)

					#se muestran todos los equipos entregados por institución, filtrados por fecha sin municipio o centro
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_reparacion_re AS a INNER JOIN tab_canaima_c AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND entregada_re = (%s) AND fec_re_re BETWEEN (%s) AND (%s)", (institucion_c, ("1"), fec_re_re_1, fec_re_re_2,))
					row_total_entregada_re_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.entregada_re_entry5.config(state = NORMAL)
					self.entregada_re_entry5.delete(0, "end")
					self.entregada_re_entry5.insert(0, len(row_total_entregada_re_institucion))
					self.entregada_re_entry5.config(state = DISABLED)

					#se muestran todos los equipos para cambio por institución, filtrados por fecha sin municipio o centro
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_canaima_c AS a INNER JOIN tab_reparacion_re AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND cambio_re = (%s) AND fec_re_re BETWEEN (%s) AND (%s)", (institucion_c, "1", fec_re_re_1, fec_re_re_2,))
					row_total_cambio_re_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.cambio_re_entry6.config(state = NORMAL)
					self.cambio_re_entry6.delete(0, "end")
					self.cambio_re_entry6.insert(0, len(row_total_cambio_re_institucion))
					self.cambio_re_entry6.config(state = DISABLED)



					#se muestran todos los equipos recibidos por institución, sin fecha ni municipios o centros
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_canaima_c AS a INNER JOIN tab_reparacion_re AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND fec_re_re BETWEEN (%s) AND (%s)", (institucion_c, fec_re_re_1, fec_re_re_2,))
					row_total_equipos_institucion = cur.fetchall()
					cur.close()
					con.close()

					self.recibidos_entry8.config(state = NORMAL)
					self.recibidos_entry8.delete(0, "end")
					self.recibidos_entry8.insert(0, len(row_total_equipos_institucion))
					self.recibidos_entry8.config(state = DISABLED)



					#se muestran todos los equipos recibidos por institución, filtrados por fecha sin municipio o centro
					con, cur = conexion_open(conexion2)
					cur.execute("SELECT institucion_c FROM tab_canaima_c AS a INNER JOIN tab_reparacion_re AS b ON a.serial_c = b.serial_c WHERE institucion_c LIKE '%%' || %s || '%%' AND fec_re_re BETWEEN (%s) AND (%s)", (institucion_c, fec_re_re_1, fec_re_re_2,))
					row_lista_reparaciones = cur.fetchall()
					cur.close()
					con.close()

					#debido a que pueden existir varios registros de un mismo equipo se procede a filtrar sólo los equipos
					total_equipos_institucion = []
					for i in row_lista_reparaciones:
						if i not in total_equipos_institucion:
							total_equipos_institucion.append(i)

					self.recibidos_entry8.config(state = NORMAL)
					self.recibidos_entry8.delete(0, "end")
					self.recibidos_entry8.insert(0, len(total_equipos_institucion))
					self.recibidos_entry8.config(state = DISABLED)
				##################################################
				#fin# si se especifica alguna fecha se muestran todos los equipos por municipios o centros, filtrados por fecha sin institución
				##################################################
			else:
				tkMessageBox.showinfo("postgresql", "La institución no se encuentra registrada.")
		else:
			tkMessageBox.showinfo("sistema-canaima", "Debe buscar una instancia a la vez:\nPor municipio o centro de actualización.\nO por institución.")

		################################################## fin total de equipos por institucion #############################################

	################################################## fin consultas ##################################################

	################################################## inicio limpiar ##################################################

	def limpiar(self):
		self.municipio_centro_combobox1.delete(0, "end")
		self.institucion_c_entry1.delete(0, "end")
		self.fec_re_re_1_entry2.delete(0, "end")
		self.fec_re_re_2_entry3.delete(0, "end")
	################################################## fin limpiar ##################################################

################################################## fin class Appselect ##################################################

"""if __name__ == "__main__":
	#ventana principal
	root = Tk()
	#root.config(bg = "grey")
	#root.geometry("830x430")
	root.title("sistema-canaima-reportes")

	app = Appselect(root)
	app.run()
	root.mainloop()"""

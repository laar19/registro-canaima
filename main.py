#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import sys

#librerías visuales
from Tkinter import*
import tkMessageBox
import ttk

#conexión con la base de datos
from conexiondb.sc_conexiondb import conexion_open, conexion2
from conexiondb.sc_conexiondb import*

#reportes
from sc_reportes import Appselect

global con, cur, app
try:
	con, cur = conexion_open(conexion2)
except TypeError:
	print "\nError al conectar con postgresql, por favor verifique:"
	print "\n1.- Usuario o contraseña incorrecto"
	print "\n2.- Si postgresql no se encuentra instalado o el servicio no se está ejecutando:\n*Para instalarlo: sudo apt-get install postgresql\n*Si está instalado, para ejecutar el servicio: sudo service postgresql start\n"
	sys.exit()
################################################## inicio class Formulario ##################################################

class Formulario:
	def __init__(self):

		#ventana principal
		self.root = Tk()
		#self.root.config(bg = "grey")
		self.root.geometry("740x320")
		self.root.title("sistema-canaima")

		#menú
		self.menubar = Menu(self.root, bg = "grey")
		#menú1 salir
		self.salir_menu1 = Menu(self.menubar, tearoff = 0)
		self.salir_menu1.add_command(label = "Exit", command = self.root.quit)
		self.menubar.add_cascade(label = "Salir", menu = self.salir_menu1)

		self.root.config(menu=self.menubar)

		################################################## self.labelframe_form0 ##################################################

		self.labelframe_form0 = LabelFrame(self.root, text = "Registrar equipo")
		self.labelframe_form0.grid(row = 0, column = 0, sticky = W+E+N+S, padx = 5)

		################################################## inicio self.labelframe_form0 ##################################################

		################################################## inicio tab_nino_n ##################################################

		self.label0 = Label(self.labelframe_form0, text = "Datos del alumno", bg = "grey")
		self.label0.grid(row = 0, column = 0)

		#ci_n. Número de cédula del alumno
		self.label1 = Label(self.labelframe_form0, text = "*Cédula del alumno")
		self.label1.grid(row = 1, column = 0)
		self.ci_n_entry1 = Entry(self.labelframe_form0)
		self.ci_n_entry1.grid(row = 1, column = 1)

		#nombre_n. Nombre del alumno
		self.label2 = Label(self.labelframe_form0, text = "*Nombre del alumno")
		self.label2.grid(row = 2, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		nombre_n = StringVar()
		def nombre_n_mayuscula(self):
			nombre_n.set(nombre_n.get().upper())

		self.nombre_n_entry2 = Entry(self.labelframe_form0, textvariable = nombre_n)
		self.nombre_n_entry2.bind("<KeyRelease>", nombre_n_mayuscula)
		self.nombre_n_entry2.grid(row = 2, column = 1)

		#plantel donde estudia el alumno_n. Plantel en el que estudia el alumno.
		self.label3 = Label(self.labelframe_form0, text = "*Plantel")
		self.label3.grid(row = 3, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		plantel_n = StringVar()
		def plantel_n_mayuscula(self):
			plantel_n.set(plantel_n.get().upper())

		self.plantel_n_entry3 = Entry(self.labelframe_form0, textvariable = plantel_n)
		self.plantel_n_entry3.bind("<KeyRelease>", plantel_n_mayuscula)
		self.plantel_n_entry3.grid(row = 3, column = 1)

		#nivel_n. Nivel académico del alumno
		self.label4 = Label(self.labelframe_form0, text = "*Nivel académico")
		self.label4.grid(row = 4, column = 0)
		nivel_n = StringVar()
		self.nivel_n_combobox1 = ttk.Combobox(self.labelframe_form0, textvariable = nivel_n, values = ["1ERGRADO", "2DOGRADO", "3ERGRADO", "4TOGRADO", "5TOGRADO", "6TOGRADO", "1ERANO", "2DOANO", "3ERANO", "4TOANO", "5TOANO", "6TOANO"])
		self.nivel_n_combobox1.configure(width = 18)
		self.nivel_n_combobox1.grid(row = 4, column = 1)

		#municipio donde queda ubicado el plantel donde estudia el alumno_n. Municipio de ubicación del plantel
		self.label5 = Label(self.labelframe_form0, text = "*Municipio")
		self.label5.grid(row = 5, column = 0)
		municipio_n = StringVar()
		self.municipio_n_combobox2 = ttk.Combobox(self.labelframe_form0, textvariable = municipio_n, values = ["ARISMENDI", "DIAZ", "MARCANO", "TUBORES", "PENINSULA DE MACANAO", "GARCIA", "MARINO", "MANEIRO", "ANTOLIN DEL CAMPO", "VILLALBA", "GOMEZ"])
		self.municipio_n_combobox2.configure(width = 18)
		self.municipio_n_combobox2.grid(row = 5, column = 1)

		################################################## fin tab_nino_n ##################################################

		################################################## inicio tab_representante_r ##################################################

		self.label6 = Label(self.labelframe_form0, text = "Datos del representante", bg = "grey")
		self.label6.grid(row = 6, column = 0)

		#ci_r. Número de cédula del representante
		self.label7 = Label(self.labelframe_form0, text = "*Cédula del representante")
		self.label7.grid(row = 7, column = 0)
		self.ci_r_entry6 = Entry(self.labelframe_form0)
		self.ci_r_entry6.grid(row = 7, column = 1)

		#nombre_r. Nombre del representante
		self.label8 = Label(self.labelframe_form0, text = "*Nombre del representante")
		self.label8.grid(row = 8, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		nombre_r = StringVar()
		def nombre_r_mayuscula(self):
			nombre_r.set(nombre_r.get().upper())

		self.nombre_r_entry7 = Entry(self.labelframe_form0, textvariable = nombre_r)
		self.nombre_r_entry7.bind("<KeyRelease>", nombre_r_mayuscula)
		self.nombre_r_entry7.grid(row = 8, column = 1)

		#tlf_r. Número de teléfono del representante
		self.label9 = Label(self.labelframe_form0, text = "Teléfono")
		self.label9.grid(row = 9, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		tlf_r = StringVar()
		def tlf_r_mayuscula(self):
			tlf_r.set(tlf_r.get().upper())

		self.tlf_r_entry8 = Entry(self.labelframe_form0, textvariable = tlf_r)
		self.tlf_r_entry8.bind("<KeyRelease>", tlf_r_mayuscula)
		self.tlf_r_entry8.grid(row = 9, column = 1)

		################################################## fin tab_representante_r ##################################################

		################################################## inicio tab_canaima_c ##################################################

		self.label10 = Label(self.labelframe_form0, text = "Datos del equipo", bg = "grey")
		self.label10.grid(row = 10, column = 0)

		#serial_c. Serial de equipo
		self.label11 = Label(self.labelframe_form0, text = "*Serial de la canaima")
		self.label11.grid(row = 11, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		serial_c = StringVar()
		def serial_c_mayuscula(self):
			serial_c.set(serial_c.get().upper())

		self.serial_c_entry9 = Entry(self.labelframe_form0, textvariable = serial_c)
		self.serial_c_entry9.bind("<KeyRelease>", serial_c_mayuscula)
		self.serial_c_entry9.grid(row = 11, column = 1)

		#modelo_c. Modelo del equipo
		self.label12 = Label(self.labelframe_form0, text = "*Modelo de la canaima")
		self.label12.grid(row = 12, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		modelo_c = StringVar()
		def modelo_c_mayuscula(self):
			modelo_c.set(modelo_c.get().upper())

		self.modelo_c_entry10 = Entry(self.labelframe_form0, textvariable = modelo_c)
		self.modelo_c_entry10.bind("<KeyRelease>", modelo_c_mayuscula)
		self.modelo_c_entry10.grid(row = 12, column = 1)

		#institucion_c. Plantel en el que fue entregado el equipo.
		self.label13 = Label(self.labelframe_form0, text = "*Institución")
		self.label13.grid(row = 13, column = 0)
		#función para convertir las letras minúsculas en mayúsculas
		institucion_c = StringVar()
		def institucion_c_mayuscula(self):
			institucion_c.set(institucion_c.get().upper())

		self.institucion_c_entry11 = Entry(self.labelframe_form0, textvariable = institucion_c)
		self.institucion_c_entry11.bind("<KeyRelease>", institucion_c_mayuscula)
		self.institucion_c_entry11.grid(row = 13, column = 1)

		################################################## fin tab_canaima_c ##################################################
		
		################################################## inicio tab_reparacion_re ##################################################

		self.label14 = Label(self.labelframe_form0, text = "Datos de la reparación", bg = "grey")
		self.label14.grid(row = 0, column = 2)

		#fec_re_re. Fecha de recepción del equipo
		self.label15 = Label(self.labelframe_form0, text = "*Fecha de recepción")
		self.label15.grid(row = 1, column = 2)
		self.fec_re_re_entry12 = Entry(self.labelframe_form0)
		self.fec_re_re_entry12.grid(row = 1, column = 3)

		#fec_en_re. Fecha de entrega del equipo
		self.label16 = Label(self.labelframe_form0, text = "Fecha de entrega")
		self.label16.grid(row = 2, column = 2)
		self.fec_en_re_entry13 = Entry(self.labelframe_form0)
		self.fec_en_re_entry13.grid(row = 2, column = 3)

		#falla_re. Falla del equipo
		self.label17 = Label(self.labelframe_form0, text = "*Falla")
		self.label17.grid(row = 3, column = 2)
		#función para convertir las letras minúsculas en mayúsculas
		falla_re = StringVar()
		def falla_re_mayuscula(self):
			falla_re.set(falla_re.get().upper())

		self.falla_re_entry14 = Entry(self.labelframe_form0, textvariable = falla_re)
		self.falla_re_entry14.bind("<KeyRelease>", falla_re_mayuscula)
		self.falla_re_entry14.grid(row = 3, column = 3)

		#act_re. Si el equipo fue actualizado o no
		self.act_re_radio_var = StringVar()
		self.label18 = Label(self.labelframe_form0, text = "Actualizada")
		self.label18.grid(row = 4, column = 2)
		self.act_re_radio1 = Radiobutton(self.labelframe_form0, text = "Sí", variable = self.act_re_radio_var, value = True)
		self.act_re_radio1.grid(row = 4, column = 3)
		self.act_re_radio2 = Radiobutton(self.labelframe_form0, text = "No", variable = self.act_re_radio_var, value = False)
		self.act_re_radio2.grid(row = 4, column = 4)
		self.act_re_radio2.select()

		#reparada_re. Si el equipo fue reparado o no
		self.reparada_re_radio_var = StringVar()
		self.label19 = Label(self.labelframe_form0, text = "Reparada")
		self.label19.grid(row = 5, column = 2)
		self.reparada_re_radio3 = Radiobutton(self.labelframe_form0, text = "Sí", variable = self.reparada_re_radio_var, value = True)
		self.reparada_re_radio3.grid(row = 5, column = 3)
		self.reparada_re_radio4 = Radiobutton(self.labelframe_form0, text = "No", variable = self.reparada_re_radio_var, value = False)
		self.reparada_re_radio4.grid(row = 5, column = 4)
		self.reparada_re_radio4.select()

		#entregada_re. Si el equipo fue entregado o no
		self.entregada_re_radio_var = StringVar()
		self.label20 = Label(self.labelframe_form0, text = "Entregada")
		self.label20.grid(row = 6, column = 2)
		self.entregada_re_radio5 = Radiobutton(self.labelframe_form0, text = "Sí", variable = self.entregada_re_radio_var, value = True)
		self.entregada_re_radio5.grid(row = 6, column = 3)
		self.entregada_re_radio6 = Radiobutton(self.labelframe_form0, text = "No", variable = self.entregada_re_radio_var, value = False)
		self.entregada_re_radio6.grid(row = 6, column = 4)
		self.entregada_re_radio6.select()

		#cambio_re. Si el equipo es para cambio o no
		self.cambio_re_radio_var = StringVar()
		self.label21 = Label(self.labelframe_form0, text = "Cambio")
		self.label21.grid(row = 7, column = 2)
		self.cambio_re_radio7 = Radiobutton(self.labelframe_form0, text = "Sí", variable = self.cambio_re_radio_var, value = True)
		self.cambio_re_radio7.grid(row = 7, column = 3)
		self.cambio_re_radio8 = Radiobutton(self.labelframe_form0, text = "No", variable = self.cambio_re_radio_var, value = False)
		self.cambio_re_radio8.grid(row = 7, column = 4)
		self.cambio_re_radio8.select()

		#centro_re. Lugar donde se diagnosticó el equipo
		self.label22 = Label(self.labelframe_form0, text = "*Centro de actualización")
		self.label22.grid(row = 8, column = 2)
		#función para convertir las letras minúsculas en mayúsculas
		centro_re = StringVar()
		def centro_re_mayuscula(self):
			centro_re.set(centro_re.get().upper())

		self.centro_re_entry15 = Entry(self.labelframe_form0, textvariable = centro_re)
		self.centro_re_entry15.bind("<KeyRelease>", centro_re_mayuscula)
		self.centro_re_entry15.grid(row = 8, column = 3)
		self.centro_re_entry15.insert(0, "COORDINACION CBIT")

		################################################## fin tab_reparacion_re ##################################################

		################################################## inicio botones ##################################################

		self.boton1 = Button(self.labelframe_form0, text = "Insertar", cursor = "plus", command = self.validar_insert, bg = "grey", activebackground = "grey")
		self.boton1.grid(row = 11, column = 2, columnspan = 1)
		self.boton2 = Button(self.labelframe_form0, text = "  Buscar  ", cursor = "circle", command = self.buscar, bg = "grey", activebackground = "grey")
		self.boton2.grid(row = 11, column = 2, columnspan = 2)
		self.boton3 = Button(self.labelframe_form0, text = "Modificar", cursor = "exchange", command = self.modificar, bg = "grey", activebackground = "grey")
		self.boton3.grid(row = 11, column = 3, columnspan = 2)
		self.boton4 = Button(self.labelframe_form0, text = "Limpiar", cursor = "pirate", command = self.limpiar, bg = "grey", activebackground = "grey")
		self.boton4.grid(row = 11, column = 4)

		################################################## fin botones ##################################################

	################################################## inicio capturar los datos ##################################################

	#función que captura los datos de los entry y los almacena en variables
	def capturar(self):
		global id_cr#llave primaria de la tabla tab_canaima_representante_cr que relaciona las canaimas con los representante: tab_canaima_c y tab_representante_r
		id_cr = str()

		#datos del alumno: tab_nino_n
		global ci_n#cédula del alumno
		ci_n = str(self.ci_n_entry1.get())
		global nombre_n#nombre del alumno
		nombre_n = str(self.nombre_n_entry2.get())
		nombre_n = nombre_n.strip(" ")
		global plantel_n#plantel donde estudia el alumno
		plantel_n = str(self.plantel_n_entry3.get())
		plantel_n = plantel_n.strip(" ")
		global nivel_n#nivel académico del alumno del alumno
		nivel_n = str(self.nivel_n_combobox1.get())
		global municipio_n#municipio donde queda ubicado el plantel donde estudia el alumno
		municipio_n = str(self.municipio_n_combobox2.get())

		#datos del representante: tab_representante_r
		global ci_r#cédula del representante
		ci_r = str(self.ci_r_entry6.get())
		global nombre_r#nombre del representante
		nombre_r = str(self.nombre_r_entry7.get())
		nombre_r = nombre_r.strip(" ")
		global tlf_r#teléfono del representante
		tlf_r = str(self.tlf_r_entry8.get())

		#datos del equipo: tab_canaima_c
		global serial_c#serial de la canaima
		serial_c = str(self.serial_c_entry9.get())
		global modelo_c#modelo de la canaima
		modelo_c = str(self.modelo_c_entry10.get())
		modelo_c = modelo_c.strip(" ")
		#datos de la institución
		global institucion_c#institución donde fue entregada la canaima
		institucion_c = str(self.institucion_c_entry11.get())
		institucion_c = institucion_c.strip(" ")

		#datos de la raparación: tab_reparacion_re
		global id_re#llave primaria de la tabla reparación: tab_reparacion_re
		id_re = str()
		global fec_re_re#fecha en la que fue recibido el equipo al momento del diagnóstico
		fec_re_re = str(self.fec_re_re_entry12.get())
		global fec_en_re#fecha en que el representante retira el equipo
		fec_en_re = str(self.fec_en_re_entry13.get())
		global falla_re#falla que presenta el equipo
		falla_re = str(self.falla_re_entry14.get())
		global act_re#variable que verifica si el equipo fue actualizado o no
		act_re = str(self.act_re_radio_var.get())
		global reparada_re#variable que verifica si el equipo fue reparado o no
		reparada_re = str(self.reparada_re_radio_var.get())
		global entregada_re#variable que verifica si el equipo fue entregado al representante o no
		entregada_re = str(self.entregada_re_radio_var.get())
		global cambio_re#variable que verifica si el equipo va para cambio o no
		cambio_re = str(self.cambio_re_radio_var.get())
		global centro_re#centro donde se diagnosticó el equipo
		centro_re = str(self.centro_re_entry15.get())
		centro_re = centro_re.strip(" ")
	################################################## fin capturar los datos ##################################################

	################################### inicio generar clave primaria de la tabla reparación: tab_reparacion_re ###############################
	def pk_tab_reparacion_re(self):

		#cur.close()
		#con.close()

		self.capturar()

		con, cur = conexion_open(conexion2)
		cur.execute("SELECT id_re FROM tab_reparacion_re WHERE serial_c = (%s)", (serial_c,))
		self.row = cur.fetchall()
		cur.close()
		con.close()

		guion = "-"
		contador = 0

		#si no existe ninguna reparación registrada
		if len(self.row) == 0:
			contador = contador + 1
		elif len(self.row) > 0:
			contador = len(self.row) + 1
		else:
			tkMessageBox.showinfo("postgresql", "Error al generar la clave primaria de la tabla reparación")

		id_re = str(serial_c) + guion + str(int(contador))

		con, cur = conexion_open(conexion2)
		cur.execute("INSERT INTO tab_reparacion_re VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_re, fec_re_re, fec_en_re, falla_re, act_re, reparada_re, entregada_re, cambio_re, centro_re, serial_c,))
		con.commit()
		cur.close()
		con.close()

		tkMessageBox.showinfo("postgresql", "Los datos se guardaron con éxito")
		self.limpiar()

	################################################## fin generar clave primaria de la reparación #############################################

	################################################## inicio insertar ##################################################

	#se insertan los datos en la base de datos
	def insertar(self):

		self.capturar()

		#validar que no haya duplicidad en las llaves primarias de la base de datos
		#se consultan los datos ingresados con los de la base de datos para su posterior verificación
		con, cur = conexion_open(conexion2)

		cur.execute("SELECT ci_r FROM tab_representante_r WHERE ci_r = (%s)", (ci_r,))
		self.row1 = cur.fetchall()

		cur.execute("SELECT ci_n FROM tab_nino_n WHERE ci_n = (%s)", (ci_n,))
		self.row2 = cur.fetchall()

		cur.execute("SELECT serial_c FROM tab_canaima_c WHERE serial_c = (%s)", (serial_c,))
		self.row3 = cur.fetchall()

		#se asigna nueva clave primara a la tabla tab_canaima_representante_cr
		cur.execute("SELECT id_cr FROM tab_canaima_representante_cr")
		self.row4 = cur.fetchall()
		self.row4 = str(self.row4).strip("[('',)]")
		id_cr = int(len(self.row4) + 1 )

		cur.close()
		con.close()

		#si los datos son encontrados...
		#si la cédula del representante existe en la base de datos...
		if len(self.row1) > 0:
			#si la cédula del alumno existe en la base de datos...
			if len(self.row2) > 0:
				#si el serial del equipo existe en la base de datos...
				if len(self.row3) > 0:
					#se inserta una nueva reparación
					con, cur = conexion_open(conexion2)
					self.pk_tab_reparacion_re()
					cur.close()
					con.close()
				#si el serial del equipo no existe en la base de datos se inserta un nuevo equipo al alumno
				else:
					con, cur = conexion_open(conexion2)
					cur.execute("INSERT INTO tab_canaima_c VALUES (%s, %s, %s, %s)", (serial_c, modelo_c, institucion_c, ci_n,))
					con.commit()
					cur.close()
					con.close()
					#se cierra la conexión y se vuelve a abrir para evitar problemas con las llaves foráneas
					con, cur = conexion_open(conexion2)
					self.pk_tab_reparacion_re()
					cur.close()
					con.close()
					#se cierra la conexión y se vuelve a abrir para evitar problemas con las llaves foráneas
					con, cur = conexion_open(conexion2)
					cur.execute("INSERT INTO tab_canaima_representante_cr VALUES (%s, %s, %s)", (id_cr, ci_r, serial_c,))
					con.commit()
					cur.close()
					con.close()

			#si la cédula del alumno no existe en la base de datos se inserta un nuevo alumno al representante
			else:
				try:
					con, cur = conexion_open(conexion2)
					cur.execute("INSERT INTO tab_nino_n VALUES (%s, %s, %s, %s, %s, %s)", (ci_n, nombre_n, plantel_n, nivel_n, municipio_n, ci_r,))
					cur.execute("INSERT INTO tab_canaima_c VALUES (%s, %s, %s, %s)", (serial_c, modelo_c, institucion_c, ci_n,))
					con.commit()
					cur.close()
					con.close()
					#se cierra la conexión y se vuelve a abrir para evitar problemas con las llaves foráneas
					con, cur = conexion_open(conexion2)
					self.pk_tab_reparacion_re()
					cur.close()
					con.close()

					con, cur = conexion_open(conexion2)
					cur.execute("INSERT INTO tab_canaima_representante_cr VALUES (%s, %s, %s)", (id_cr, ci_r, serial_c,))
					con.commit()
				except (IntegrityError, InternalError) as e:
					con.rollback()
					tkMessageBox.showinfo("postgresql", "El serial del equipo ya se encuentra registrado con otro alumno")
				finally:
					cur.close()
					con.close()
		#si no se encuentra ningún registro en la base de datos se insertan los nuevos datos
		else:
			try:
				con, cur = conexion_open(conexion2)
				cur.execute("INSERT INTO tab_representante_r VALUES (%s, %s, %s)", (ci_r, nombre_r, tlf_r,))
				cur.execute("INSERT INTO tab_nino_n VALUES (%s, %s, %s, %s, %s, %s)", (ci_n, nombre_n, plantel_n, nivel_n, municipio_n, ci_r,))
				cur.execute("INSERT INTO tab_canaima_c VALUES (%s, %s, %s, %s)", (serial_c, modelo_c, institucion_c, ci_n,))
				con.commit()
				cur.close()
				con.close()
				#se cierra la conexión y se vuelve a abrir para evitar problemas con las llaves foráneas
				con, cur = conexion_open(conexion2)
				self.pk_tab_reparacion_re()
				cur.close()
				con.close()

				con, cur = conexion_open(conexion2)
				cur.execute("INSERT INTO tab_canaima_representante_cr VALUES (%s, %s, %s)", (id_cr, ci_r, serial_c,))
				con.commit()

			except (IntegrityError, InternalError) as e:
				con.rollback()
				tkMessageBox.showinfo("postgresql", "El serial del equipo o la cédula del alumno se encuentran registrados")
			finally:
				cur.close()
				con.close()
	################################################## fin insertar ##################################################

	################################################## inicio modificar ##################################################
	def modificar(self):

		self.capturar()

		#si los datos son encontrados...
		#si la búsqueda se hizo por la cédula o el nombre del alumno
		if len(str(ci_n)) > 0 or len(str(nombre_n)) > 0 and len(str(ci_r)) == 0 and len(str(nombre_r)) == 0 and len(str(serial_c)) == 0:
			if len(nombre_n) == 0 or nombre_n.isspace() == True or len(plantel_n) == 0 or plantel_n.isspace() == True or len(nivel_n) == 0 or nivel_n.isspace() == True or len(nombre_r) == 0 or nombre_r.isspace() == True:
				tkMessageBox.showinfo("sistema-canaima", "Los campos marcados ""*"" son obligatorios")
			elif self.validar_nivel_n() and self.validar_municipio_n() and self.validar_tlf_r():
				con, cur = conexion_open(conexion2)
				cur.execute("UPDATE tab_representante_r SET nombre_r = (%s), tlf_r = (%s) WHERE ci_r = (%s)", (nombre_r, tlf_r, ci_r,))
				cur.execute("UPDATE tab_nino_n SET nombre_n = (%s), plantel_n = (%s), nivel_n = (%s), municipio_n = (%s) WHERE ci_n = (%s)", (nombre_n, plantel_n, nivel_n, municipio_n, ci_n,))
				#la búsqueda está hecha y los datos mostrados, por lo que es redundante validar
				cur.execute("SELECT id_re, serial_c FROM tab_reparacion_re WHERE serial_c = (%s) OR id_re = (%s)", (serial_c, serial_c))
				row_id_re = cur.fetchall()
				if len(row_id_re) > 0:
					if len(modelo_c) == 0 or modelo_c.isspace() == True or len(institucion_c) == 0 or institucion_c.isspace() == True or len(falla_re) == 0 or falla_re.isspace() == True or len(centro_re) == 0 or centro_re.isspace() == True:
						tkMessageBox.showinfo("sistema-canaima", "Los campos marcados ""*"" son obligatorios")
						return False
					elif self.validar_nivel_n() and self.validar_municipio_n() and self.validar_tlf_r() and self.validar_fec_re_re() and self.validar_fec_en_re():
						row_id_re2 = row_id_re[0][0] #id de la tabla reparación
						row_serial_c = row_id_re[0][1] #serial original del equipo que se usará para modificar el modelo y la institución (modelo_c, institucion_c) donde se entregó el equipo

						cur.execute("UPDATE tab_canaima_c SET modelo_c = (%s), institucion_c = (%s) WHERE serial_c = (%s)", (modelo_c, institucion_c, row_serial_c,))
						cur.execute("UPDATE tab_reparacion_re SET fec_re_re = (%s), fec_en_re = (%s), falla_re = (%s), act_re = (%s), reparada_re = (%s), entregada_re = (%s), cambio_re = (%s), centro_re = (%s) WHERE id_re = (%s)", (fec_re_re, fec_en_re, falla_re, act_re, reparada_re, entregada_re, cambio_re, centro_re, row_id_re2,))
						con.commit()
						cur.close()
						con.close()
						tkMessageBox.showinfo("postgresql", "Los datos se actualizaron con éxito")
						return True
					else:
						return False
				con.commit()
				cur.close()
				con.close()
				tkMessageBox.showinfo("postgresql", "Los datos se actualizaron con éxito")
				return True

		#si se busca la cédula o el nombre del representante
		elif len(str(ci_n)) == 0 and len(str(nombre_n)) == 0 and len(str(ci_r)) > 0 and len(str(nombre_r)) > 0 and len(str(serial_c)) == 0:
			if len(nombre_r) == 0 or nombre_r.isspace() == True:
				tkMessageBox.showinfo("sistema-canaima", "Los campos marcados ""*"" son obligatorios")
				return False

			elif self.validar_tlf_r():
				con, cur = conexion_open(conexion2)
				cur.execute("UPDATE tab_representante_r SET nombre_r = (%s), tlf_r = (%s) WHERE ci_r = (%s)", (nombre_r, tlf_r, ci_r,))
				con.commit()
				cur.close()
				con.close()

				tkMessageBox.showinfo("postgresql", "Los datos se actualizaron con éxito")
				return True
		else:
			if len(nombre_r) == 0 or nombre_r.isspace() == True:
				tkMessageBox.showinfo("sistema-canaima", "Los campos marcados ""*"" son obligatorios")
				return False
			else:
				tkMessageBox.showinfo("sistema-canaima", "Debe buscar una instancia a la vez")
				self.limpiar()
	################################################## fin modificar ##################################################

	################################################## inicio limpiar campos ##################################################
	def limpiar(self):
		#habilitar campos
		#habilitar datos del alumno
		self.ci_n_entry1.config(state = NORMAL)
		self.nombre_n_entry2.config(state = NORMAL)
		self.plantel_n_entry3.config(state = NORMAL)
		self.nivel_n_combobox1.config(state = NORMAL)
		self.municipio_n_combobox2.config(state = NORMAL)
		#habilitar datos del representante
		self.ci_r_entry6.config(state = NORMAL)
		#habilitar datos del equipo
		self.serial_c_entry9.config(state = NORMAL)
		self.modelo_c_entry10.config(state = NORMAL)
		self.institucion_c_entry11.config(state = NORMAL)
		#habilitar datos de la reparación
		self.fec_re_re_entry12.config(state = NORMAL)
		self.fec_en_re_entry13.config(state = NORMAL)
		self.falla_re_entry14.config(state = NORMAL)
		self.act_re_radio1.config(state = NORMAL)
		self.act_re_radio2.config(state = NORMAL)
		self.reparada_re_radio3.config(state = NORMAL)
		self.reparada_re_radio4.config(state = NORMAL)
		self.entregada_re_radio5.config(state = NORMAL)
		self.entregada_re_radio6.config(state = NORMAL)
		self.cambio_re_radio7.config(state = NORMAL)
		self.cambio_re_radio8.config(state = NORMAL)
		self.centro_re_entry15.config(state = NORMAL)
		#restaurar campos
		#restaurar campos del alumno
		self.ci_n_entry1.delete(0, "end")
		self.nombre_n_entry2.delete(0, "end")
		self.plantel_n_entry3.delete(0, "end")
		self.nivel_n_combobox1.delete(0, "end")
		self.municipio_n_combobox2.delete(0, "end")
		#restaurar campos del representante
		#datos del representante
		self.ci_r_entry6.delete(0, "end")
		self.nombre_r_entry7.delete(0, "end")
		self.tlf_r_entry8.delete(0, "end")
		#restaurar cmpos del equipo
		self.serial_c_entry9.delete(0, "end")
		self.modelo_c_entry10.delete(0, "end")
		self.institucion_c_entry11.delete(0, "end")
		#restaurar campos de la reparación
		self.fec_re_re_entry12.delete(0, "end")
		self.fec_en_re_entry13.delete(0, "end")
		self.falla_re_entry14.delete(0, "end")
		self.centro_re_entry15.delete(0, "end")
		self.centro_re_entry15.insert(0, "COORDINACION CBIT")
	################################################## fin limpiar campos ##################################################

	#bloquear campos de la reparación
	def disable_reparacion(self):
		self.fec_re_re_entry12.config(state = DISABLED)
		self.fec_en_re_entry13.config(state = DISABLED)
		self.falla_re_entry14.config(state = DISABLED)
		self.act_re_radio1.config(state = DISABLED)
		self.act_re_radio2.config(state = DISABLED)
		self.reparada_re_radio3.config(state = DISABLED)
		self.reparada_re_radio4.config(state = DISABLED)
		self.entregada_re_radio5.config(state = DISABLED)
		self.entregada_re_radio6.config(state = DISABLED)
		self.cambio_re_radio7.config(state = DISABLED)
		self.cambio_re_radio8.config(state = DISABLED)
		self.centro_re_entry15.config(state = DISABLED)

	################################################## inicio buscar datos ##################################################
	def buscar(self):
		self.capturar()
		self.limpiar()

		#si se buscar por el número de cédula del alumno se muestran los datos del alumno y representante
		if len(str(ci_n)) > 0 and len(str(nombre_n)) == 0 and len(str(ci_r)) == 0 and len(str(nombre_r)) == 0 and len(str(serial_c)) == 0:
			try:
				con, cur = conexion_open(conexion2)
				#cédula del alumno
				cur.execute("SELECT ci_n FROM tab_nino_n WHERE ci_n = (%s)", (ci_n,))
				row_ci_n = cur.fetchall()
			except (DataError, UnicodeEncodeError) as e:
				tkMessageBox.showinfo("sistema-canaima", "Ingrese correctamente el número de cédula")
			finally:
				cur.close()
				con.close()

			#si existe el alumno en la base de datos
			if len(row_ci_n) == 1:
				#se muestran los datos del alumno y representante
				con, cur = conexion_open(conexion2)
				#datos del alumno
				cur.execute("SELECT ci_n, nombre_n, plantel_n, nivel_n, municipio_n, ci_r FROM tab_nino_n WHERE ci_n = (%s)", (ci_n,))
				row_datos_n = cur.fetchall()
				#datos del representante
				cur.execute("SELECT nombre_r, tlf_r FROM tab_representante_r WHERE ci_r = (%s)", (row_datos_n[0][5],))
				row_datos_r = cur.fetchall()
				cur.close()
				con.close()

				self.ci_n_entry1.insert(0, row_datos_n[0][0])
				self.nombre_n_entry2.insert(0, row_datos_n[0][1])
				self.plantel_n_entry3.insert(0, row_datos_n[0][2])
				self.nivel_n_combobox1.set(row_datos_n[0][3])
				self.municipio_n_combobox2.set(row_datos_n[0][4])
				self.ci_r_entry6.insert(0, row_datos_n[0][5])
				self.nombre_r_entry7.insert(0, row_datos_r[0][0])
				self.tlf_r_entry8.insert(0, row_datos_r[0][1])

				#se crea una lista con los equipos de ese alumno
				lista1 = Tk()
				lista1.title("Equipos pertenecientes al alumno")
				listbox1 = Listbox(lista1, width = "50")
				listbox1.pack()

				#se llena la lista con los equipos
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT serial_c FROM tab_canaima_c WHERE ci_n = (%s)", (ci_n,))
				row_seriales_n = cur.fetchall()
				cur.close()
				con.close()

				for i in row_seriales_n:
					contador1 = 0
					contador1 = contador1 + 1
					contador2 = int(row_seriales_n.index(i)) + 1
					listbox1.insert(contador1 + 1, row_seriales_n[contador2 - 1])
			else:
				self.limpiar()
				tkMessageBox.showinfo("postgresql", "El número de cédula del alumno no se encuentra registrado")

			#se omiten los demás datos
			#datos del alumno
			self.ci_n_entry1.config(state = DISABLED)
			#datos del representante
			self.ci_r_entry6.config(state = DISABLED)
			#datos del equipo
			self.serial_c_entry9.config(state = DISABLED)
			self.modelo_c_entry10.config(state = DISABLED)
			self.institucion_c_entry11.config(state = DISABLED)
			#datos de la raparación
			self.disable_reparacion()

		#si se busca por el nombre del alumno se muestran los datos del alumno y representante
		elif len(str(ci_n)) == 0 and len(str(nombre_n)) > 0 and len(str(ci_r)) == 0 and len(str(nombre_r)) == 0 and len(str(serial_c)) == 0:
			con, cur = conexion_open(conexion2)
			#nombre del alumno
			cur.execute("SELECT nombre_n FROM tab_nino_n WHERE nombre_n = (%s)", (nombre_n,))
			row_nombre_n = cur.fetchall()
			cur.close()
			con.close()

			#si no existe el alumno en la base de datos
			if len(row_nombre_n) == 0:
				tkMessageBox.showinfo("postgresql", "El nombre del alumno no se encuentra registrado")
			#si existe el alumno en la base de datos
			elif len(row_nombre_n) == 1:
				#se muestran los datos del alumno y representante
				con, cur = conexion_open(conexion2)
				#datos del alumno
				cur.execute("SELECT ci_n, nombre_n, plantel_n, nivel_n, municipio_n, ci_r FROM tab_nino_n WHERE nombre_n = (%s)", (nombre_n,))
				row_datos_n = cur.fetchall()
				#datos del representante
				cur.execute("SELECT nombre_r, tlf_r FROM tab_representante_r WHERE ci_r = (%s)", (row_datos_n[0][5],))
				row_datos_r = cur.fetchall()
				cur.close()
				con.close()

				self.ci_n_entry1.insert(0, row_datos_n[0][0])
				self.nombre_n_entry2.insert(0, row_datos_n[0][1])
				self.plantel_n_entry3.insert(0, row_datos_n[0][2])
				self.nivel_n_combobox1.set(row_datos_n[0][3])
				self.municipio_n_combobox2.set(row_datos_n[0][4])
				self.ci_r_entry6.insert(0, row_datos_n[0][5])
				self.nombre_r_entry7.insert(0, row_datos_r[0][0])
				self.tlf_r_entry8.insert(0, row_datos_r[0][1])

				#se crea una lista con los equipos de ese alumno
				lista2 = Tk()
				lista2.title("Equipos pertenecientes al alumno")
				listbox2 = Listbox(lista2, width = "50")
				listbox2.pack()

				#se llena la lista con los equipos
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT serial_c FROM tab_canaima_c WHERE ci_n = (%s)", (row_datos_n[0][0],))
				row_seriales_n = cur.fetchall()
				cur.close()
				con.close()

				for i in row_seriales_n:
					contador1 = 0
					contador1 = contador1 + 1
					contador2 = int(row_seriales_n.index(i)) + 1
					listbox2.insert(contador1 + 1, row_seriales_n[contador2 - 1])
			else:
				tkMessageBox.showinfo("postgresql", "Existen varios registros con este mismo nombre")
				self.limpiar()

			#se omiten los demás datos
			#datos del alumno
			self.ci_n_entry1.config(state = DISABLED)
			#datos del representante
			self.ci_r_entry6.config(state = DISABLED)
			#datos del equipo
			self.serial_c_entry9.config(state = DISABLED)
			self.modelo_c_entry10.config(state = DISABLED)
			self.institucion_c_entry11.config(state = DISABLED)
			#datos de la raparación
			self.disable_reparacion()

		#si se busca por el número de cédula del representante se muestran los datos del representante
		elif len(str(ci_n)) == 0 and len(str(nombre_n)) == 0 and len(str(ci_r)) > 0 and len(str(nombre_r)) == 0 and len(str(serial_c)) == 0:
			try:
				con, cur = conexion_open(conexion2)
				#cédula del representante
				cur.execute("SELECT ci_r FROM tab_representante_r WHERE ci_r = (%s)", (ci_r,))
				row_ci_r = cur.fetchall()
			except (DataError, UnicodeEncodeError) as e:
				tkMessageBox.showinfo("sistema-canaima", "Ingrese correctamente el número de cédula")
			finally:
				cur.close()
				con.close()

			#si existe el representante en la base de datos
			if len(row_ci_r) == 1:
				#se muestran los datos del representante
				con, cur = conexion_open(conexion2)
				#datos del representante
				cur.execute("SELECT ci_r, nombre_r, tlf_r FROM tab_representante_r WHERE ci_r = (%s)", (ci_r,))
				row_datos_r = cur.fetchall()
				cur.close()
				con.close()

				self.ci_r_entry6.insert(0, row_datos_r[0][0])
				self.nombre_r_entry7.insert(0, row_datos_r[0][1])
				self.tlf_r_entry8.insert(0, row_datos_r[0][2])

				#se crea una lista con los equipos cuyo responsable es el representante
				lista3 = Tk()
				lista3.title("Equipos pertenecientes al representante")
				listbox3 = Listbox(lista3, width = "50")
				listbox3.pack()

				#se llena la lista con los equipos
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT serial_c FROM tab_canaima_representante_cr WHERE ci_r = (%s)", (ci_r,))
				row_seriales_cr = cur.fetchall()
				cur.close()
				con.close()

				for i in row_seriales_cr:
					contador1 = 0
					contador1 = contador1 + 1
					contador2 = int(row_seriales_cr.index(i)) + 1
					listbox3.insert(contador1 + 1, row_seriales_cr[contador2 - 1])
			else:
				tkMessageBox.showinfo("postgresql", "El número de cédula del representante no se encuentra registrado")
				self.limpiar()

			#se omiten los demás datos
			#datos del alumno
			self.ci_n_entry1.config(state = DISABLED)
			self.nombre_n_entry2.config(state = DISABLED)
			self.plantel_n_entry3.config(state = DISABLED)
			self.nivel_n_combobox1.config(state = DISABLED)
			self.municipio_n_combobox2.config(state = DISABLED)
			#datos del representante
			self.ci_r_entry6.config(state = DISABLED)
			#datos del equipo
			self.serial_c_entry9.config(state = DISABLED)
			self.modelo_c_entry10.config(state = DISABLED)
			self.institucion_c_entry11.config(state = DISABLED)
			#datos de la raparación
			self.disable_reparacion()

		#si se busca por el nombre del representante se muestran los datos del representante
		elif len(str(ci_n)) == 0 and len(str(nombre_n)) == 0 and len(str(ci_r)) == 0 and len(str(nombre_r)) > 0 and len(str(serial_c)) == 0:
			con, cur = conexion_open(conexion2)
			#nombre del representante
			cur.execute("SELECT nombre_r FROM tab_representante_r WHERE nombre_r = (%s)", (nombre_r,))
			row_nombre_r = cur.fetchall()
			cur.close()
			con.close()

			#si no existe el representante en la base de datos
			if len(row_nombre_r) == 0:
				tkMessageBox.showinfo("postgresql", "El nombre del representante no se encuentra registrado")
			#si existe el representante en la base de datos
			elif len(row_nombre_r) == 1:
				#se muestran los datos del representante
				con, cur = conexion_open(conexion2)
				#datos del representante
				cur.execute("SELECT ci_r, nombre_r, tlf_r FROM tab_representante_r WHERE nombre_r = (%s)", (nombre_r,))
				row_datos_r = cur.fetchall()
				cur.close()
				con.close()

				self.ci_r_entry6.insert(0, row_datos_r[0][0])
				self.nombre_r_entry7.insert(0, row_datos_r[0][1])
				self.tlf_r_entry8.insert(0, row_datos_r[0][2])

				#se crea una lista con los equipos cuyo responsable es el representante
				lista4 = Tk()
				lista4.title("Equipos pertenecientes al representante")
				listbox4 = Listbox(lista4, width = "50")
				listbox4.pack()

				#se llena la lista con los equipos
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT serial_c FROM tab_canaima_representante_cr WHERE ci_r = (%s)", (row_datos_r[0][0],))
				row_seriales_cr = cur.fetchall()
				cur.close()
				con.close()

				for i in row_seriales_cr:
					contador1 = 0
					contador1 = contador1 + 1
					contador2 = int(row_seriales_cr.index(i)) + 1
					listbox4.insert(contador1 + 1, row_seriales_cr[contador2 - 1])
			else:
				tkMessageBox.showinfo("postgresql", "Existen varios registros con este mismo nombre")
				self.limpiar()

			#se omiten los demás datos
			#datos del alumno
			self.ci_n_entry1.config(state = DISABLED)
			self.nombre_n_entry2.config(state = DISABLED)
			self.plantel_n_entry3.config(state = DISABLED)
			self.nivel_n_combobox1.config(state = DISABLED)
			self.municipio_n_combobox2.config(state = DISABLED)
			#datos del representante
			self.ci_r_entry6.config(state = DISABLED)
			#datos del equipo
			self.serial_c_entry9.config(state = DISABLED)
			self.modelo_c_entry10.config(state = DISABLED)
			self.institucion_c_entry11.config(state = DISABLED)
			#datos de la raparación
			self.disable_reparacion()

		#si se busca por el serial del equipo se muestran todos los datos
		elif len(str(ci_n)) == 0 and len(str(nombre_n)) == 0 and len(str(ci_r)) == 0 and len(str(nombre_r)) == 0 and len(str(serial_c)) > 0:
			self.centro_re_entry15.delete(0, "end")

			con, cur = conexion_open(conexion2)
			#serial del equipo
			cur.execute("SELECT serial_c FROM tab_canaima_c WHERE serial_c = (%s)", (serial_c,))
			row_serial_c = cur.fetchall()
			#id de la reparación
			cur.execute("SELECT id_re FROM tab_reparacion_re WHERE serial_c = (%s)", (serial_c,))
			row_id_re = cur.fetchall()
			cur.execute("SELECT id_re FROM tab_reparacion_re WHERE id_re = (%s)", (serial_c,))
			row_id_re2 = cur.fetchall()#variable que guarda todas las reparaciones de un mismo serial
			cur.close()
			con.close()

			#si existe el serial en la base de datos
			if len(row_serial_c) == 1 and len(row_id_re) >= 1:
				self.limpiar()
				lista = Tk()
				lista.title("Reparaciones registradas")
				listbox1 = Listbox(lista, width = "50")
				listbox1.pack()

				#se llena la lista con las reparaciones encontradas
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT id_re FROM tab_reparacion_re WHERE serial_c = (%s)", (serial_c,))
				row_id_re = cur.fetchall()
				cur.close()
				con.close()
				
				for i in row_id_re:
					contador1 = 0
					contador1 = contador1 + 1
					contador2 = int(row_id_re.index(i)) + 1
					listbox1.insert(contador1 + 1, row_id_re[contador2 - 1])

			#si existe la reparación en la base de datos
			elif len(row_id_re2) == 1:
				con, cur = conexion_open(conexion2)
				cur.execute("SELECT serial_c FROM tab_reparacion_re WHERE id_re = (%s)", (serial_c,))
				row_serial_c2 = cur.fetchall()
				cur.close()
				con.close()

				#se muestran todos los datos
				con, cur = conexion_open(conexion2)
				#cédula del alumno
				cur.execute("SELECT ci_n FROM tab_canaima_c WHERE serial_c = (%s)", (row_serial_c2[0][0],))
				row_ci_n = cur.fetchall()
				#datos del alumno
				cur.execute("SELECT nombre_n, plantel_n, nivel_n, municipio_n FROM tab_nino_n WHERE ci_n = (%s)", (row_ci_n[0][0],))
				row_datos_n = cur.fetchall()
				#cédula del representante
				cur.execute("SELECT ci_r FROM tab_canaima_representante_cr WHERE serial_c = (%s)", (row_serial_c2[0][0],))
				row_ci_r = cur.fetchall()
				#datos del representante
				cur.execute("SELECT nombre_r, tlf_r FROM tab_representante_r WHERE ci_r = (%s)", (row_ci_r[0][0],))
				row_datos_r = cur.fetchall()
				#datos del equipo
				cur.execute("SELECT serial_c, modelo_c, institucion_c FROM tab_canaima_c WHERE serial_c = (%s)", (row_serial_c2[0][0],))
				row_datos_c = cur.fetchall()
				#datos de la reparación
				cur.execute("SELECT fec_re_re, fec_en_re, falla_re, act_re, reparada_re, entregada_re, cambio_re, centro_re FROM tab_reparacion_re WHERE id_re = (%s)", (serial_c,))
				row_datos_re = cur.fetchall()
				cur.close()
				con.close()

				self.ci_n_entry1.insert(0, row_ci_n[0][0])
				self.nombre_n_entry2.insert(0, row_datos_n[0][0])
				self.plantel_n_entry3.insert(0, row_datos_n[0][1])
				self.nivel_n_combobox1.set(row_datos_n[0][2])
				self.municipio_n_combobox2.set(row_datos_n[0][3])
				self.ci_r_entry6.insert(0, row_ci_r[0][0])
				self.nombre_r_entry7.insert(0, row_datos_r[0][0])
				self.tlf_r_entry8.insert(0, row_datos_r[0][1])
				self.serial_c_entry9.insert(0, row_id_re2[0][0])
				self.modelo_c_entry10.insert(0, row_datos_c[0][1])
				self.institucion_c_entry11.insert(0, row_datos_c[0][2])
				self.fec_re_re_entry12.insert(0, row_datos_re[0][0])
				self.fec_en_re_entry13.insert(0, row_datos_re[0][1])
				self.falla_re_entry14.insert(0, row_datos_re[0][2])
				if int(row_datos_re[0][3]) == 1:
					self.act_re_radio1.select()
				else:
					self.act_re_radio2.select()
				if int(row_datos_re[0][4]) == 1:
					self.reparada_re_radio3.select()
				else:
					self.reparada_re_radio4.select()
				if int(row_datos_re[0][5]) == 1:
					self.entregada_re_radio5.select()
				else:
					self.entregada_re_radio6.select()
				if int(row_datos_re[0][6]) == 1:
					self.cambio_re_radio7.select()
				else:
					self.cambio_re_radio8.select()
				self.centro_re_entry15.insert(0, row_datos_re[0][7])

				#datos del alumno
				self.ci_n_entry1.config(state = DISABLED)
				#datos del representante
				self.ci_r_entry6.config(state = DISABLED)
				#datos del equipo
				self.serial_c_entry9.config(state = DISABLED)
			else:
				tkMessageBox.showinfo("postgresql", "El equipo no se encuentra registrado")

		#si se buscan varios argumentos a la vez
		else:
			tkMessageBox.showinfo("sistema-canaima", "Debe buscar una instancia a la vez")
			self.limpiar()
	################################################## fin buscar datos ##################################################

	################################################## inicio validaciones ##################################################

	#validar_vacio
	def validar_vacio(self):

		self.capturar()

		if len(nombre_n) == 0 or nombre_n.isspace() == True or len(plantel_n) == 0 or plantel_n.isspace() == True or len(nivel_n) == 0 or nivel_n.isspace() == True or len(nombre_r) == 0 or nombre_r.isspace() == True or len(modelo_c) == 0 or modelo_c.isspace() == True or len(falla_re) == 0 or falla_re.isspace() == True or len(centro_re) == 0 or centro_re.isspace() == True:
			tkMessageBox.showinfo("__sistema_canaima__", "Los campos marcados ""*"" son obligatorios")
			return False
		else:
			return True

	#validar_numero
	def validar_numero(self):

		self.capturar()

		if ci_n.isdigit() != True or ci_r.isdigit() != True:
			tkMessageBox.showinfo("sistema-canaima", "Debe ingresar sólo números:\n*Cédula del alumno\n*Cédula del representante")
			return False
		else:
			return True

	#validar_letra
	def validar_letra(self):

		self.capturar()

		nombre_n_letra = nombre_n.strip(" ")
		nombre_r_letra = nombre_r.strip(" ")
		nombre_n_letra = nombre_n_letra.replace(' ', '')
		nombre_r_letra = nombre_r_letra.replace(' ', '')
		if nombre_n_letra.isalpha() != True or nombre_r_letra.isalpha() != True:
			tkMessageBox.showinfo("sistema-canaima", "Debe ingresar sólo letras:\n*Nombre del alumno\n*Nombre del representante")
			return False
		else:
			return True

	#validar_nivel_n
	def validar_nivel_n(self):

		self.capturar()

		lista_niveles = ["1ERGRADO", "2DOGRADO", "3ERGRADO", "4TOGRADO", "5TOGRADO", "6TOGRADO", "1ERANO", "2DOANO", "3ERANO", "4TOANO", "5TOANO", "6TOANO"]

		if nivel_n not in lista_niveles:
			tkMessageBox.showinfo("sistema-canaima", "Ingrese correctamente el nivel académico del alumno")
			return False
		else:
			return True

	#validar_municipio_n
	def validar_municipio_n(self):

		self.capturar()

		lista_municipios = ["ARISMENDI", "DIAZ", "MARCANO", "TUBORES", "PENINSULA DE MACANAO", "GARCIA", "MARINO", "MANEIRO", "ANTOLIN DEL CAMPO", "VILLALBA", "GOMEZ"]

		if municipio_n not in lista_municipios:
			tkMessageBox.showinfo("sistema-canaima", "El municipio no existe")
			return False
		else:
			return True

	#validar_tlf_r
	def validar_tlf_r(self):

		self.capturar()

		if (len(tlf_r) == 11 and tlf_r.isdigit() == True) or tlf_r == "SIN TELEFONO":
			return True
		else:
			tkMessageBox.showinfo("sistema-canaima", "El número de teléfono debe contener 11 caracteres numéricos.\nO en su defecto: SIN TELEFONO")
			return False

	#validar_serial_modelo
	def validar_serial_modelo(self):

		self.capturar()

		if serial_c.isalnum() == True and len(serial_c) <= 25 and len(modelo_c) <= 20:
			return True
		else:
			tkMessageBox.showinfo("sistema-canaima", "El serial y el modelo del equipo debe contener no más de 25 caracteres alfanuméricos")
			return False

	#validar_fec_re_re. Formato de fecha: 2006-06-06, año-mes-día
	def validar_fec_re_re(self):

		self.capturar()

		lista_dias = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
		lista_meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

		if len(fec_re_re) == 10 and fec_re_re[0:4].isdigit() == True and fec_re_re[4] == "-" and fec_re_re[5:7] in lista_meses != True and fec_re_re[7] == "-" and fec_re_re[8:10] in lista_dias != True:
			return True
		else:
			tkMessageBox.showinfo("sistema-canaima", "La fecha debe contener el siguiente formato aaaa-mm-dd")
			return False

	#validar_fec_en_re. Formato de fecha: 2006-06-06, año-mes-día
	def validar_fec_en_re(self):

		self.capturar()

		lista_dias = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
		lista_meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

		if len(fec_en_re) == 10 and fec_en_re[0:4].isdigit() == True and fec_en_re[4] == "-" and fec_en_re[5:7] in lista_meses != True and fec_en_re[7] == "-" and fec_en_re[8:10] in lista_dias != True:
				return True
		elif len(fec_en_re) == 0:
				return True
		else:
			tkMessageBox.showinfo("sistema-canaima", "La fecha debe contener el siguiente formato aaaa-mm-dd")
			return False

	#funcion que agrupa las validaciones

	def validar_insert(self):

		if self.validar_vacio() and self.validar_numero() and self.validar_letra() and self.validar_nivel_n() and self.validar_municipio_n() and self.validar_tlf_r() and self.validar_serial_modelo() and self.validar_fec_re_re() and self.validar_fec_en_re():
			self.insertar()
			return True
		else:
			return False

	################################################## fin validaciones ##################################################

################################################## fin class Formulario ##################################################
app = Formulario(), Appselect()
app[0].root.mainloop()

"""if __name__ == "__main__":
	#ventana principal
	root = Tk()
	#root.config(bg = "grey")
	root.geometry("740x320")
	root.title("sistema-canaima")

	app = Formulario(root)
	root.mainloop()"""

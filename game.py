""" @author: Alvaro Velasco	Date: 10 Mayo 2016 """

import gtk
from random import randint

# DEFINITIONS

def apretado_undo(boton):
	if undo == 1:
		but_undo.set_label("Puedes deshacer %s vez mas" % undo)
	else:
		but_undo.set_label("Puedes deshacer %s veces mas" % undo)

def change_color():
	for x in range(0, TAM):
		for y in range (0, TAM):
			i = x+TAM*y
			boton = botones[i]
			boton.posicion = (x, y)
			if tablero[x][y] == 0:
				change_black(boton)
			else:
				change_blue(boton)

def change_btr(boton):
	image_btr = gtk.Image()
	image_btr.set_from_file("images/btr.gif")
	boton.set_image(image_btr)

def change_rtb(boton):
	image_rtb = gtk.Image()
	image_rtb.set_from_file("images/rtb.gif")
	boton.set_image(image_rtb)

def change_blue(boton):
	image_blue = gtk.Image()
	image_blue.set_from_file("images/blue.png")
	boton.set_image(image_blue)

def change_black(boton):
	image_black = gtk.Image()
	image_black.set_from_file("images/black.png")
	boton.set_image(image_black)

def change_red(boton):
	image_red = gtk.Image()
	image_red.set_from_file("images/red.png")
	boton.set_image(image_red)

def change_green(boton):
	image_green = gtk.Image()
	image_green.set_from_file("images/green.gif")
	boton.set_image(image_green)

def change_gold(boton):
	image_gold = gtk.Image()
	image_gold.set_from_file("images/gold.png")
	boton.set_image(image_gold)

def change_silver(boton):
	image_silver = gtk.Image()
	image_silver.set_from_file("images/silver.png")
	boton.set_image(image_silver)

def change_white(boton):
	image_white = gtk.Image()
	image_white.set_from_file("images/white.png")
	boton.set_image(image_white)

def change_level(boton):
	global level, hits, tablero, undo, WarSecINFO
	try:
		level = int(tbox_level.get_text())
		hits = 0
		undo = 0
		recoverhighscore()
		while len(high_score) <= level:
			high_score.append('SinPuntuacion')
		golpes_txt.set_label("Llevas %s golpes" % (hits))
		record_txt.set_label("Nivel: %s    Record: %s" % (level, high_score[level-1]))
		tablero_level(boton)
		but_reboot.set_sensitive(True)
		but_undo.set_sensitive(False)
		firma.set_visible(False)
		record_table.set_visible(False)
	except ValueError:
		tbox_level.set_text("Nivel con NUMERO")

def change_board(boton):
	global tablero
	(x, y) = boton.posicion
	for i in range(-1, 2):
		if tablero[x-2][y+i] == 0:
			tablero[x-2][y+i] = 1
		else:
			tablero[x-2][y+i] = 0
		if tablero[x + 2][y + i] == 0:
			tablero[x +2][y + i] = 1
		else:
			tablero[x +2][y + i] = 0
	for i in range(-2, 3):
		if tablero[x-1][y+i] == 0:
			tablero[x-1][y+i] = 1
		else:
			tablero[x-1][y+i] = 0
		if tablero[x][y+i] == 0:
			tablero[x][y+i] = 1
		else:
			tablero[x][y+i] = 0
		if tablero[x+1][y+i] == 0:
			tablero[x+1][y+i] = 1
		else:
			tablero[x+1][y+i] = 0
	change_color()

def changehighscore():
	global level, high_score, hits, undo
	k = -1
	for l in range(0, len(high_score)):
		if high_score[l] != 'SinPuntuacion':
			high_score[l] = int(high_score[l])
		else:
			high_score[l] = 'SinPuntuacion'
	while len(high_score) < level:  # Writing that it has levels without score
		high_score.append('SinPuntuacion')
	if high_score[(level + k)] == "SinPuntuacion":
		high_score[(level + k)] = hits
		tbox_level.set_text('Siuuh!')
		record_txt.set_text('GOLPES: %s    NIVEL: %s' % (hits, level))
		golpes_txt.set_text('Eres el primero en jugar!')
		index_interface(index_yes)
	elif high_score[(level + k)] > hits:
		tbox_level.set_text('Siuuh!')
		record_txt.set_text('GOLPES: %s    NIVEL: %s' % (hits, level))
		golpes_txt.set_text('N U E V O   R E C O R D')
		high_score[(level + k)] = hits
		index_interface(index_oro)
	elif high_score[(level + k)] == hits:
		tbox_level.set_text('Siuuh!')
		record_txt.set_text('GOLPES: %s    NIVEL: %s' % (hits, level))
		golpes_txt.set_text('Igualas el record !')
		index_interface(index_plata)
	else:
		tbox_level.set_text('Siuuh!')
		record_txt.set_text('GOLPES: %s    RECORD: %s' % (hits, high_score[(level + k)]))
		golpes_txt.set_text('Nivel %s terminado' % level)
		index_interface(index_ok)
	but_reboot.set_sensitive(False)
	ch = False  # Saving
	while ch == False:
		try:
			a = open(file_name, 'w')
			for l in range(0, len(high_score)):
				a.writelines(str(high_score[l]) + "\n")
			ch = True
		except IOError:
			print 'Vaya, ha ocurrido un error mientras guardabamos las puntuaciones...'
	hits = 0
	level = 0
	undo = 0

def checkend():
	global tablero, checkit, high_score
	if level != 0:
		checkit = 0
		for r in range(0, TAM):
			for c in range(0, TAM):
				if tablero[c][r] == 1:
					checkit += 1
		if checkit == 0:
			but_left.set_sensitive(False)
			but_undo.set_sensitive(False)
			but_reboot.set_sensitive(False)
			changehighscore()
			print_hs()

def close_all(ventana):
	gtk.main_quit

def funct_left(boton):
	global level
	level -= 1
	tbox_level.set_text("%s" % level)
	but_left.set_sensitive(True)
	if level <= 1:
		but_left.set_sensitive(False)

def funct_right(boton):
	global level, botones
	level += 1
	tbox_level.set_text("%s" % level)
	but_left.set_sensitive(True)
	if level <= 1:
		but_left.set_sensitive(False)

def index_interface(index):  # CHANGE THE BUTTONS COLORS DEPENDING THE GAME
	for i in range(0, TAM2):
		b = botones[i]
		if index[i] == 0: change_black(b)
		elif index[i] == 1: change_red(b)
		elif index[i] == 2: change_gold(b)
		elif index[i] == 3: change_white(b)
		elif index[i] == 4: change_green(b)
		elif index[i] == 5: change_silver(b)
		elif index[i] == 6: change_blue(b)
		elif index[i] == 7: change_btr(b)
		elif index[i] == 8: change_rtb(b)

def less_undo(boton):  # Go to the before step
	global undo
	undo -= 1
	x = memraw[undo]
	y = memcol[undo]
	boton.posicion = (x, y)
	if undo <= 0:
		but_undo.set_sensitive(False)
		but_undo.set_label("No puedes deshacer")
	if undo >= 0:	
		change_board(boton)
def more_undo(boton):  # saving the hit to undo later
	global undo, hits
	but_undo.set_sensitive(True)
	but_undo.set_label("DESHACER JUGADA")
	(x,y) = boton.posicion
	memraw[undo] = x
	memraw.append(0)
	memcol[undo] = y
	memcol.append(0)
	undo += 1
	hits += 1
	golpes_txt.set_label("Llevas %s golpes" % (hits))
	record_txt.set_label("Nivel: %s    Record: %s" % (level, high_score[level-1]))
	if level == 0:
		golpes_txt.set_label("Seleccione un nivel")
		record_txt.set_label("Esta en modo prueba")
	checkend()

def new_board():  # To make a new simple board
	tablero = [0] * (TAM+4)
	for i in range(0, TAM+4):
		tablero[i] = [0] * (TAM+5)
	return tablero

def recoverhighscore():
	global high_score
	ch = False
	while ch == False:  # Abrimos el fichero en 'a' para copiarlo en 'High score'
		try:
			file = open(file_name, 'r')
			ch = True
		except IOError:
			filenew = open(file_name, 'w')
			filenew.write("SinPuntuacion")
			filenew.close()
	high_score = file.read()
	high_score = high_score.split()
	file.close()  # Cerramos el fichero

def copy_array(tab):
	arr = new_board()
	for i in range(0, len(tab)):
		for j in range(0, len(tab)):
			arr[i][j] = tab[i][j]
	return arr

def soltado_undo(boton):
	but_undo.set_label("CLICK PARA DESHACER")

def tablero_level(boton):
	global tablero, undo, level, recomenzar
	tablero = new_board()
	for b in range (0, level):
		x = randint(0, TAM-1)
		y = randint(0, TAM-1)
		boton.posicion = (x, y)
		change_board(boton)
	recomenzar = copy_array(tablero)
	undo = 0

def recomienza(boton):
	global tablero, recomenzar, undo, hits
	tablero = copy_array(recomenzar)
	golpes_txt.set_text("Vuelve a empezar!")
	hits = 0
	undo = 0
	but_undo.set_sensitive(False)
	change_color()

def print_hs():  # change te highscores showned
	global punt_text, high_score
	punt_text = "\n\n\n\n\n\n\n"
	recoverhighscore()
	mark = 0
	for i in range (0, len(high_score) - 1):
		if str(high_score[i]) != "SinPuntuacion":
			mark = 1
			punt_text += "\tNivel "
			punt_text += str(i+1)
			punt_text += " - "
			punt_text += str(high_score[i])
			punt_text += " golpes\t\n"
	if mark == 0: punt_text += "\nNo hay records almacenados\n"
	puntuaciones.set_text(punt_text)

def hs_on(boton):  # SHOW / QUIT HIGH SCORES
	global WarSecHS
	if WarSecHS == 0:
		supertable.attach(record_table, 1, 2, 0, 1)
		record_table.attach(puntuaciones, 0, 1, 0, 1)
		record_table.attach(records_image, 0, 1, 0, 1)
		supertable.attach(firma, 1, 2, 1, 2)
		firma.set_visible(True)
		records_image.set_visible(True)
		puntuaciones.set_visible(True)
		WarSecHS = 1
	if record_table.get_visible():
		record_table.set_visible(False)
		firma.set_visible(False)
	else: record_table.set_visible(True); firma.set_visible(True)

def info_on(boton):  # SHOW / QUIT TUTORIAL
	global WarSecINFO, botones, image_tutorial
	if WarSecINFO == 0:
		for b in botones:
			b.set_visible(False)
		tabla.attach(image_tutorial, 0, 10, 0, 10)
		WarSecINFO = 1
	if image_tutorial.get_visible():
		image_tutorial.set_visible(False)
		for b in botones:
			b.set_visible(True)
	else:
		for b in botones:
			b.set_visible(False)
		image_tutorial.set_visible(True)

# CODE

TAM = 10
TAM2 = TAM*TAM
file_name = "HS.txt"
memraw = [0]
memcol = [0]
undo = 0
hits = 0
high_score = []
level = 0
recoverhighscore()
botones = []
tablero = new_board()
recomenzar = new_board()
WarSecHS = 0  # Avoid a warning
WarSecINFO = 0  # avoid a warning

color_gris = gtk.gdk.color_parse('#151515')  # Use to background

ventana = gtk.Window()
centro = gtk.WIN_POS_CENTER


tbox_level = gtk.Entry()  # Textbox to set a level
tbox_level.set_text("?")
tbox_level.set_alignment(0.5)
tbox_level.set_width_chars(5)

but_level= gtk.Button()  # Button to change te level
but_level.set_label("Cambiar nivel!")

but_left = gtk.Button()  # button to decrease level
image_left = gtk.Image()
image_left.set_from_file("images/left.png")
but_left.set_image(image_left)
but_left.set_relief(gtk.RELIEF_NONE)
but_left.set_sensitive(False)

but_right = gtk.Button()  # button to increase level
image_right = gtk.Image()
image_right.set_from_file("images/right.png")
but_right.set_image(image_right)
but_right.set_relief(gtk.RELIEF_NONE)

but_undo = gtk.Button()  # button to undo the hit
but_undo.set_label("DESHACER!")

but_reboot = gtk.Button()  # Button to restart game
image_reboot = gtk.Image()
image_reboot.set_from_file("images/reboot.png")
but_reboot.set_image(image_reboot)
but_reboot.set_sensitive(False)

but_info = gtk.Button()  # Info button
image_info = gtk.Image()
image_info.set_from_file("images/info.png")
but_info.set_image(image_info)

but_hs = gtk.Button()  # Show high scores
image_hs = gtk.Image()
image_hs.set_from_file("images/punt.png")
but_hs.set_image(image_hs)

image_tutorial = gtk.Image()  # Gif tutorial image
image_tutorial.set_from_file("images/tutorial.gif")

records_image = gtk.Image()  # Cup image
records_image.set_from_file("images/coup.png")
records_image.set_alignment(xalign=0.5, yalign=0)

golpes_txt = gtk.Label()  # Label
golpes_txt.set_label("PRUEBE EL TABLERO")

record_txt = gtk.Label()  # Label
record_txt.set_label("O ELIJA UN NIVEL")

puntuaciones = gtk.Label()  # Label to show the highscores
puntuaciones.set_text("MAXIMAS PUNTUACIONES!")
puntuaciones.set_alignment(xalign=0.5, yalign=0)
puntuaciones.set_visible(True)
print_hs()

firma = gtk.Label()
firma.set_text("Realizado por:\nAlvaro Velasco Gil\nMayo 2016")

# TABLES FOR SHOW
' Codificacion = 0:negro 1:rojo 2:oro 3:blanco 4:verde 5:plata 6:azul 7:rojo-negro 8:negro-rojo'
index_flecha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0,
				0, 1, 8, 8, 0, 0, 0, 0, 8, 0, 1, 1, 1, 0, 0, 0, 0, 7, 8, 1, 1, 1, 0, 0, 0, 0, 0, 7, 1, 1, 1, 0, 0, 0, 0,
				0, 0, 7, 1, 1, 8, 8, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index_ok = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4,
			0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 4, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 4, 4, 0, 4, 0, 4, 0, 4, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index_oro = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3, 2, 2,
			 2, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0,
			 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index_plata = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 3, 5,
			   5, 5, 5, 0, 5, 5, 0, 0, 5, 5, 5, 5, 0, 0, 5, 0, 5, 0, 0, 5, 5, 0, 0, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0,
			   0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index_yes = [0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0,
			 0, 2, 0, 0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0,
			 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0]

# PLAY-BUTTONS

for i in range(0, TAM2):
	imBlack = gtk.Image()  # creamos la imagen
	imBlack.set_from_file("images/black.png")
	butBlack = gtk.Button()  # creamos el boton
	butBlack.set_image(imBlack)
	butBlack.set_relief(gtk.RELIEF_NONE)
	botones.append(butBlack)

# PRINCIPAL WINDOW COLORS

index_interface(index_flecha)

# NEW TABLES

tabla = gtk.Table(TAM, TAM, homogeneous=True)
menu_table = gtk.Table(2, 3, homogeneous=True)
left_table = gtk.Table(2, 3, homogeneous=False)
supertable = gtk.Table(2, 2, homogeneous=False)
record_table = gtk.Table(2, 1, homogeneous=False)

(x, y) = (0, 0)  # ADD PLAY-BUTTONS TO Tabla
for b in botones:
	b.posicion = (x, y)
	tabla.attach(b, x, x + 1, y, y + 1)
	x += 1
	if x == TAM: x = 0; y += 1  # row change

(x, y) = (0, 0)
left_table.attach(but_left, 0, 1, 0, 1)
left_table.attach(tbox_level, 1, 2, 0, 1)
left_table.attach(but_right, 2, 3, 0, 1)
left_table.attach(but_level, 0, 3, 1, 2)

menu_table.attach(left_table, 0, 3, 0, 2)
menu_table.attach(golpes_txt, 3, 6, 0, 1)
menu_table.attach(but_undo, 6, 9, 0, 1)
menu_table.attach(record_txt, 3, 6, 1, 2)
menu_table.attach(but_reboot, 6, 7, 1, 2)
menu_table.attach(but_hs, 7, 8, 1, 2)
menu_table.attach(but_info, 8, 9, 1, 2)

(x, y) = (0, 0)
supertable.attach(tabla, 0, 1, 0, 1)
supertable.attach(menu_table, 0, 1, 1, 2)


for b in botones:
	b.connect("clicked", change_board)
	b.connect("clicked", more_undo)

but_left.connect("clicked", funct_left)
but_right.connect("clicked", funct_right)
but_level.connect("clicked", change_level)

but_undo.set_sensitive(False)
but_undo.set_label("No puedes deshacer")

but_undo.connect("clicked", less_undo)
but_undo.connect("pressed", apretado_undo)
but_undo.connect("released", soltado_undo)

but_reboot.connect("clicked", recomienza)
but_hs.connect("clicked", hs_on)
but_info.connect("clicked", info_on)

map = golpes_txt.get_colormap()
color = map.alloc_color("#808080")
style = golpes_txt.get_style().copy()
style.fg[gtk.STATE_NORMAL] = color
golpes_txt.set_style(style)
puntuaciones.set_style(style)
record_txt.set_style(style)

# END

ventana.modify_bg(gtk.STATE_NORMAL, color_gris)
ventana.set_title("THE CLEANER: Deja todo negro!")
ventana.set_position(centro)
ventana.connect("destroy", close_all)
ventana.add(supertable)
ventana.set_icon_from_file("images/icon.png")
ventana.set_resizable(False)
ventana.show_all()
gtk.main()

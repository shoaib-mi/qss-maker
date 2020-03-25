import sqlite3, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

__author__ = 'Shoaib Mirzaei'

class EditWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		theme_db_path = os.getcwd() + "/themes.db"
		if os.path.isfile(theme_db_path):
			#connection to database
			self.theme_db_conn = sqlite3.connect(theme_db_path)
			self.theme_db = self.theme_db_conn.cursor()
		else:
			#creating a database
			self.theme_db_conn = sqlite3.connect(theme_db_path)
			self.theme_db = self.theme_db_conn.cursor()
			#create a table for each widget and set column names to properties of widgets 
			sql = "CREATE TABLE 'QWidget' ( `ThemeName` TEXT, `font-family` TEXT, `font-size` TEXT )"
			self.theme_db.execute(sql)
			sql = "CREATE TABLE 'HeaderBar' ( `ThemeName` TEXT, `height` TEXT, `background-color` TEXT, `color` TEXT )"
			self.theme_db.execute(sql)
			sql = "CREATE TABLE 'OuterLayout' ( `ThemeName` TEXT, `background-image` TEXT )"
			self.theme_db.execute(sql)
			sql = "CREATE TABLE 'QComboBox' ( `ThemeName` TEXT, `color` TEXT, `background-color` TEXT, `selection-background-color` TEXT, `font-family` TEXT, `font-size` TEXT, `border` TEXT, `border-color` TEXT, `border-image` TEXT, `border-radius` TEXT, `border-style` TEXT, `border-width` TEXT, `margin` TEXT, `padding` TEXT, `text-align` TEXT, `width` TEXT, `height` TEXT )"
			self.theme_db.execute(sql)
			sql = "CREATE TABLE 'QGroupBox' ( `ThemeName` TEXT, `color` TEXT, `background-color` TEXT, `font-family` TEXT, `font-size` TEXT, `border` TEXT, `border-color` TEXT, `border-image` TEXT, `border-radius` TEXT, `border-style` TEXT, `border-width` TEXT, `margin` TEXT, `padding` TEXT, `text-align` TEXT )"
			self.theme_db.execute(sql)
			sql = "CREATE TABLE 'QLabel' ( `ThemeName` TEXT, `color` TEXT, `background-color` TEXT, `font-family` TEXT, `font` TEXT, `border-color` TEXT, `border-radius` TEXT, `border-style` TEXT, `border-width` TEXT, `margin` TEXT, `padding` TEXT, `qproperty-alignment` TEXT )"
			self.theme_db.execute(sql)
			sql = "CREATE TABLE 'QLineEdit' ( `ThemeName` TEXT, `color` TEXT, `background-color` TEXT, `font-family` TEXT, `font-size` TEXT, `border` TEXT, `border-color` TEXT, `border-image` TEXT, `border-radius` TEXT, `border-style` TEXT, `border-width` TEXT, `margin` TEXT, `padding` TEXT, `text-align` TEXT )"
			self.theme_db.execute(sql)
			sql = "CREATE TABLE 'QPushButton' ( `ThemeName` TEXT, `color` TEXT, `background-color` TEXT, `font-family` TEXT, `font-size` TEXT, `border` TEXT, `border-color` TEXT, `border-image` TEXT, `border-radius` TEXT, `border-style` TEXT, `border-width` TEXT, `margin` TEXT, `padding` TEXT, `text-align` TEXT )"
			self.theme_db.execute(sql)
			#sql = "CREATE TABLE 'QToolTip' ( `ThemeName` TEXT, `border` TEXT, `border-color` TEXT, `background-color` TEXT, `width` TEXT, `height` TEXT, `margin` TEXT, `padding` TEXT, `border-radius` TEXT, `color` TEXT )"
			#self.theme_db.execute(sql)
			sql = "CREATE TABLE 'QScrollArea' ( `ThemeName` TEXT, `border` TEXT, `border-color` TEXT, `background-color` TEXT, `background` TEXT, `width` TEXT, `height` TEXT, `margin` TEXT, `padding` TEXT, `border-radius` TEXT, `color` TEXT )"
			self.theme_db.execute(sql)
			sql = "CREATE TABLE 'QTableWidget' ( `ThemeName` TEXT, `color` TEXT, `background-color` TEXT, `font-family` TEXT, `font-size` TEXT, `border` TEXT, `border-color` TEXT, `border-image` TEXT, `border-radius` TEXT, `border-style` TEXT, `border-width` TEXT, `margin` TEXT, `padding` TEXT, `text-align` TEXT )"
			self.theme_db.execute(sql)
		
		self.select_theme()
		self.widget_presentation = QHBoxLayout()
		self.widget_presentation_gbox = QGroupBox(title='widget presentation')
		self.widget_presentation_gbox.setLayout(self.widget_presentation)
		self.widgets_box_gbox = QGroupBox(title='Widgets list')
		self.widgets_box = QVBoxLayout()
		self.properties_grid_gbox = QGroupBox(title='properties list')
		self.properties_grid = QGridLayout()
		
		radiobutton = QRadioButton("QWidget")
		radiobutton.text = "QWidget"
		radiobutton.widget = QLabel('universal config')
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("QLabel")
		radiobutton.text = "QLabel"
		radiobutton.widget = QLabel("sample text")
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("QLineEdit")
		radiobutton.text = "QLineEdit"
		radiobutton.widget = QLineEdit("sample text")
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("QComboBox")
		radiobutton.widget = QComboBox()
		for i in range(0,5):
			radiobutton.widget.addItem('value ' + str(i) + 'th')
		radiobutton.text = "QComboBox"
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("QGroupBox")
		radiobutton.widget = QGroupBox(title='title')
		tmp = QVBoxLayout()
		for i in range(0,5):
			tmp.addWidget( QLabel("label #" + str(i)) )
		radiobutton.widget.setLayout(tmp)
		radiobutton.text = "QGroupBox"
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("QTableWidget")
		radiobutton.widget = QTableWidget()
		radiobutton.widget.setRowCount(3)
		radiobutton.widget.setColumnCount(3)
		radiobutton.widget.setItem(0,0, QTableWidgetItem("Name"))
		radiobutton.widget.setItem(0,1, QTableWidgetItem("Email"))
		radiobutton.widget.setItem(0, 2 , QTableWidgetItem("Phone No"))
		radiobutton.widget.setItem(1,0, QTableWidgetItem("Parwiz"))
		radiobutton.widget.setItem(1,1, QTableWidgetItem("parwiz@gmail.com"))
		radiobutton.widget.setItem(1,2, QTableWidgetItem("845845845"))
		radiobutton.text = "QTableWidget"
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("QPushButton")
		radiobutton.widget = QPushButton('button')
		radiobutton.text = "QPushButton"
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("QScrollArea")
		radiobutton.widget = QScrollArea()
		tmp = QGroupBox()
		tmp_layout = QVBoxLayout()
		for i in range(0,50):
			tmp_layout.addWidget(QPushButton("button #" + str(i)))
		tmp.setLayout( tmp_layout )
		radiobutton.widget.setWidget(tmp)
		radiobutton.text = "QScrollArea"
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("OuterLayout")
		radiobutton.widget = QVBoxLayout()
		radiobutton.text = "OuterLayout"
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		radiobutton = QRadioButton("HeaderBar")
		radiobutton.widget = QVBoxLayout()
		radiobutton.text = "HeaderBar"
		radiobutton.toggled.connect(self.on_radio_button_toggled)
		self.widgets_box.addWidget(radiobutton)
		
		self.widgets_box_gbox.setLayout(self.widgets_box)
		self.properties_grid_gbox.setLayout(self.properties_grid)
		
		self.config_box = QHBoxLayout()
		self.config_box.setObjectName('MainBox')
		self.config_box.addWidget(self.widgets_box_gbox)
		self.config_box.addWidget(self.properties_grid_gbox)
		self.config_box.addWidget(self.widget_presentation_gbox)
		
		create_button = QPushButton("create qss file")
		create_button.setStyleSheet("background-color:green;")
		create_button.clicked.connect(self.create_qss_clicked)
		
		self.save_box = QHBoxLayout()
		self.save_box.setObjectName('MainBox')
		self.save_box.addWidget(QLabel("theme_name: " + self.theme_name + ','))
		self.save_box.addWidget(QLabel("<font color=blue><u>$all the changes you are making will be automatically saved$</u></font>"))
		self.save_box.addWidget(create_button)

		self.statusbar = QLabel()
		self.main_box = QVBoxLayout()
		self.main_box.addLayout(self.save_box)
		self.main_box.addLayout(self.config_box)
		self.main_box.addWidget(self.statusbar)
		self.setLayout(self.main_box)

	def create_qss_clicked(self):
		f = open(self.theme_name + '-style.qss','w')
		self.theme_db.execute( "select name from sqlite_master where type = 'table'" )
		tables = self.theme_db.fetchall()
		for table in tables:
			self.theme_db.execute( 'SELECT * FROM ' + table[0] + ' WHERE ThemeName="' + self.theme_name + '"' )
			values = self.theme_db.fetchall()
			descriptions = self.theme_db.description
			f.write(table[0] + "{\n")
			for i in range(1,len(descriptions)):
				if values[0][i]:
					f.write("	" + descriptions[i][0] + ": " + values[0][i] + ";\n")
			f.write("}\n\n")
		f.close()
		self.statusbar.setStyleSheet("background-color: purple;color:white;")
		self.statusbar.setText("qss file has been created successfuly")

	def select_theme(self):
		self.dialog = QDialog()
		label1 = QLabel( "select your theme" )
		label2 = QLabel( "Enter new theme name" )
		new_theme = QLineEdit()
		new_theme.textChanged.connect(self.new_theme_text_changed)
		self.theme_db.execute( "select ThemeName from QLabel" )
		themes = self.theme_db.fetchall()
		theme_list = []
		combo = QComboBox()
		for l in themes:
			theme_list.append( l[0] )
			combo.addItem( l[0] )
		buttonbox = QHBoxLayout()
		ok_button = QPushButton('ok')
		ok_button.clicked.connect( lambda status,text=combo.currentText(),themes_list=theme_list:self.ok_button_clicked(status,text,theme_list) )
		cancel_button = QPushButton('cancel')
		cancel_button.clicked.connect( self.cancel_button_clicked )
		self.new_button = QPushButton('New Theme')
		self.new_button.clicked.connect( lambda status,widget=new_theme:self.new_button_clicked(status,widget) )
		self.new_button.setEnabled(False)
		buttonbox.addWidget( self.new_button )
		buttonbox.addWidget( cancel_button )
		buttonbox.addWidget( ok_button )
		ok_button.setDefault(True)
		layout = QGridLayout()
		layout.addWidget(label1,0,0)
		layout.addWidget(combo,1,0)
		layout.addWidget(label2,0,1)
		layout.addWidget(new_theme,1,1)
		layout.addLayout(buttonbox,2,0,1,2)
		self.dialog.setLayout(layout)
		self.dialog.exec_()
		
	def new_theme_text_changed(self,text):
		if text:
			self.new_button.setEnabled(True)
		else:
			self.new_button.setEnabled(False)
			
	def ok_button_clicked(self,status,text,theme_list):
		self.dialog.close()
		self.theme_name = text
		
	def cancel_button_clicked(self):
		self.dialog.close()
		quit()

	def new_button_clicked(self,status,widget):
		self.dialog.close()
		text = widget.text()
		self.theme_db.execute( "select name from sqlite_master where type = 'table'" )
		tables = self.theme_db.fetchall()
		for table in tables:
			self.theme_db.execute( "insert into " + table[0] + " (ThemeName) values('" + text + "')" )
		self.theme_db_conn.commit()
		self.theme_name = text

	def change_color_button_clicked(self,status,widget,prop,widget_to_show,tablename):
		color = QColorDialog.getColor()
		old_style = widget_to_show.styleSheet()
		new_style = prop + ":" + color.name() + ";"
		if color.isValid():
			widget.setStyleSheet("background-color:" + color.name() + ';')
			tmp = prop + ":"
			tmp_start_index = old_style.find(tmp)
			if tmp_start_index != -1:
				tmp_end_index = tmp_start_index + old_style[tmp_start_index:].find(';')
				if ( old_style[tmp_start_index-1] == ';' ) or ( tmp_start_index == 0 ):
					style = old_style[:tmp_start_index] + new_style + old_style[tmp_end_index+1:]
					widget_to_show.setStyleSheet( style )
			else:
				style = old_style + new_style
				widget_to_show.setStyleSheet( style )
			sql = 'UPDATE "' + tablename + '" SET "' + prop + '"="' + color.name() + '" WHERE "ThemeName"="' + self.theme_name + '"'
			self.theme_db.execute(sql)
			self.theme_db_conn.commit()
			
	def change_prop_text_changed(self,value,prop,widget_to_show,tablename):
		old_style = widget_to_show.styleSheet()
		new_style = prop + ":" + value + ";"
		tmp = prop + ":"
		tmp_start_index = old_style.find(tmp)
		if tmp_start_index != -1:
			tmp_end_index = tmp_start_index + old_style[tmp_start_index:].find(';')
			if ( old_style[tmp_start_index-1] == ';' ) or ( tmp_start_index == 0 ):
				if value == '':
					style = old_style[:tmp_start_index] + old_style[tmp_end_index+1:]
				else:
					style = old_style[:tmp_start_index] + new_style + old_style[tmp_end_index+1:]
				widget_to_show.setStyleSheet( style )
		else:
			style = old_style + new_style
			widget_to_show.setStyleSheet( style )
		sql = 'UPDATE "' + tablename + '" SET "' + prop + '" = "' + value + '" WHERE "ThemeName" = "' + self.theme_name + '"'
		self.theme_db.execute(sql)
		self.theme_db_conn.commit()

	def on_radio_button_toggled(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			layout = self.properties_grid
			for i in reversed( range( layout.count() ) ): 
				widgetToRemove = layout.itemAt(i).widget()
				layout.removeWidget(widgetToRemove)
				widgetToRemove.setParent(None)

			layout = self.widget_presentation
			for i in reversed( range( layout.count() ) ): 
				widgetToRemove = layout.itemAt(i).widget()
				layout.removeWidget(widgetToRemove)
				widgetToRemove.setParent(None)
				
			sql = "SELECT * FROM " + radiobutton.text + ' WHERE "ThemeName"="' + self.theme_name + '"'
			self.theme_db.execute(sql)
			qlabel_val = self.theme_db.fetchall()
			qlabel_description = self.theme_db.description
			for i in range(1,len(qlabel_description)):
				if qlabel_description[i][0] in ['color','background-color','border-color','selection-background-color']:
					change_color_button = QPushButton()
					self.properties_grid.addWidget( QLabel(qlabel_description[i][0]),i-1,0 )
					self.properties_grid.addWidget( change_color_button,i-1,1 )
					if ( len(qlabel_val)>0 ) and ( qlabel_val[0][i] not in [None,'None',''] ):
						radiobutton.widget.setStyleSheet( radiobutton.widget.styleSheet() + qlabel_description[i][0] + ":" + qlabel_val[0][i] + ';' )
						change_color_button.setStyleSheet( "background-color:" + qlabel_val[0][i] + ';' )
					change_color_button.clicked.connect(lambda status,widget=change_color_button,prop=qlabel_description[i][0],widget_to_show=radiobutton.widget,tablename=radiobutton.text: self.change_color_button_clicked(status,widget,prop,widget_to_show,tablename))
				else:
					change_prop_text = QLineEdit()
					self.properties_grid.addWidget( QLabel(qlabel_description[i][0]),i-1,0 )
					self.properties_grid.addWidget( change_prop_text,i-1,1 )
					if ( len(qlabel_val)>0 ) and ( qlabel_val[0][i] not in [None,'None',''] ):
						radiobutton.widget.setStyleSheet( radiobutton.widget.styleSheet() + qlabel_description[i][0] + ":" + qlabel_val[0][i] + ';' )
						change_prop_text.setText( qlabel_val[0][i] )
					change_prop_text.textChanged.connect(lambda text,prop=qlabel_description[i][0],widget_to_show=radiobutton.widget,tablename=radiobutton.text: self.change_prop_text_changed(text,prop,widget_to_show,tablename))
			self.widget_presentation.addWidget(radiobutton.widget)
				
app = QApplication( [] )
edit_page = EditWindow()
edit_page.show()
app.exec_()

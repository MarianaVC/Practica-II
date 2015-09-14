#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Clase para el chat. 
author: Mariana Valdivia
correo: marianavc@ciencias.unam.mx
last edited: Agosto 2015
"""

import sys
from PyQt4 import QtGui, QtCore


class Login(QtGui.QWidget):
    
    def __init__(self):
        super(Login, self).__init__()
        self.ventanaLogin()
        ##
        
        
    def ventanaLogin(self):

        #Definomos los labels para los inputs
        usuario = QtGui.QLabel('Nombre de usuario')
        password = QtGui.QLabel('Contraseña')
        ip = QtGui.QLabel('IP del otro usuario')   
        # definimos los inputs
        self.usuarioEdit = QtGui.QLineEdit()
        self.passwordEdit = QtGui.QLineEdit()
        self.ipEdit = QtGui.QLineEdit()
        #definimos el grid
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        #definimos los botones. 
        self.login_btn = QtGui.QPushButton('Iniciar Sesión', self)
        cancelar_btn = QtGui.QPushButton('Cancelar', self)
        #definimos la acción del botón cancelar y para el botón de iniciar sesión. 
        cancelar_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.login_btn.clicked.connect(self.iniciaSesion)

        #Acomodamos los elementos con el grid. 
        grid.addWidget(usuario, 1, 0)
        grid.addWidget(self.usuarioEdit, 1, 1)

        grid.addWidget(password, 2, 0)
        grid.addWidget(self.passwordEdit, 2, 1)

        grid.addWidget(ip, 3,0)
        grid.addWidget(self.ipEdit, 3, 1)

        grid.addWidget(self.login_btn, 4 , 0)
        grid.addWidget(cancelar_btn, 4, 1)



        # ajustamos los botones. 
        self.login_btn.resize(self.login_btn.sizeHint())
        cancelar_btn.resize(cancelar_btn.sizeHint())

        #preparamos la ventana 
        self.setLayout(grid) 
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Iniciar Sesión')
        self.setWindowIcon(QtGui.QIcon('user.png'))
        self.center()
        self.show()
        
    # Con esta función hacemos que la ventana se muestre en el centro de la pantalla.     
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    

    def iniciaSesion(self):
        rojo = '#f6989d' 
        verde = '#c4df9b'         
        if(self.usuarioEdit.text()=='admin' and self.passwordEdit.text()=='admin' and self.ipEdit.text()!=''):
            self.usuarioEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.passwordEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.ipEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            # hacemos un evento al dar click al botón de iniciar sesión. 
            self.chat = Chat()
            self.login_btn.clicked.connect(self.on_pushButton_clicked)
            ##self.close()
        elif(self.usuarioEdit.text()=='admin' and
            self.passwordEdit.text()!='admin' and
            self.ipEdit.text()!=''):
            self.usuarioEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.passwordEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.ipEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.login_btn.clicked.connect(self.iniciaSesion)
        elif(self.usuarioEdit.text()=='admin' and
            self.passwordEdit.text()=='admin' and
            self.ipEdit.text()==''):
            self.usuarioEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.passwordEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.ipEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.login_btn.clicked.connect(self.iniciaSesion)
        elif(self.usuarioEdit.text()=='admin' and
            self.passwordEdit.text()!='admin' and
            self.ipEdit.text()==''):
            self.usuarioEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.passwordEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.ipEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.login_btn.clicked.connect(self.iniciaSesion)
        elif(self.usuarioEdit.text()=='admin' and
            self.passwordEdit.text()=='admin' and
            self.ipEdit.text()==''): 
            self.usuarioEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.passwordEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.ipEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.login_btn.clicked.connect(self.iniciaSesion) 
        elif(self.usuarioEdit.text()!='admin' and
            self.passwordEdit.text()=='admin' and
            self.ipEdit.text()==''):
            self.usuarioEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.passwordEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.ipEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.login_btn.clicked.connect(self.iniciaSesion)
        elif(self.usuarioEdit.text()!='admin' and
            self.passwordEdit.text()=='admin' and
            self.ipEdit.text()!=''):
            self.usuarioEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.passwordEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.ipEdit.setStyleSheet('QLineEdit { background-color: %s }' % verde)
            self.login_btn.clicked.connect(self.iniciaSesion)
        elif(self.usuarioEdit.text()!='admin' and
            self.passwordEdit.text()!='admin' and
            self.ipEdit.text()==''):
            self.usuarioEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.passwordEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.ipEdit.setStyleSheet('QLineEdit { background-color: %s }' % rojo)
            self.login_btn.clicked.connect(self.iniciaSesion)    

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        self.chat.exec_()




class Chat(QtGui.QWidget):

    def __init__(self):
        super(Chat, self).__init__()
        
        self.ventanaChat()

    def ventanaChat(self):
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid) 
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Chat')
        self.setWindowIcon(QtGui.QIcon('user.png'))
        self.center()
        self.show()
        
    # Con esta función hacemos que la ventana se muestre en el centro de la pantalla.     
    def center(self):  
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())  
            
                
  
def main():
    
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Login')

    main = Login()
    main.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()  
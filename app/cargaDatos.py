#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime,re
from models import User, Role, Padron, Listas
from config import db,app


with app.app_context():

    db.drop_all()
    db.create_all()


    if not User.query.filter(User.username == "admin").first():
        
        # creo los roles
        rol1 = Role(name="admin")
        rol2 = Role(name="std")
        
        db.session.add(rol1)
        db.session.add(rol2)

        # creo un usuario admin
        userAdmin = User(
                username="admin",
                password="1234",
            )
        userAdmin.roles.append(rol1)
        db.session.add(userAdmin)
        
        #Creo usuarios Std para votar
        x = 1
        while (x <= 3):
            userStd = User(
                    username="User" + str(x),
                    password="1234",
                )
            userStd.roles.append(rol2)
            x+=1
            #Agrego Session
            db.session.add(userStd)
            
        #Creo listas En blanco y Anulado
        
        lista_1 = Listas (
            nro_lista = "En Blanco",
        )
        
        lista_2 = Listas (
            nro_lista = "Nulo",
        )
        db.session.add(lista_1)
        db.session.add(lista_2)
        

    # datos para el padrón
    archivo = open("padron.html", "r", encoding="utf8")
    padron = archivo.read()
    pattern = re.compile("</span>(\d\d\d)</div>")
    matching = pattern.findall(padron)
    nros_socio = []
    for n in matching:
        padron = Padron(nro_socio=n)
        db.session.add(padron)


    db.session.commit()
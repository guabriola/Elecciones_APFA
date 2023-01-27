#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime,re


from models import User, Role, Padron
from config import db,app


with app.app_context():

    db.drop_all()
    db.create_all()


    if not User.query.filter(User.username == "admin").first():
        # creo los roles
        rol1 = Role(name="admin")
        rol2 = Role(name="std")

        # creo un usuario admin
        user = User(
                username="admin",
                password="1234",
            )
        user.roles.append(rol1)

        # agrego
        db.session.add(rol1)
        db.session.add(rol2)
        db.session.add(user)

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
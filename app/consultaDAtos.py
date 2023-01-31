#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime, re

from models import User, Role, Padron
from config import db, app

with app.app_context():
    lista_padron = []
    lista_padron = (db.session.query(Padron.id, Padron.nro_socio).all())
    print(lista_padron)

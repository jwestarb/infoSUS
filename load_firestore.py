#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

current_dir = os.getcwd()
json_dir = os.path.join(current_dir, 'Sigtap', 'json')
filename = os.path.join(json_dir, 'tb_procedimento.json')

try:
    f = open(filename, 'r', encoding='utf-8')
except IOError as ex:
    print('Não foi possivel abrir o arquivo {}'.format(filename))

cred = credentials.Certificate(
    "procsus-a03a9-firebase-adminsdk-4dab7-aae19a5a30.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

r = json.loads(f.read())

for proc in r["tb_procedimento"]:
    print(proc["CO_PROCEDIMENTO"])
    doc_ref = db.collection('procedimentos').document(proc["CO_PROCEDIMENTO"])
    doc_ref.set(proc)

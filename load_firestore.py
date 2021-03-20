#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import json
import progressbar
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

SIGTAP_TABLES = (
    ('tb_procedimento', 'co_procedimento'),
    ('tb_grupo', 'co_grupo'),
    ('tb_sub_grupo', 'co_sub_grupo'),
    ('tb_forma_organizacao', 'co_forma_organizacao'),
    ('tb_cid', 'co_cid'),
    ('tb_descricao', 'co_procedimento'),
    ('tb_descricao_detalhe', 'co_detalhe'),
    ('tb_detalhe', 'co_detalhe'),
    ('tb_financiamento', 'co_financiamento'),
    ('tb_grupo_habilitacao', 'nu_grupo_habilitacao'),
    ('tb_habilitacao', 'co_habilitacao'),
    ('tb_modalidade', 'co_modalidade'),
    ('tb_ocupacao', 'co_ocupacao'),
    ('tb_registro', 'co_registro'),
    ('tb_regra_condicionada', 'co_regra_condicionada'),
    ('tb_renases', 'co_renases'),
    ('tb_rubrica', 'co_rubrica'),
    ('tb_servico', 'co_servico'),
    ('tb_servico_classificacao', 'co_servico'),
    ('tb_sia_sih', 'co_procedimento_sia_sih'),
    ('tb_tipo_leito', 'co_tipo_leito'),
    ('tb_componente_rede', 'co_componente_rede'),
    ('tb_rede_atencao', 'co_rede_atencao'),
    ('tb_tuss', 'co_tuss')
)

if __name__ == '__main__':
    current_dir = os.getcwd()
    json_dir = os.path.join(current_dir, 'Sigtap', 'json')

    cred = credentials.Certificate('comments-devjc-ad243d4d5314.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    total_regs = 0

    for table in SIGTAP_TABLES:
        # print(table[0], ' - ', table[1])
        filename = os.path.join(json_dir, '{}.json'.format(table[0]))

        try:
            f = open(filename, 'r', encoding='utf-8')
        except IOError as ex:
            print('Não foi possivel abrir o arquivo {}. Erro: {}'.format(filename, ex))
            sys.exit(-1)

        r = json.loads(f.read())
        table_json = r[table[0]]
        qtd = len(table_json)

        total_regs = total_regs + qtd
        print(table[0], ': ', qtd)

        # pbar_widgets = [
        #     progressbar.FormatLabel('Reg: %(value)d / '),
        #     progressbar.Percentage(),
        #     progressbar.Bar()
        # ]
        # pbar = progressbar.ProgressBar(widgets=pbar_widgets, maxval=qtd)
        # pbar.start()

        batch = db.batch()
        i = 0

        for num, reg in enumerate(table_json):
            key = reg[table[1]]
            # doc_ref = db.collection(table[0]).document(key)
            # batch.set(doc_ref, reg)
            i += 1
            # pbar.update(num)
            if i == 500:
                i = 0
                # batch.commit()

        # batch.commit()
        # pbar.finish()

    print('TOTAL: ', total_regs)
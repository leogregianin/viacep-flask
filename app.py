#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for
import json
import requests
import viacep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def busca_cep():
    d_cep = request.form['cep']
    d = viacep.ViaCEP(d_cep)
    dados_json = d.retorna_json_completo()

    cep      = dados_json['cep']
    rua      = (u'%s' % dados_json['logradouro'])
    bairro   = (u'%s' % dados_json['bairro'])
    cidade   = (u'%s' % dados_json['localidade'])
    uf       = dados_json['uf']
    ibge     = dados_json['ibge']
    return render_template('busca_cep.html', cep=cep,rua=rua,bairro=bairro,cidade=cidade,uf=uf,ibge=ibge)

if __name__ == '__main__':
    app.run()  

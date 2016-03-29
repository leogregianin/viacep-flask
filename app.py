#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for
import json
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def busca_cep():
    d_cep = request.form['cep']
    url_api = ('http://www.viacep.com.br/ws/%s/json' % d_cep)
    req = requests.get(url_api)
    print(req.text)
    dados_json = json.loads(req.text)

    cep      = dados_json['cep']
    rua      = dados_json['logradouro']
    bairro   = dados_json['bairro']
    cidade   = dados_json['localidade']
    uf       = dados_json['uf']
    ibge     = dados_json['ibge']
    return render_template('busca_cep.html', cep=cep,rua=rua,bairro=bairro,cidade=cidade,uf=uf,ibge=ibge)

if __name__ == '__main__':
    app.run()  

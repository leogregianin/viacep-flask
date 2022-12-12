#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for
import json
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def busca_cep():
    d_cep = request.form['cep']
    if len(d_cep) != 8:
        msg = "Digite um valor numérico de 8 dígitos"
        return render_template('index.html', msg=msg)


    d = requests.get('https://viacep.com.br/ws/{}/json/'.format(d_cep))
    dados_json = d.json()

    if dados_json.get('erro'):
        return render_template('erro.html')


    cep      = dados_json['cep']
    rua      = (u'%s' % dados_json['logradouro'])
    bairro   = (u'%s' % dados_json['bairro'])
    cidade   = (u'%s' % dados_json['localidade'])
    uf       = dados_json['uf']
    ibge     = dados_json['ibge']
    return render_template('busca_cep.html', cep=cep,rua=rua,bairro=bairro,cidade=cidade,uf=uf,ibge=ibge)

if __name__ == '__main__':
    app.run()  

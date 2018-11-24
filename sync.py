#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import run, PIPE

dirdest = "/mnt/dadoscoopemg01/share/"
dirlocal = "/mnt/dadoscoopemgsede/share/"
dirfinal = "ssh://192.168.102.252:5252//" + dirdest

logfile = open("/var/log/log.unisync", "a")

param1 = "/usr/local/bin/unison  -perms 0 -auto -prefer"
unison_env = os.environ.copy()


diretorios=[
    'GERENCIA_CONTROLE_FINANCEIRO/Gerência_de_Controles\ Financeiros/CARTÃO\ DE\ ASSINATURA\ -\ COOPERADOS',
    'CONTROLE_INTERNO/PRODUCAO\ ATENDIMENTO',
    'GERENCIA_CONTROLE_FINANCEIRO/CAPITAL\ SOCIAL\ -\ RESGATES\ EVENTUAIS/Registros\ Resgates',
    'GERENCIA_RELACIONAMENTO_NEGOCIO/Gerencia_de_\ Contas/Produto\ e\ Serviços/Sicoob\ consórcio/',
    'GERENCIA_RELACIONAMENTO_NEGOCIO/ATENDIMENTO/SILVANE',
    'GERENCIA_RELACIONAMENTO_NEGOCIO/Controle\ de\ Agenda\ \ e\ banco\ de\ horas\ do\ setor/Banco\ de\ Horas/', 
    'scanner',
    ]

def execute(cmd):
    print ("Executando " + cmd + "\n")
    saida = run(cmd, env=unison_env, shell=True, stdout=logfile, stderr=logfile)
    if saida.returncode  > 0:
        print ( "Erro ao executa " + cmd + "\n\n" )

pid = str(os.getpid())
pidfile = "/tmp/unisonsync.pid"

if os.path.isfile(pidfile):
    print ("%s arquivo existe, saindo..." % pidfile)
    sys.exit()
open(pidfile, 'w').write(pid)
try:

    for dir in diretorios:
        direxe = dir.replace(" ","\\ ")
        cmd = param1 + " " + dirlocal + direxe + " -batch " + dirlocal + direxe + " " + dirfinal + direxe
        execute(cmd)

finally:
    os.unlink(pidfile)


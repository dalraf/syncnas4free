#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import run, PIPE

dirdest = "/mnt/dadosufvcredipa01/share/"
dirlocal = "/mnt/dadosufvcredi01/sharenew/"
dirfinal = "ssh://192.168.22.251:5252//" + dirdest

logfile = open("/var/log/log.unisync", "a")

param1 = "/usr/local/bin/unison  -perms 0 -auto -prefer"
unison_env = os.environ.copy()


diretorios=[
    'DOCUMENTOS ABERTURA DE CONTAS',
    'SEGUROS',
    ]

def execute(cmd):
    print ("Executando " + cmd + "\n")
    saida = run(cmd, env=unison_env, shell=True, stdout=logfile, stderr=logfile)
    if saida.returncode  > 0:
        print ( "Erro ao executa " + cmd + "\n o erro foi\n" + output + erro + str(rc) )

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


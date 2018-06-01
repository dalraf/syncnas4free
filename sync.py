#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import Popen, PIPE

def execute(cmd):
    print "Executando " + cmd + "\n"
    saida = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, erro = saida.communicate()
    rc = saida.returncode
    if rc > 0:
        print "Erro ao executa " + cmd + "\n o erro foi\n" + output + erro + str(rc)

pid = str(os.getpid())
pidfile = "/tmp/mydaemon.pid"

if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    sys.exit()
file(pidfile, 'w').write(pid)
try:
    dirdest = "/mnt/dadosufvcredipa01/share/"
    dirlocal = "/mnt/dadosufvcredi01/share/"
    dirfinal = "ssh://192.168.22.251:5252//" + dirdest
    param1 = "/usr/local/bin/unison  -perms 0 -logfile /var/log/log.unisync -auto -prefer"
    diretorios=[
        'DOCUMENTOS\\ ABERTURA\\ DE\\ CONTAS',
        'SEGUROS',
        ]

    for dir in diretorios:
        cmd = param1 + " " + dirlocal + dir + " -batch " + dirlocal + dir + " " + dirfinal + dir
        execute(cmd)

finally:
    os.unlink(pidfile)


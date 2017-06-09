#!/usr/bin/python
# -*- coding: utf-8 -*-
from files import *
import sintatico
import lexico
import sys


def main():
    try:
        sys.argv[1]
    except Exception:
        print getErro(00, None, None)
        return None

    if(checarExtensao(sys.argv[1]) != 1):
        print getErro(01, None, None)
        return None

    source = readSource(sys.argv[1])       # Ler código fonte
    tokens = lexico.findTokens(source)     # Encontrar tokens
    lexico.findErros(tokens)               # Encontrar erros lexicos
    lexico.makeTable(tokens)               # Construir arquivo com tabela de tokens
    sintatico.programa(tokens)


if __name__ == '__main__':
    main()
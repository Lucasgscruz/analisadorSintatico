#!/usr/bin/python
# -*- coding: utf-8 -*-

from files import *
import sintatico
import erros
import lexico
import sys


def main():
    try:
        sys.argv[1]
    except Exception:
        print erros.getErro(00, None, None)
        return None

    if(checarExtensao(sys.argv[1]) != 1):
        print erros.getErro(01, None, None)
        return None

    source = readSource(sys.argv[1])    # Ler código fonte
    tokens = lexico.findTokens(source)  # Encontrar tokens
    erro = lexico.findErros(tokens)     # Encontrar erros lexicos
    if(erro == 0):                     # Se não foram encontrados erros léxicos
        lexico.makeTable(tokens)
                         # Construir arquivo com tabela de tokens
        sintatico.programa(tokens)


if __name__ == '__main__':
    main()

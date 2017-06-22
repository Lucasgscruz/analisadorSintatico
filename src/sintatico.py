#!/usr/bin/python
# -*- coding: utf-8 -*-

from erros import *
import sys
import re

if __name__ != '__main__':
    i = 0

    def E(tokens):
        T(tokens)
        Elinha(tokens)

    def T(tokens):
        F(tokens)
        Tlinha(tokens)

    def F(tokens):
        global i
        if(re.match(r'^[a-zA-z0-9_]', tokens[i][0]) or
           re.match(r'^[-0-9.]+$', tokens[i][0])):   # Terminal
            i += 1
        elif(tokens[i][0] == '('):  # Terminal
            i += 1
            E(tokens)
            if(tokens[i][0] == ')'):  # Terminal
                i += 1
            else:
                print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                sys.exit()
        else:
            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
            sys.exit()

    def Elinha(tokens):
        global i
        if(tokens[i][0] == '+'):
            i += 1
            T(tokens)
            Elinha(tokens)
        elif(tokens[i][0] == '$' or tokens[i][0] == ')' or tokens[i][0] == ';'
             or tokens[i][0] == '{'):
            pass
        else:
            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
            sys.exit()

    def Tlinha(tokens):
        global i
        if(tokens[i][0] == '*'):
            i += 1
            F(tokens)
            Tlinha(tokens)
        elif(tokens[i][0] == '$' or tokens[i][0] == '+'
             or tokens[i][0] == ')' or tokens[i][0] == ';' or tokens[i][0] == '{'):
            pass
        else:
            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
            sys.exit()

    def expressao(tokens):
        """
        Realiza verificação da validade de expressões aritmeticas.
        """
        E(tokens)
        return 1

    def valor(tokens):
        if(expressao(tokens)):  # Se for expressao, numero ou id
            pass
        else:
            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
            sys.exit()

    def atribuicao(tokens):
        global i
        if(re.match(r'^[a-zA-z0-9_]+$', tokens[i][0])):  # <ID>
            i += 1
            if(tokens[i][0] == '='):  # <ATTRIB>
                i += 1
                valor(tokens)
                if(tokens[i][0] == ';'):  # <;>
                    i += 1
                else:
                    i -= 1
                    print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                    sys.exit()
            else:
                print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                sys.exit()

    def dec2(tokens):
        global i
        i += 1
        if(re.match(r'^[a-zA-z0-9_]+$', tokens[i][0])):  # <ID>
            i += 1
            if(tokens[i][0] == ';'):
                pass
            elif(tokens[i][0] == ','):  # Se for outra virgula
                dec2(tokens)
            else:
                print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                sys.exit()
        else:
            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
            sys.exit()

    def declaracao(tokens):
        global i
        i += 1
        if(re.match(r'^[a-zA-z0-9_]+$', tokens[i][0])):  # <ID>
            i += 1
            if(tokens[i][0] == ','):  # Multiplas declarações
                dec2(tokens)
            elif(tokens[i][0] == ';'):  # Declaração simples
                i += 1
            elif(tokens[i][0] == '='):  # Declaração com atribuicao
                i -= 1
                atribuicao(tokens)
            else:
                print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                sys.exit()
        else:
            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
            sys.exit()

    def bloco(tokens):
        global i
        while (tokens[i][0] != '}'):
            # Se o token for uma palavra reservada é uma declaracao
            if(tokens[i][0] == 'int' or tokens[i][0] == 'float' or tokens[i][0] == 'char'):
                declaracao(tokens)

            # Se o token for uma repetiçao
            elif(tokens[i][0] == 'while'):
                repeticao(tokens)

            # Se o token for uma condicao
            elif(tokens[i][0] == 'if'):
                condicao(tokens)

            # Se o token for um identificador é uma atribuição
            elif(re.match(r'^[a-zA-z0-9_]+$', tokens[i][0])):
                atribuicao(tokens)

    def repeticao(tokens):
        global i
        i += 1
        if(expressao(tokens)):
            if(tokens[i][0] == '{'):
                i += 1
                bloco(tokens)
                if(tokens[i][0] == '}'):
                    i += 1
                else:
                    print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                    sys.exit()
            else:
                print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                sys.exit()
        else:
            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
            sys.exit()

    def condicao(tokens):
        global i
        i += 1
        if(expressao(tokens)):
            if(tokens[i][0] == '{'):
                i += 1
                bloco(tokens)
                if(tokens[i][0] == '}'):
                    i += 1
                else:
                    print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                    sys.exit()
                if(tokens[i][0] == 'else'):
                    i += 1
                    if(tokens[i][0] == '{'):
                        i += 1
                        bloco(tokens)
                        if(tokens[i][0] == '}'):
                            i += 1
                        else:
                            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                            sys.exit()
                    else:
                        print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                        sys.exit()
            else:
                print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ', tokens[i][2]
                sys.exit()
        else:
            print '[Erro] Erro sintatico: linha ', tokens[i][1], 'coluna ',
            tokens[i][2], ' - Expressao invalida!'
            sys.exit()

    def programa(tokens):
        """
        Funçao para reconhecimento dos tipos de tokens.
        """
        global i
        tokens.append('$')

        while (i < len(tokens)):
            if(tokens[i][0] == '$'):
                i += 1
            # Se o token for uma palavra reservada é uma declaracao
            elif(tokens[i][0] == 'int' or tokens[i][0] == 'float' or tokens[i][0] == 'char'):
                declaracao(tokens)

            # Se o token for uma repetiçao
            elif(tokens[i][0] == 'while'):
                repeticao(tokens)

            # Se o token for uma condicao
            elif(tokens[i][0] == 'if'):
                condicao(tokens)

            # Se o token for um identificador é uma atribuição
            elif(re.match(r'^[a-zA-z0-9_]+$', tokens[i][0])):
                atribuicao(tokens)

            else:
                i += 1
        else:
            print '\nAnalises léxica e sintatica concluidas! Nenhum erro detectado!'

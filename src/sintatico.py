#!/usr/bin/python
# -*- coding: utf-8 -*-

from erros import *
import sys
import re

if __name__ != '__main__':
    i = 0

    def E(tokens):
        # print ' entrou E'
        T(tokens)
        Elinha(tokens)

    def T(tokens):
        # print ' entrou  T'
        F(tokens)
        Tlinha(tokens)

    def F(tokens):
        # print ' entrou F'
        global i
        if(re.match(r'^[a-zA-z0-9_]', tokens[i]) or
           re.match(r'^[-0-9.]+$', tokens[i])):   # Terminal
            i += 1
        elif(tokens[i] == '('):  # Terminal
            i += 1
            E(tokens)
            if(tokens[i] == ')'):  # Terminal
                i += 1
            else:
                "Erro na função F! Parenteses nao fechado!"
                sys.exit()
        else:
            print "Erro na funcao F!"
            sys.exit()

    def Elinha(tokens):
        # print ' entrou E_ '
        global i
        if(tokens[i] == '+'):
            i += 1
            T(tokens)
            Elinha(tokens)
        elif(tokens[i] == '$' or tokens[i] == ')' or tokens[i] == ';' or tokens[i] == 'f'):
            pass
        else:
            print 'Erro na funçao Elinha!'
            sys.exit()

    def Tlinha(tokens):
        # print ' entrou T_ '
        global i
        if(tokens[i] == '*'):
            i += 1
            F(tokens)
            Tlinha(tokens)
        elif(tokens[i] == '$' or tokens[i] == '+'
             or tokens[i] == ')' or tokens[i] == ';' or tokens[i] == 'f'):
            pass
        else:
            print 'Erro na funçao Tlinha!'
            sys.exit()

    def expressao(tokens):
        E(tokens)
        return 1

    def valor(tokens):
        if(expressao(tokens)):  # Se for expressao, numero ou id
            pass
        else:
            print 'Atribuicao invalida!'
            sys.exit()

    def atribuicao(tokens):
        global i
        if(re.match(r'^[a-zA-z0-9_]+$', tokens[i])):  # <ID>
            i += 1
            if(tokens[i] == '='):  # <ATTRIB>
                i += 1
                valor(tokens)
                if(tokens[i] == ';'):  # <;>
                    i += 1
                else:
                    print 'Erro! Falta um ponto e virgula'
                    sys.exit()
            else:
                print 'Erro! Falta o sinal de ='
                sys.exit()

    def declaracao(tokens):
        global i
        i += 1
        if(re.match(r'^[a-zA-z0-9_]+$', tokens[i])):
            i += 1
            if (tokens[i] == ';'):
                i += 1
            else:
                print 'Erro!'
        else:
            print 'Erro'

    def programa(tokens):
        global i
        tokens = ['int', 'a', ';']
        tokens.append('$')

        while (i < len(tokens)):
            if(tokens[i] == 'int' or tokens[i] == 'float' or tokens[i] == 'char'):
                declaracao(tokens)

            # Se o token for um identificador é uma atribuição
            elif(re.match(r'^[a-zA-z0-9_]+$', tokens[i])):
                atribuicao(tokens)


            i += 1
        else:
            print 'Encerrou a execuçao com sucesso!'

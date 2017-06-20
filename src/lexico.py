#!/usr/bin/python
# -*- coding: utf-8 -*-
from dicionario import *
from erros import *
from files import *
import re

if __name__ != '__main__':

    def findTokens(source):
        """
        Retorna a lista de tokens do codigo fonte.
        """
        i = 0
        linha = 1
        coluna = 1
        tokens = []
        tokenAux = ""

        while(i < len(source)):
            tokenAux += source[i]

            if (tokenAux == " "):  # Eliminar espaços
                tokenAux = ""
            else:

                if(tokenAux == '\n'):
                    linha += 1
                    coluna = 1
                    tokenAux = ""

                if(tokenAux == '/'):   # verifica comentarios
                    if(source[i + 1] == '/'):
                        tokenAux = ""
                        i += 1
                        while (source[i] != '\n'):
                            i += 1
                        else:
                            linha += 1
                            coluna = 1

                    elif(source[i + 1] == '*'):  # ???
                        tokenAux = ""
                        i += 2
                        while (source[i] != '*' and source[i + 1] != '/'):
                            if(source[i] == '\n'):
                                linha += 1
                                coluna = 1
                            i += 1
                        else:
                            i += 2

                if(i + 1 < len(source)):
                    # Pode ser um identificador ou uma palavra reservada.
                    if(re.match(r'^[a-zA-z0-9_]+$', tokenAux)):
                        if((source[i + 1] in delimitadores) or
                           (source[i + 1] in aritmeticos) or
                            (source[i + 1] in logicos) or
                           source[i + 1] == "\n"):
                            tokens.append([tokenAux, linha, coluna])
                            tokenAux = ""
                    # verifica numeros
                    if(re.match(r'([-\d]+[.]*[\d]+)', tokenAux)):
                        if((source[i + 1] in delimitadores) or
                            (source[i + 1] in aritmeticos) or
                            (source[i + 1] in logicos) or
                           source[i + 1] == '\n'):
                            tokens.append([tokenAux, linha, coluna])
                            tokenAux = ""

                    if(tokenAux == '='):    # verifica atribuição
                        if(re.match(r'([-\d]+[.]*[\d]+)', source[i + 1]) or
                           re.match(r'^[a-zA-z0-9_]+$', source[i + 1]) or
                           source[i + 1] == ' '):
                            tokens.append([tokenAux, linha, coluna])
                            tokenAux = ""

                    if(tokenAux in delimitadores):  # verifica delimitadores
                        tokens.append([tokenAux, linha, coluna])
                        tokenAux = ""

                    if(tokenAux in aritmeticos):  # verifica aritmeticos
                        tokens.append([tokenAux, linha, coluna])
                        tokenAux = ""

                    if(tokenAux in logicos):  # verifica logicos
                        if(str(tokenAux + source[i + 1] in uniaoLogicos) or
                           source[i + 1] == ' ' or
                           source[i + 1] == r'([-\d]+[.]*[\d]+)' or
                           source[i + 1] == r'^[a-zA-z]+$'):

                        # Reconhecimento de dois simbolos logicos juntos
                        #    if(re.match(r'^[-0-9.]+$', source[i+1])):
                        #         tokens.append(tokenAux)
                        #         tokenAux = ""
                        #    else:
                        #        tokens.append(tokenAux + source[i+1])
                        #        tokenAux = ""
                        #        i += 1
                            tokens.append([tokenAux, linha, coluna])
                            tokenAux = ""
            coluna += 1
            i += 1

        for j in tokens:
            print j
        return tokens

    def findErros(tokens):
        erro = 0
        for lexema in tokens:
            # Encontrar identificadores errados
            if(re.match(r'([\d]+[a-zA-z_]+)', lexema[0])):
                setListaErros(getErro(02, lexema[1], lexema[2]))
                erro = 1
            if(lexema[0] in logicos and
               ((tokens[tokens.index(lexema) + 1][0] in logicos) or
                (tokens[tokens.index(lexema) + 1][0] in aritmeticos)) and
                ((tokens[tokens.index(lexema) + 2][0] in logicos) or
                 (tokens[tokens.index(lexema) + 2][0] in aritmeticos))):
                setListaErros(getErro(02, lexema[1], lexema[2]))
                erro = 1

        for i in (getListaErros()):
            print i

        if(erro == 1):
            return 1
        return 0

    def makeTable(tokens):
        """
        Constroi tabala de tokens.
        """
        for i in tokens:
            if (i[0] in reservadas):
                writeTable(['[RESERVADA]', i[1], i[2]])

            elif(i[0] in aritmeticos):
                writeTable(['[ARITM]', i[1], i[2]])

            elif (i[0] in delimitadores):
                writeTable(['[DELIMITADOR]', i[1], i[2]])

            elif(i[0] in logicos):
                writeTable(['[LOGICO]', i[1], i[2]])

            elif (re.match(r'^[-0-9.]+$', i[0])):
                writeTable(['[NUM]', i[1], i[2]])

            elif (re.match(r'^[a-zA-z0-9_]+$', i[0])):
                writeTable(['[IDENTIFICADOR]', i[1], i[2]])

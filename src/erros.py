#!/usr/bin/python
# -*- coding: utf-8 -*-


if __name__ != '__main__':

    __dicErros__ = {
        00: "[Erro]: Arquivo contendo o código fonte não foi passado!",
        01: "[Erro]: O arquivo passado possui extensão incompatível.",
        02: "[Erro]: Erro lexico na linha "
    }

    __listaErros__ = []

    def getErro(chave, linha, coluna):
        """A função retorna a string do erro correspondente contido no
        dicionário de erros."""

        if(linha is None and coluna is None):
            return __dicErros__[chave]
        return __dicErros__[chave] + str(linha) + " e coluna " + str(coluna)

    def getListaErros():
        """A função retorna a lista de erros encontrados no código
        fonte."""

        return __listaErros__

    def setListaErros(erro):
        """A função acrescenta ao final da lista de erros uma nova string
        de um erro encontrado."""
        return __listaErros__.append(erro)

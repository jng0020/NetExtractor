# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

class CrearDiccionario:
    """
    Clase que crea un diccionario de manera automática
    
    Args:
        modusuario: instancia de la clase modelo
    """
    
    def __init__(self, modusuario):
        self.mod = modusuario
    
    def obtenerPersPelicula(self, url):
        lista = list()
        formato = 0
        web = urllib.request.urlopen(url)
        html = BeautifulSoup(web.read(), "html.parser")
        for pers in html.find_all("b"):
            if(not len(pers) == 0):
                pn = pers.contents[0]
                pn = str(pn)
                pn = pn.strip()
                if (not '<' in pn and not '>' in pn and not 'EXT.' in pn and not 'INT.' in pn and not 'INT ' in pn and not 'EXT ' in pn and not '.' in pn and not ':' in pn and not ';' in pn and not '"' in pn and not '!' in pn and not '?' in pn and not ',' in pn and len(pn)<30 and not 'Genres' in pn and not 'Writers' in pn and not '_' in pn):
                    if (not pn in lista):
                        if(not pn == ''):
                            lista.append(pn)
                            self.mod.anadirPersonaje(pn,pn)
                
                if ('EXT. ' in pn or 'INT. ' in pn or 'INT ' in pn or 'EXT ' in pn):
                    formato = 1
        if (formato == 0):
            self.mod.borrarDictPersonajes()
        if (len(lista)==0):
            formato = 0
        return formato
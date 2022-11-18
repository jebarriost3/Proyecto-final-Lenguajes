#parser con expresiones regulares 
#para el analizador lexico

import ply.lex as lex
import re
import codecs
import os
import sys
tokens =['piceplacement','sidetomove','castlingability','enpassanttargetsquare','halfmoveclock','fullmovecounter','FEN']
t_piceplacement = r'([1-8KQRBNPkqrbnp/]+)'
t_sidetomove = r'([wb])'
t_castlingability = r'([KQkq-]+)'
t_enpassanttargetsquare = r'([a-h][1-8]|-)'
t_halfmoveclock = r'([0-9]+)'
t_fullmovecounter = r'([1-9][0-9]*)'
t_ignore  = ' \t'
def t_FEN(t):
    r'([1-8KQRBNPkqrbnp/]+) ([wb]) ([KQkq-]+) ([a-h][1-8]|-) ([0-9]+) ([1-9][0-9]*)'
    t.value = t.value
    return t
def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
def t_newline(t):
    r' \n+  '
     
lexer = lex.lex()
data = input('Ingrese el FEN: ')
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok: break
    print (tok)
     
      
    
     

 

 

 
  
 
  
 


 
  

 
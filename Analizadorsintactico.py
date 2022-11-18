import ply.yacc as yacc
import os
import codecs
import re
from AnalizadorLexico2 import tokens
from AnalizadorLexico2 import lexer
from sys import stdin
 
precedence = (
    ('Left','piceplacement'), ('Left','sidetomove'), ('Left','castlingability'), ('Left','enpassanttargetsquare'), ('Left','halfmoveclock'), ('Left','fullmovecounter'), ('Left','FEN')
)
def p_pieceplacement(p):
    '''pieceplacement = rank8'/'rank7'/'rank6'/'rank5'/'rank4'/'rank3'/'rank2'/'rank1' '''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]
def p_slidetomove(p):
    '''sidetomove = 'w' | 'b' '''
    p[0] = p[1]
    
def p_castlingability(p):
    '''castlingability = '-' | 'K' | 'Q' | 'k' | 'q' | 'KQ' | 'Kk' | 'Kq' | 'Qk' | 'Qq' | 'kq' | 'KQk' | 'KQq' | 'Kkq' | 'Qkq' | 'KQkq' '''
    p[0] = p[1]
    
def p_enpassanttargetsquare(p):
    '''enpassanttargetsquare = '-' | 'a1' | 'a2' | 'a3' | 'a4' | 'a5' | 'a6' | 'a7' | 'a8' | 'b1' | 'b2' | 'b3' | 'b4' | 'b5' | 'b6' | 'b7' | 'b8' | 'c1' | 'c2' | 'c3' | 'c4' | 'c5' | 'c6' | 'c7' | 'c8' | 'd1' | 'd2' | 'd3' | 'd4' | 'd5' | 'd6' | 'd7' | 'd8' | 'e1' | 'e2' | 'e3' | 'e4' | 'e5' | 'e6' | 'e7' | 'e8' | 'f1' | 'f2' | 'f3' | 'f4' | 'f5' | 'f6' | 'f7' | 'f8' | 'g1' | 'g2' | 'g3' | 'g4' | 'g5' | 'g6' | 'g7' | 'g8' | 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6' | 'h7' | 'h8' '''
    p[0] = p[1]
    
def p_halfmoveclock(p):
    '''halfmoveclock = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' '''
    p[0] = p[1]
    
def p_fullmovecounter(p):
    '''fullmovecounter = '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' '''
    p[0] = p[1]
    

       
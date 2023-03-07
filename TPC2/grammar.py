from lark import Lark,Token
from lark.tree import pydot__tree_to_png
from lark import Transformer
from lark import Discard
import sys

grammar = '''
//Regras Sintaticas
start: entrada*
entrada : (completa | remissiva) (completa | remissiva)*
remissiva : "-" WORD+ (at_conceito)*
completa: ID (item)*
item: (lingua | at_conceito) 
//LF lingua (lingua)*
//Regras Lexicográficas
ID: "0".."9"+ 
//WORD:/[^\s:;]+/
WORD: /[^\s:;]+( [^\s:;]+)*(?=;)?/
DOISPONTOS:":"
// LINHAB: "/" 
//line: WORD+
lingua: ID_LINGUA DOISPONTOS WORD+ (VIR WORD+)*
VIR:";"
at_conceito: AT_CONCEITO DOISPONTOS WORD+ (VIR WORD+)* 
ID_LINGUA: ("es" | "ga" | "en" | "pt" | "la")
AT_CONCEITO: ("SIN" | "VAR" | "Area" | "Vid" | "Nota")
//%import common.WORD
//Tratamento dos espaços em branco
%import common.WS
%ignore WS
//%import common.LF
'''
# Soma da lista, encontrar o maior da lista
class ExemploTransformer(Transformer):
  def __init__(self):
          self.elems = {}


  def addElem(self,elem):
    # print(elem)
    if elem not in self.elems.keys(): self.elems[elem] = 1
    else: self.elems[elem] += 1

  def start(self,entrada):
    pass
    
  def entrada(self,entrada):
    pass

  def LF (self,linhab):
    pass
  
  def line(self,line):
    pass

  def DOISPONTOS(self, doispontos):
    # print("doisPontos")
    pass
    
  def ID_LINGUA(self,idL):
    # print("idL")
    pass 

  def WORD(self,word):
    # print("Word")
    pass 

  def VIR(self,vir):
    pass

  pass


p = Lark(grammar)   

# for frase in sys.stdin:
#     tree = p.parse(frase)
#     # print(tree.pretty())
#     #for element in tree.children:
#     #print(element)
#     data = ExemploTransformer().transform(tree) # chamar o transformer para obter
#     #print(data)


tree = p.parse('''
- A
Vid : adenina

1
ga : á f
Area : Anatomía
es : ala
en : wing
pt : asa
la : ala

2
ga : a termo a
Area : Fisioloxía
es : a término
en : full term
pt : a termo

3
ga : abdome m
Area : Anatomía
SIN : rexión abdominal (f); panza [pop.]
es : abdomen; panza [pop.]; región abdominal
en : abdomen; abdominal region; gut [pop.]
pt : abdome; abdômen [Br.]; abdómen [Pt.]; barriga [pop.]; região abdominal
la : abdomen

4
ga : abdome agudo m
Area : Semioloxía
es : abdomen agudo
en : acute abdomen
pt : abdome agudo; abdômen agudo [Br.]; abdómen agudo [Pt.]

- abdome distendido 
Vid : abdome globuloso

5
ga : abdome en táboa m
Area : Semioloxía
SIN : ventre de madeira
es : abdomen en tabla
en : abdominal guarding
pt : abdome em tábua; abdômen em tábua [Br.]; abdómen em tábua [Pt.]

6
ga : abdome globuloso m
Area : Semioloxía
SIN : abdome prominente; abdome distendido
es : abdomen distendido; abdomen globuloso; abdomen prominente
en : distended abdomen
pt : abdome distendido; abdômen distendido [Br.]; abdómen distendido [Pt.]

- abdome prominente 
Vid : abdome globuloso

- *abducción
Vid : abdución

7
ga : abdución f
Area : Fisioloxía Anatomía
SIN : separación
es : abducción; separación
en : abduction
pt : abdução; separação
la : abductio
Nota : Evítese “abducción”.

- aberración cromosómica 
Vid : anomalía cromosómica

8
ga : abertura inferior da pelve f
Area : Anatomía
SIN : estreito inferior da pelve (m)
es : estrecho inferior de la pelvis
en : pelvic outlet
pt : abertura inferior da pelve; estreito inferior da pelve
la : apertura pelvis inferior

''')

print(tree.pretty())
# for element in tree.children:
#   print(element)
data = ExemploTransformer().transform(tree) # chamar o transformer para obter
#print(data)




from lark import Lark,Token
from lark.tree import pydot__tree_to_png
from lark import Transformer
from lark import Discard
import sys

grammar = '''
//Regras Sintaticas
start: entrada*
entrada : LF completa (LF completa)*
remissiva : WORD+ LF (at_conceito LF)*
completa: ID (LF item)*
item: (lingua | at_conceito) 
//LF lingua (LF lingua)*
//Regras Lexicográficas
ID: "0".."9"+ 
WORD:/[^\s]+/
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
%import common.LF
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
3
ga : abdome
Area : Anatomia
SIN : rexion aslda
es : abdomen
en : abdomen
pt : abdome
la : abdomen
''')

print(tree.pretty())
for element in tree.children:
  print(element)
data = ExemploTransformer().transform(tree) # chamar o transformer para obter
#print(data)




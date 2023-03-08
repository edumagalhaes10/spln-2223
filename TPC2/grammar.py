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
WORD: /(?!\d)[^\s:;]+( [^\s:;]+)*(?=;)?/
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
    print(entrada)
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


f = open("t.txt","r")
txt = f.read()
f.close()


tree = p.parse(txt)

print(tree.pretty())
for element in tree.children:
  print(element)
data = ExemploTransformer().transform(tree) # chamar o transformer para obter
#print(data)




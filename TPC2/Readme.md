# TPC2

## 1ª fase

Numa primeira fase, foi acrescentada uma função *normalize* de forma a normalizar a sintaxe da linguagem para esta ser mais orientada ao conceito e menos ao pdf.

Assim, após correr o ficheiro **4med.py**, obtemos um ficheiro **new_syntax.txt** com a sintaxe normalizada da linguagem, obtida a partir de transformações do ficheiro xml inicial(**medicina.xml**).

## 2ª fase

Nesta fase é pretendido definir um parser a partir da gramática abstrata.
Decidi utilizar um lark parser para reconhecer a linguagem.
Para testar o parser, basta correr o ficheiro **grammar.py** que utiliza uma amostra de registos da linguagem (ficheiro **t.txt**).
Contudo, ainda falta reconhecer os atributos de termo tais como se o termo é masculino ou feminino, se é popular, etc...
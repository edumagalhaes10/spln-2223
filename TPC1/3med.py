import re

def remove_header_footer(txt):
    txt = re.sub(r'font="1">ocabulario.*', r'###', txt)
    txt = re.sub(r'.*\n###\n.*\n',r'###___\n',txt)
    txt = re.sub(r'<page.*\n|</page>\n',r'',txt)

    return txt

def removeLixo(txt):
    txt = re.sub(r'<\?xml.*\n', r'', txt)
    txt = re.sub(r'<!DOCTYPE.*\n\n', r'', txt)
    txt = re.sub(r'</?pdf2xml.*\n', r'', txt)
    txt = re.sub(r'<fontspec.*\n', r'', txt)
    txt = re.sub(r'<text.*(font=".*">)(.*)</text>', r'\1\2', txt)
    txt = re.sub(r'font=".*">\s*\n', r'', txt)
    txt = re.sub(r'font=".*"><b>\s*</b>\n', r'', txt)
    txt = re.sub(r'font=".*"><i>\s*</i>\n', r'', txt)
    txt = re.sub(' +', ' ', txt)

    return txt


def correctMistakes(txt):
    txt = re.sub(r'(font=".*">\s*.*)\nfont="(14|15)">(.*)', r'\1\3',txt)
    txt = re.sub(r'(font=".*">)<i>(.*)</i><i>(.*)</i>', r'\1\2\3', txt)

    return txt

def tagER(txt):
    txt = re.sub(r'font="(3|10|11)">(<i>)?<b>\s*(\D*)</b>(</i>)?',r'###R \3', txt)

    return txt

def tagEC(txt):
    txt = re.sub(r'font="2">\s*(\d+.*)\nfont="3"><b>\s*(.*)</b>', r'###C \1\2', txt)
    txt = re.sub(r'font="3"><b>\s*(\d+\s.*)</b>',r'###C \1', txt)
    txt = re.sub(r'font="12">\s*(\d.*)',r'###C \1', txt)

    return txt

def correctEC(txt):
    txt = re.sub(r'(###C.*)\nfont="3"><b>(.*)</b>\n', r'\1\2\n', txt)
    txt = re.sub(r'(###C.*)\nfont="10"><i><b>(.*)</b></i>\n', r'\1\2\n', txt)
    txt = re.sub(r'(###C.*)\nfont="13"><b>(.*)</b>\n', r'\1\2\n', txt)

    while re.search(r'(###C.*)\n###R(.*\n)', txt):
        txt = re.sub(r'(###C.*)\n###R(.*\n)', r'\1\2', txt)

    txt = re.sub(' +', ' ', txt)

    return txt

def correctER(txt):
    while re.search(r'(###R.*)\n###R (.*\n)', txt):
        txt = re.sub(r'(###R.*)\n###R(.*\n)', r'\1\2', txt)

    txt = re.sub(r'(###R.*)\nfont="10"><i><b>(.*)</b></i>\n', r'\1\2\n', txt)
    txt = re.sub(r'(###R.*)\nfont="13"><b>(.*)</b>', r'\1\2', txt)
    txt = re.sub(r'font=".*"><b>(.*)<\/b>\n(Vid\..*)\n', r'###R \1\n\2', txt)
    return txt

def tagArea(txt):
    txt = re.sub(r'(###C.*\n)font="6"><i>(.*)</i>',r'\1#Area \2', txt)
    txt = re.sub(r'(#Area.*\n)font="6"><i>(.*)</i>',r'\1#Area \2', txt)

    return txt 

def tagTraducao(txt):
    txt = re.sub(r'font="0">(.*)',r'@\1', txt)
    txt = re.sub(r'@(;)',r'=\1', txt)
    txt = re.sub(r'font="7"><i>(.*)</i>',r'= \1', txt)

    while re.search(r'(=.*)\n=(.*)\n',txt):
        txt = re.sub(r'(=.*)\n=(.*)\n', r'\1\2\n', txt)

    return txt

def cleanFontVid(txt):
    txt = re.sub(r'font="[0,5]">\s*(Vid\.-?.*)',r'\1', txt)    
    txt = re.sub(r'(Vid\.-.*)\nfont="5">(.*)\n', r'\1\2\n', txt)
    txt = re.sub(r'(Vid\.-.*)\nfont="6"><i>(.*)</i>?\n', r'\1\2\n', txt)


    return txt

def notasSinVar(txt):
    while re.search(r'font="9">.*\nfont="9">.*\n',txt):
        txt = re.sub(r'font="9">(.*)\nfont="9"(.*)\n', r'\1\2', txt)
   
    while re.search(r'font="5">.*\nfont="5">.*\n',txt):
        txt = re.sub(r'font="5">(.*)\nfont="5">(.*)\n', r'\1\2\n', txt)

    txt = re.sub(r'@\s*(VAR\.-.*)\n', r'\1\n', txt)

    txt = re.sub(r'font="9">(.*)\n', r'\1\n', txt)
    txt = re.sub(r'font="5">(.*)\n', r'\1\n', txt)
    
    return txt

def correctStuff(txt):
    txt = re.sub(r'font="7">(.*)',r'= \1', txt)
    txt = re.sub(r'(.*)\nfont="6"><i>(.*)</i>', r'\1 \2', txt)
    txt = re.sub(' +', ' ', txt)
    # txt = re.sub(r'^\s+',r'',txt)

    return txt

f = open('medicina.xml')
txt = f.read()

txt = removeLixo(txt)

txt = remove_header_footer(txt)

txt = correctMistakes(txt)

txt = cleanFontVid(txt)

txt = tagEC(txt)

txt = tagER(txt)

txt = correctEC(txt)

txt = correctER(txt)

txt = tagTraducao(txt)

txt = tagArea(txt)

txt = notasSinVar(txt)

txt = correctStuff(txt)


def storeER(e, page, dicR):
    aux = re.split("\n",e)
    dicR[aux[0].strip()] = {"definição":aux[1].strip(), "página":page}
    # print(page)
    # print(aux[:-1])

    return dicR

def storeEC(e, page, dicC):
    aux = re.split("\n",e)
    # print(aux)
    info = {}
    for i,elem in enumerate(aux):
        # print(elem)
        if i==0:
            # print(elem)
            numero_indice = elem[0]
            # print(numero_indice)
            termo = elem[1:-1].strip()
            # print(termo)
            gender = elem[-1]
            # print(gender)
            info["número_índice"] = numero_indice
            info["género"] = gender
            info["página"] = page
            # dicC[termo] = info
       
        # res = re.search(r'#Area (.*)',elem)
        # info["área"] = res.group(1)
        
        dicC[termo] = info

    # print(page)
    # print(aux)

    return dicC


def storeInfo(txt):

    dicR = {}
    dicC = {}
    page = 20
    entradas = re.split("###",txt)
    entradas=entradas[1:]
    # print(entradas)

    for e in entradas:
        if e == '___\n':
            page +=1
            # print(page)
        elif e[0] == 'R':
            dicR = storeER(e[1:-1].strip(),page,dicR)
        elif e[0] == "C":
            # print(e[1:].strip())
            dicC = storeEC(e[1:].strip(),page,dicC)
    
    # print(dicR)
    # print(dicC)

storeInfo(txt)

print(txt)
import argparse
from glob import glob

from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string 

parser = argparse.ArgumentParser(
    prog="Cria Modelo",
    epilog="Made for SPLN 22/23"
)

parser.add_argument("dir")
parser.add_argument("--epochs", "-e", default=5)
parser.add_argument("--vec_size", "-v", default=300)
parser.add_argument("--out", "-o", default="./model")

args = parser.parse_args()
dir = args.dir
files = glob(f"{dir}/*.txt")
print(files)

epochs = int(args.epochs)
vec_size = int(args.vec_size)
out = args.out


#Preprocessing
punct = string.punctuation +'\n' +"—" + "–" + "..."
stop_w = stopwords.words("portuguese")


sentences = []

for file in files:
    print(file)
    #, encoding = 'latin1'
    with open(file,'r') as f:
        #f = open(book,'r')
        txt = f.read()

    sent_tokenized_text = sent_tokenize(txt)

    for sent in sent_tokenized_text:
        words = word_tokenize(sent)
        words = [w.lower() for w in words if (w.lower() not in punct and w.lower() not in stop_w) ]
        sentences.append(words) 



model = Word2Vec(sentences, vector_size = vec_size,epochs=epochs)
model.save(out+".vec")

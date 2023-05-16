import argparse
import gensim
from gensim.models import Word2Vec

parser = argparse.ArgumentParser(
    prog="Teste de Analogias",
    epilog="Made for SPLN 22/23"
)

parser.add_argument("model")
parser.add_argument("--analogias", "-a")
parser.add_argument("--similar", "-s")



args = parser.parse_args()

modelName = args.model
if args.analogias:
    analogias = args.analogias
else:
    analogias = "val.txt"

if args.similar:
    sim = args.similar
else:
    sim = "sim.txt"

model = Word2Vec.load(modelName)

fd = open(analogias, 'r')

if analogias:
    fd = open(analogias, 'r')
    for line in fd:
        words = line.split()
        if len(words) == 3:
            w1, w2, w3 = words
            print(f"Analogia: {line}\n",model.wv.most_similar(positive=[w1.lower(),w3.lower()], negative=[w2.lower()]))
            print("*"*50)


if sim:
    fd = open(sim, 'r')
    for line in fd:
        words = line.split()
        if len(words) == 3:
            w1, w2, w3 = words
            print(f"Similaridade: {w1} - {w2}\n",model.wv.similarity(w1.lower(),w2.lower()))
            print(f"Similaridade: {w1} - {w3}\n",model.wv.similarity(w1.lower(), w3.lower()))
            print("*"*50)


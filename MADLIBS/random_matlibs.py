import imp
from sample_madlibs import code, hp, hungergames
import random

if __name__== "__main__":
    m = random.choice([code, hp, hungergames])
    m.madlib()
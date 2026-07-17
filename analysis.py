import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pricesFile = "./prices.txt"

def loadPrices(fn):
    """
    Load prices from csv file (one instrument per column) and transpose into one instrument per row
    """
    global nt, nInst
    df = pd.read_csv(fn, sep=r"\s+", header=0, index_col=None)
    nt, nInst = df.shape
    return (df.values).T

prcAll = loadPrices(pricesFile)

plt.plot(prcAll[40])
plt.show()
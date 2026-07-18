import numpy as np

nInst=51
currentPos = np.zeros(nInst)
def getMyPosition (prcSoFar):
    global currentPos
    (nins,nt) = prcSoFar.shape

    long_window = 50
    short_window = 20
    if (nt < long_window):
        return np.zeros(nins)
    
    recent = prcSoFar[:,-long_window:]
    short_rec = prcSoFar[:,-short_window:]
    ma = recent.mean(axis=1)
    sma = short_rec.mean(axis=1)

    # lastRet = np.log(prcSoFar[:,-1] / prcSoFar[:,-2])
    # lNorm = np.sqrt(lastRet.dot(lastRet))
    # lastRet /= lNorm

    last_price = prcSoFar[:,-1]
    dev = ma - sma #dev is positive if current price is below average/should buy

    norm = np.sqrt(dev.dot(dev)) 
    if norm != 0:
        dev /= norm


    rpos = np.array([int(x) for x in 5000 * dev / prcSoFar[:,-1]])
    currentPos = np.array([int(x) for x in currentPos+rpos])
    return currentPos

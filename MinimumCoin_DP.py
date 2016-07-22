

def changedp(V,A):

    subTable = [0] * (A + 1) # to hold running minimum coin counts
    n = len(V)
    coinsAdd = [0] * (A + 1)  # to hold coins that are used during through amounts
    #denomination = [0] * (A+1)  # to hold the denominations -- need to figure out how to size this better..

    # do I need to check for 0 coming through in V?

    if (n == 0 or A == 0 or V[0] == 0):
        return 0;

    for currCents in range(A+1):
        coinCount = currCents
        currCoin = 1

        subprob = float("inf")

        for j in V:
            if j <=currCents:     #if coinval is <=current cents then not enough to do anything so it skips back up to prev. line
                if subTable[currCents-j] + 1 < coinCount:
                    subprob = min(subprob, subTable[currCents-j]+1)
                    coinCount = subprob
                    currCoin = j
        subTable[currCents] = coinCount #add to table used to get minimum coins
        coinsAdd[currCents] = currCoin  #add current coin denomination to table for later traceback

    # print for debugging only
    #print subTable
    #print coinsAdd  # coins added for each change in amount 1....n
    #print subTable[A]  # minimum coins in last element of calc subTable


    #get counts of each denomination
    cnt = 0
    denomination = [0] * (A+1)
    currAmt = A
    while currAmt > 0:
        denomination[cnt] = coinsAdd[currAmt]
        currAmt = currAmt - coinsAdd[currAmt]
        cnt = cnt+1
    #print denomination  #actual coins used # print for debugging only
    # now sum them up against original list
    countArray = [0] * (n)
    cntIndx = 0
    for m in V:
        for n in denomination:
            if n == m:
                countArray[cntIndx] = countArray[cntIndx] + 1
        cntIndx = cntIndx + 1

    print "Minimum coins needed to make change of" , A ,": " , subTable[A]
    print "Denominations of " , V , " needed: " , countArray, "\n"



    return countArray, subTable[A]




print "minimumCoins (dp):"
changedp([1,3,4],11)
changedp([1,3,4],15)
changedp([1,2,4,8],15)
changedp([1,2,4,8],16)
changedp([1,2,4,8],17)
changedp([1,3,7,12],29)
changedp([1,3,7,12],31)
#changedp([1,3,4],11)  #shorter one at end to test time...


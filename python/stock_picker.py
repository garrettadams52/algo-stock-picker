from json.encoder import INFINITY


def picker(prices):
    ans = [None, None]
    diff = 0
    for i,val in enumerate(prices):
        for j,vals in enumerate(reversed(prices)):
            k = len(prices)-1-j
            #print(i,k,val,vals)
            if k > i and vals - val > diff:
                diff = vals - val
                ans = [i, k]

    #print(diff)
    return ans

#print(picker([17,3,6,9,15,8,6,1,10]))
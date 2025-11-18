def findMinDifference( timePoints):
    min=2000
    for i in range(len(timePoints)):
        hi,mi=tuple(map(lambda x:int(x),timePoints[i].split(":")))
        for j in range(len(timePoints)):
            if i==j:
                continue
            hj,mj=tuple(map(lambda x:int(x),timePoints[j].split(":")))
            hd=abs(hi-hj)
            if hd>12:
                hd=24-hd
            hd*=60
            totmd=abs(hd-mi+mj) if timePoints[i]<timePoints[j] else 2000
            if min>totmd:
                min=totmd
    return min
print(findMinDifference(["01:01","02:02"]))
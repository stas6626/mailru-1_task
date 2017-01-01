def solution(a):
    maximum=0
    dlinna=len(a)
    for i in range(0,dlinna-13):
        poditog=1
        for j in range(0,13):
            poditog*=int(a[i+j])
        
        if poditog>maximum:
            maximum=poditog
    return maximum
        

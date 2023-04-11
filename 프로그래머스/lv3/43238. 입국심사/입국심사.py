def finish(minute,times):
    done=0
    for time in times:
        done+=minute//time
    return done

def solution(n, times):
    l=0
    r=max(times)*(n//len(times)+1)
    while l<=r:
        mid= (l+r)//2
        if finish(mid,times) == n:
            r=mid
            if l==r:
                break
        elif finish(mid,times) < n:
            l=mid+1
        else:
            r=mid-1
    return mid

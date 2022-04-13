def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
        
    counts,window={},{}
    for i in range(len(s1)):
        counts[s1[i]] = 1 + counts.get(s1[i],0)
    need = len(counts)
    print(need)
        
    have = 0
    l = 0
    for r in range(len(s2)):
        print(r)
        window[s2[r]] = 1 + window.get(s2[r],0)
            
        if s2[r] in counts and window[s2[r]] == counts[s2[r]]:
            have += 1
            print(have)
        if r - l + 1 >len(s1):
                
            if s2[l] in counts and window[s2[l]] == counts[s2[l]]:
                have -= 1
                print(f'have:{have}')
            window[s2[l]] -= 1
            l += 1
        print(f'l:{l}')    
        if have == need:
            return True
    return False
                
s1='ab'
s2='eidboaoo'

print(checkInclusion(s1,s2))

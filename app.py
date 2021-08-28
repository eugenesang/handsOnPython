def permute(s, answer='', ans=[]):
    if len(s)==0:
        ans.append(answer)
        return 
    
    for i in range(len(s)):
        ch=s[i]
        left_substr=s[0:i]
        right_substr= s[i+1:]
        rest=left_substr+right_substr

        permute(rest, answer+ch, ans)


def permutation(string):
    num=[]
    permute(string,'',num )
    return num

def unrepeatedPermutation(string):
    arr=permutation(string)
    ret=[]
    for i in arr:
        if not ret.__contains__(i):
            ret.append(i)
    return ret

print(len(permutation("eugene")))
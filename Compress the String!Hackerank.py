"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

"""

s=list(map(int,input()))
l=[]
i=0
while(i!=len(s)):
    count=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            count+=1
        else:
            break
    l.append((count,s[i]))
    i+=count
print(*l)
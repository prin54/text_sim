"""
Created on Thu Jan  9 09:01:38 2020

@author: Rohan Suri

Problem Statement 
__________________
Given a single domain and a list of random domain names, find which are the closest match in the list, 
Example: Given input domain:google.com and domain list: [thegoogle.com, good.go, google.co.in, bing.com] will closely matches with thegoogle.com, good.go, google.co.in but not bing.com. Example google .com matches 100% with google.com

Input: domain and list of the domain with which you will match the  domain
Output: Floating Point/Decimal or Percentage value of Single Domain Matches with the other domains within the domain list.
Partial Acceptable Solution: None (If its a match or not is not acceptable)
Complete solution: Giving output in floating-point/decimals as prediction from  0-1 or 0%-100% with each domain in the domain list.

"""



#default
domain_list= ['thegoogle.com', 'good.go', 'google.co.in', 'bing.com','google.com'] 
domain="google.com"


domain = input("Enter base domain: ")
len_domain_list = int(input("Enter no of domains to match: "))
print("Enter",len_domain_list,"domains:")
domain_list=[]
for _ in range(len_domain_list):
    domain_list.append(input())
print()
    
from difflib import SequenceMatcher
def edit_distance(str1, str2):
    s = SequenceMatcher(None, str1, str2)
    a = s.get_opcodes()
    edist = 0
    for i in a :
        if(i[0]!="equal"):
            if(i[0]=="insert"):
                edist += i[4] - i[3]
            elif(i[0]=="delete"):
                edist += i[2] - i[1]
            elif(i[0]=="replace"):
                edist += i[2]-i[1]
    return(edist)

def compute_similarity(str1, str2):
    n=edit_distance(str1, str2)
    d=max(len(str1),len(str2))
    similarity = 1 - (n/d)
    return(similarity)

print("Similarity Scores with",domain)
for str2 in domain_list:
    score= round(compute_similarity(domain, str2), 3)
    print(str2,score)

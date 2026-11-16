# num = [10,20,40,50,30]
# print(max(num))


# word = "xyz"
# def freq_cal(word):
#     empt_dict ={}

#     for i in word:
#         if i in empt_dict:
#             empt_dict[i] +=2
#         else:
#             empt_dict[i] = 5
#     else:
#         empt_dict[i] = 9
        
#     return empt_dict 
# print(freq_cal(word))

# d="python is  easy python is hard"
# words = d.split()
# for word in set(words):
#     print(word,words.count(word))

d="python is  easy and python is hard"
words=d.lower().split()
count={}
for words in words:
    if words in count:
        count[words]+=1
    else:
        count[words]=1
print(count)


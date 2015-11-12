char_str = "first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!"

list_str = list(char_str)
dict_str = {}

#转换成字典
for temp in list_str:
    if temp in dict_str:
        dict_str[temp] = dict_str[temp] + 1
    else:
        dict_str[temp] = 1
print (dict_str)

#key与values反转
dict_change = {}
for temp in dict_str:
    if dict_str[temp] in dict_change:
        if isinstance(dict_change[dict_str[temp]],str):
            dict_change[dict_str[temp]] = list(dict_change[dict_str[temp]])
            (dict_change[dict_str[temp]]).append(temp)
            
        else:               
            (dict_change[dict_str[temp]]).append(temp)        
    else:
        dict_change[dict_str[temp]] = temp

print (dict_change)

list_keys = list(dict_change.keys())
print (list_keys)

#冒泡排序:字符出现的次数
for i in range((len(list_keys) - 2),0,-1):
    j = len(list_keys) - 2
    while j >= 0:
        if list_keys[j] < list_keys[j+1]:
            list_keys[j],list_keys[j+1] = list_keys[j+1],list_keys[j]
        j -= 1
#打印结果
i = 0
for temp in list_keys:
    if i > 9 :
        break
    if isinstance(dict_change[temp],list):
        i = i + len(dict_change[temp])
    else:
        i += 1
    print ('top %d ,count is %d,character is %s' %(i,temp,dict_change[temp]))

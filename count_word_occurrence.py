#the given sentence 
sentence = "To change the overall look of your document. To change the look available in the gallery"

#split the sentence into words
sentence1=sentence.split()
#an empty list to store the words without duplication
words=[]
#an empty list to store the count of each word
count=[]
#run a loop which traverse all the words in sentence
for w in sentence1:
    #if word is not in words list then append that word into list and append 1 into count list because that word is appears first time
    if w not in words:
        words.append(w)
        count.append(1)
   #if the word is already in the list 'words' then we simply just increase the count of that word in the 'count' list at the corresponding index of that word in the 'words' list
    else:
        index=words.index(w)
        count[index]=count[index]+1
#display the count of each word
print("The count of each word is : ")
for i in range(0,len(words)):
    print(words[i],"=",count[i])
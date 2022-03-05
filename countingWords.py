introString=input("enter string:")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1
        
        print("number of words in the strings:")
        print(wordCount)
        print("number of characters in the strings:")
        print(characterCount)

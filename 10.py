def count(word):
    v_count=0
    c_count=0
    for i in word:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            v_count+=1
        else:
            c_count+=1
    print("vowel:",v_count)
    print("Consonants:",c_count)
word=input("enter the string: ")
count(word)

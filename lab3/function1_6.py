#Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def inverted_sentence():
    snt = list(input("Enter the sentence: ").split())
    snt.reverse()
    print(*snt)

inverted_sentence()
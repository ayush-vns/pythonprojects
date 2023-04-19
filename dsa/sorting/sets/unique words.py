paragraph = """
In this article, I’d like to reacquaint you with the humble workhorse of communication that is the paragraph. Paragraphs are everywhere. In fact, at the high risk of stating the obvious, you are reading one now. Despite their ubiquity, we frequently neglect their presentation. This is a mistake.

"""
print(paragraph)
listofwords=paragraph.split()
print(listofwords)
uniquewords=set(listofwords)
print(uniquewords)
print(len(uniquewords))
print(len(listofwords))
repeatedwords=listofwords.copy()
for ch in uniquewords:
    repeatedwords.remove(ch)
print(repeatedwords)
print(uniquewords.difference(repeatedwords))

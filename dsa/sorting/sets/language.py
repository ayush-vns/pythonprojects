English = {'a', 'b', 'd', 'e'}
Hindi = {'b', 'c', 'e', 'f'}
Chinese = {'d', 'e', 'f', 'g'}
print(English, Hindi, Chinese)
StudentsKnowingHindiEnglishChinese = English.intersection(Hindi).intersection(Chinese)
print(StudentsKnowingHindiEnglishChinese)
StudentsKnowingEnglishOnly = English.difference(Chinese).difference(Hindi)
print(StudentsKnowingEnglishOnly)
AllStudents = English.union(Hindi).union(Chinese)
print(AllStudents)

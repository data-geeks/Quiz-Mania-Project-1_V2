import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='xmltest.xml')
root = tree.getroot()
for elem in root:
    question = elem[0].text
    option1 = elem[1].text
    option2 = elem[2].text
    option3 = elem[3].text
    option4 = elem[4].text
    answer = elem[5].text
    print(f'''
    Question: {question}
    A : {option1}
    B : {option2}
    C : {option3}
    D: {option4}
    ''')

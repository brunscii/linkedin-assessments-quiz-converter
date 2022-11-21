with open('js.md','r') as fs:
    questions = []
    answers = []
    qBuffer = ''
    aBuffer = ''
    qBuff = False
    aBuff = False

    for line in fs:
        if(line.startswith('####')):
            #question begins
            if aBuffer != '':
                answers.append(aBuffer)
            aBuff = False
            aBuffer = ''
            qBuffer = line
            qBuff = True

        elif line.startswith('- [ ]'):
            #answer is found
            if aBuffer != '':
                if aBuffer.find('```') :
                    answers.append(aBuffer.replace('```','<code>').replace('```','</code>'))
                else:
                    answers.append(aBuffer)
                # aBuffer = line
            if qBuff:
                questions.append(qBuffer)
                qBuffer = ''
                qBuff = False
            aBuff = True
            aBuffer = line

        elif line.startswith('- [x]'):
            #actual answer
            if aBuffer != '':
                answers.append(aBuffer)
                # aBuffer = line
            if qBuff:
                questions.append(qBuffer)
                qBuffer = ''
                qBuff = False
            aBuff = True
            aBuffer = line
        elif qBuff:
            qBuffer += line

    htmlTest = ''

    for i in range(0, len(questions)):
        temp = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="style.css"><title>Document</title></head><body><div>'
        temp += questions[i].replace('#### ', '<label class="question">').replace('?','?</label>')
        if (i * 4 + 3) > len(answers)-1:
            break
        temp += answers[(i*4)].replace('- [x]', '<button class="correct-answer">"') + ('"</button>') if answers[(i*4)].startswith('- [x]') else answers[(i*4)].replace('- [ ]', '<button class="wrong-answer">"') + ('"</button>')
        temp += answers[(i*4)+1].replace('- [x]', '<button class="correct-answer">"') + ('"</button>') if answers[(i*4)+1].startswith('- [x]') else answers[(i*4)+1].replace('- [ ]', '<button class="wrong-answer">"') + ('"</button>')
        temp += answers[(i*4)+2].replace('- [x]', '<button class="correct-answer">"') + ('"</button>') if answers[(i*4)+2].startswith('- [x]') else answers[(i*4)+2].replace('- [ ]', '<button class="wrong-answer">"') + ('"</button>')
        temp += answers[(i*4)+3].replace('- [x]', '<button class="correct-answer">"') + ('"</button>') if answers[(i*4)+3].startswith('- [x]') else answers[(i*4)+3].replace('- [ ]', '<button class="wrong-answer">"') + ('"</button>')
        # temp += answers[(i*4)-2]
        # temp += answers[(i*4)-1]
        # temp += answers[(i*4)]
        htmlTest += temp + '</div><script type="text/javascript" src="script.js"></script></body></html>'
    print(htmlTest)
    with open('jsTest.html','w') as fw:
        fw.writelines(htmlTest)




# with open('js.md','r') as fs:
#     questions,answers = [],[]
#     qBuffer, aBuffer = False
#     for line in fs:
#         if line.startswith('####'):
#             questions.append(line)
#             qBuffer = True
#             aBuffer = False
#         if line.startswith('- [ ]') or line.startswith('- [x]'):
#             #This is where we start reading in the answer
#             aBuffer = True
#             if(aBuffer):
#                 answers.append(qBuffer)
#             qBuffer = line
        
#     print(len(answers))
#     for l in answers:
#         print(answers.index(l),l)
            # answers.append(line)
                # print(line)
    # print(len(questions))
    
        





# answers = []
# qs = []
# testAnswers = []



# for question in test:
#     if question.startswith('####'):
#         qs.append(question.replace('#### ',''))
#     else:
#         if question.startswith( '- [x] '):
#             print(test.index(question))
#             answers.append(question.replace('- [x]',''))
#         else: 
#             testAnswers.append(question.replace('- [ ] ',''))
            
# print(answers)

# for i in range(len(qs)):
#     print(i+1)
#     print(qs[i])
#     print(answers[i])
# print(testAnswers)
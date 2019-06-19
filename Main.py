# authors Wiljam Rautiainen, Johan Erlandson.
#This code will use python 3.7.
#Please find that your folder structure is correct if code isnt working
#Use the folder structure what is in the project
#This is the main program that does the analysising, we format our data other code files.
#To see all the print run the Main.py
#in the project folder we also have a file that contains all the prints of the program its called answer.txt
#please find that you have to use our virtual enviroment, you can dowlnload our eniroment by using
#pip install -r reg.txt


import NewCode
import csv
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
#please install
#nltk.download('vader_lexicon')

##getting the result 0 = timeBefore, 1 = interface, 2 = timeafter , 3=textBefore, 4 = textAfter

def main():
    #Please find that i = 1 because our file structure
    i =1
    while i < 5:
        numb = str(i)
        data = NewCode.main('data' + numb)
        A = calc(data[0])  ## intrface A
        B = calc(data[2])  ## interface B
        Q6(data[3],data[5])
        print("AVG before", sum(A) / len(A),data[1])
        print("AVG after", sum(B) / len(B))
        print("Talking same time After ",instace(data[3], data[5]))
        print("Talking same time Before ", instace(data[4], data[6]))
        print("_______________________________________________")
        index = str(i) + "/"
        #This will transform the data to 2 parts in text file
        writeTxt(data[3], data[5],index,"before")
        writeTxt(data[4], data[6], index, "after")
        i +=1
    print("All the Conversations that are Before when the interface is changing")
    analyData("/before")
    print("----------------------------------------------------")
    print("All the Conversations that are After when the interface is changing")
    analyData("/after")



def Q6(A,B):
    posNeg = []
    right = 0
    wrong = 0
    i = 0
    while i < len(A):
        text = A[i] + B[i]
        str1 = ''.join(text)
        words = word_tokenize(str1)
        stopWords = set(stopwords.words('english'))
        wordsFiltered = []
        ## filtering stop words
        for w in words:
            if w not in stopWords:
                wordsFiltered.append(w)

        ps = PorterStemmer()
        ## filtering stemming
        stemmed_words = []
        for w in wordsFiltered:
            stemmed_words.append(ps.stem(w))
        sid = SentimentIntensityAnalyzer()
        pos_word_list = []
        neu_word_list = []
        neg_word_list = []

        for word in stemmed_words:
            if (sid.polarity_scores(word)['compound']) >= 0.2:
                pos_word_list.append(word)
            elif (sid.polarity_scores(word)['compound']) <= -0.2:
                neg_word_list.append(word)
            else:
                neu_word_list.append(word)

        #Formula is pos/neg if neutral then our index i 0
        if(len(neg_word_list) >= len(pos_word_list)):
            wrong +=1
            i += 1
            continue
        right += 1
        i += 1
    a = [wrong,right]
    posNeg.append(a)
    print("wrong / right",posNeg)



#Q1 this fucntion calulates time AVG
def calc(data):
    i = 0
    array = []
    while i < len(data):
        summ = sum(data[i])
        i += 1
        array.append(summ)
    return(array)

#Q2 this fucntion calculates how many times two people are talking same time
def instace(A,B):
    calc=0
    i = 0
    while i < len(A):
        if A[i] != '':
            if B[i] != '':
                calc +=1
        i += 1
    return calc


def sameWords(text_a,text_b):
    sum_of_copies = 0
    sum_of_copies2 = 0
    nonsplitt_a = text_a
    nonsplitt_b = text_b
    text_a = text_a.split()
    text_b = text_b.split()
    for word in text_a:
        if text_b.__contains__(word):
            sum_of_copies = sum_of_copies + 1

    print("Number of occurences of person A words in person B words:", sum_of_copies)

    for word2 in text_b:
        if text_a.__contains__(word2):
            sum_of_copies2 = sum_of_copies2 + 1

    print("Number of occurences of person B words in person A words:", sum_of_copies2)

    #analysing emotianla synchrony
def Q5(data):
    words = word_tokenize(data)
    stopWords = set(stopwords.words('english'))
    wordsFiltered = []
    ## filtering stop words
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    ps = PorterStemmer()
    ## filtering stemming
    stemmed_words = []
    for w in wordsFiltered:
        stemmed_words.append(ps.stem(w))
    sid = SentimentIntensityAnalyzer()
    pos_word_list = []
    neu_word_list = []
    neg_word_list = []

    for word in stemmed_words:
        if (sid.polarity_scores(word)['compound']) >= 0.2:
            pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.2:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)

    if(len(neg_word_list) >= len(pos_word_list)):
        return False

    return True





#This fucntion uses python nltx library to do sentimental analyzing
def analyData(name):
    i = 1
    poscount = 0
    negcount = 0
    while i < 5:
        f = open("CleanedText/" + str(i) +name + ".txt", "r")
        ff = open("CleanedText/" + str(i) + name + "2" + ".txt", "r")
        text = f.read()
        text1 = ff.read()
        data = str(text) + str(text1)
        #Emotianla synchrony
        if(Q5(text) == Q5(text1)):
            print("Conversation is emotianally sync")
        else:
            print("Conversation is  NOT emotianally sync!")
        sameWords(str(text),str(text1))
        words = word_tokenize(data)
        stopWords = set(stopwords.words('english'))
        wordsFiltered = []
        ## filtering stop words
        for w in words:
            if w not in stopWords:
                wordsFiltered.append(w)

        ps = PorterStemmer()
        ## filtering stemming
        stemmed_words = []
        for w in wordsFiltered:
            stemmed_words.append(ps.stem(w))
        sid = SentimentIntensityAnalyzer()
        pos_word_list = []
        neu_word_list = []
        neg_word_list = []
        # This is our own calculation Q7
        fdist1 = FreqDist(stemmed_words)
        print("Most common words in conversation", fdist1.most_common(5))

        for word in stemmed_words:
            if (sid.polarity_scores(word)['compound']) >= 0.2:
                pos_word_list.append(word)
            elif (sid.polarity_scores(word)['compound']) <= -0.2:
                neg_word_list.append(word)
            else:
                neu_word_list.append(word)

        print('Positive count :', len(pos_word_list), pos_word_list)
       # print('Neutral count:', len(neu_word_list))
        print('Negative count :', len(neg_word_list), neg_word_list)
        print("_-------------------------------------------------------")
        i += 1
        poscount += len(pos_word_list)
        negcount += len(neg_word_list)
    return







#This function cleans our data to better format and saves it as .txt file
def writeTxt(A,B,index,name):
    arrA = []
    arrB = []
    i = 0
    while i < len(A):
        arrA += A[i]
        arrB += B[i]
        i +=1
    str1 = ''.join(arrA)
    a =str1.replace('/s',' /s ')
    a = a.replace('/d', ' /d ')
    a = a.replace('?', '? ')
    str2 = ''.join(arrB)
    b = str2.replace('/s', ' /s ')
    b = b.replace('/d', ' /d ')
    b = b.replace('?', '? ')
    f = open("CleanedText/" + index + name +".txt", "w+")
    f.write(a)
    f.close()
    f = open("CleanedText/" + index + name + "2" + ".txt", "w+")
    f.write(b)
    f.close()
    return


main()
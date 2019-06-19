#This file purpose is just clean data better format. it will return data that has multiple attributes inside
#Authors Wiljam Rautiainen, Johan Erlandson
import Split

def splitString(path,split):
    file = open(path, 'r')
    for line in file.readlines():
        fname = line.rstrip().split('¦')  # using rstrip to remove the \n
        i = 0
        index = []
        while i < len(fname):
            if fname[i] == '/' and fname[i + 1] == split:  # rememnber to chech that not going to overbounds!!!!!!
                index.append(i)
            if fname[i] == '/' and fname[i + 2] == split:  ## data is bad so we have to do this
                index.append(i)
            i += 1

        return(index,fname)

# return the splitted time
def splitTime(list,time):
    k = 0
    finalTime = []
    for i in list:
        piece = time[k:i]
        k = i
        finalTime.append(piece)

    return finalTime

# takes text, index returns splitted text
def splitText(text,index):
    array = []
    old = 0
    for i in index:  # split using index
        slice = text[old:i]
        array.append(slice)
        old = i
    return (array)

#takes data and returns the index where to split
def splitInterface(data,split):
    calc = 0
    i = 0
    while i < len(data):
        calc += len(data[i])
        if calc >= split:
            return(i)
        i += 1

def main(path):
    A = splitString('data/' + path +'/PersonA.txt','s')
    A1 = splitString('data/' + path +'/PersonA.txt','d')
    B = splitString('data/' + path +'/PersonB.txt','s')
    B1 = splitString('data/' + path +'/PersonB.txt','s')
    final = A[0] + B[0] + A1[0] + B1[0]
    final = [int(x) for x in final]
    # Now our array is order
    final.sort()
    file = open('data/' + path + '/Time.txt', 'r')
    for line in file.readlines():
        time = line.rstrip().split('¦')  # using rstrip to r
        time = [0 if x=='' else x for x in time]
        time = [int(x) for x in time]
    ### doing something ############################
    time = splitTime(final,time) #this retusn time in conversation
    splittedA = splitText(A[1],final) # returns splittes conversation
    splittedB = splitText(B[1], final)  # returns splittes conversation
    split_index = Split.splitter_function('data/' + path)
    index = splitInterface(splittedA,split_index[0])  # return index where iterface is changing
    return(time[0:index],split_index[1],time[index:len(time)], splittedA[0:index],splittedA[index:len(splittedA)],splittedB[0:index],splittedB[index:len(splittedA)])




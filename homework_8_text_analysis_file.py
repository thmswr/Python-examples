'''
Написать программу которая открывает текстовый файл и считает следующее:
1. Общее кол-во слов
2. Кол-во уникальных (разных)

Не влияет на уникальность:
Заглавные и прописные буквы
Знаки препинания: ',' '.' '!' '?'

Сохраняет кол-ва в отдельный файл.
Выписывает все уникальные слова в алфавитном порядке (по одному слову в строке).

'''
import datetime  #export datetime to include time to analysis output file

#Open file  to analyse the text inside
with open("228.txt", 'r', encoding='utf-8') as file:  #open file in readonly mode
    data = file.read()  #read file to string
    data = data.lower()  #get rid of capital letters

#calculate total words

#method 1 - FOR cycle utilisation.

    count = 0  #set word counter
    flag = 0  #set flag Low initially
    for i in range(len(data)):  #when i is from 0 until the number of symbols in string DATA. 4866 symbols in total.
        if data[i] != ' ' and flag == 0:  #if indexed symbol (index increments from counter) is not equal ' '(space) and flag is Low
            count += 1  #increment Words counter
            flag = 1  #hoist the Flag up!
            #when word has begun next iteration (i+1) will face condition when flag is no more = 0, so counter would not be incremented
        else:  #until next space will be read by code below and lower the flag.
            if data[i] == ' ':  #if indexed symbol is space
                flag = 0  #lower the flag
    print(f'Words:{count}')  #Result is a number of words. As is. from 1 to given number.

#method 2 - conversion to list, LEN utilisation on list content

   #get rid of commas, decimals, brackets etc. Now text separated always by spaces only and lower case.
    data = data.replace('.', '')
    data = data.replace(',', '')
    data = data.replace('!', '')
    data = data.replace('?', '')
    data = data.replace(')', '')
    data = data.replace('(', '')

with open("analysis_output.txt", 'w', encoding='utf-8') as file:  #create file to write output to

    data = data.split()  #split text from string to list
    print(f'total words: {len(data)}')  #LEN method to return count of words in the list from 0 (!) to a given number, as text gives.
    file.write(f'total words count:{len(data)}'+ '\n')
    #print(type(s))  #selfcheck

#calculate unique words in the text. Changing data type to SET we get rid of duplicates. Then use LEN method.
    data = set(data)  #now data is set()
    #print(type(data))  #selfcheck
    print(f'unique words count:{len(data)}')  #return count of items in set from 0 to given number.
    file.write(f'unique words count:{len(data)}'+ '\n')

    #print(s)  #selfcheck

#write down all words in alphabetic order. Switch type back to LIST (ordered).
    data = list(data)
    print(data)
    a = sorted(data)

#utilising FOR cycle write to file each word from new line
    for i in range(len(a)):
        file.write(a[i] + '\n')
#write down timestamp of analysis
    file.write('Text analysed at: \n')
    file.write(str(datetime.datetime.now()) + '\n')


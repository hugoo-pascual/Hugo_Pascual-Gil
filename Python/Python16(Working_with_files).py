#Example
'''def read_text1():    #One way - Read text
    file = open('pangrams.txt', encoding = 'UTF-8')
    text = file.read()
    file.close()
    
    print(text)
    print("\n")

def read_text2():   #Another way - Read text
    with open('pangrams.txt', encoding = 'UTF-8') as file:
        text = file.read()
    print(text)
    print("\n")

def read_line():    #One way - Read a line
    file = open('pangrams.txt', encoding = 'UTF-8')
    text = file.readline()
    file.close()

    print(text)
    print("\n")

def read_text2():   #Another way - Read line
    with open('pangrams.txt', encoding = 'UTF-8') as file:
        text = file.readline()
    print(text)
    print("\n")

read_text1()
read_text2()
read_line()'''


#Exercise 1

'''file = open('pangrams.txt', encoding = 'UTF-8')
file.seek(10)
text1 = file.read(10)
text2 = file.read()
file.close()
print(text1, text2)'''

#Exercise 2
'''def read_line():
    with open('pangrams.txt', encoding = 'UTF-8') as file:
        text = file.readline()
    print(f'{text}\n')

read_line()'''


#Exercise 3

'''def count_words_line(a):
    with open ('pangrams.txt', encoding = 'UTF-8') as file:
        text = file.readline(a)

    for line in text:
        words = text.split()
        word_count = len(words)
    print(f'Total number of words in line: {word_count}')

lines_counted = int(input('Line to count: '))
                    
count_words_line(lines_counted)'''  # Incorrect code


'''def count_words():
    with open('pangrams.txt', encoding='UTF-8') as file:
        line_number = 1
        total = 0
        
        for line in file:
            words_per_line = len(line.split())  #Number words per line
            print(f'Line {line_number}: {words_per_line} words')
            line_number += 1
            total = words_per_line + total
        print(f'total words in the text :{total}')

count_words()''' #Correct code


#W access

'''with open('numbers.txt', 'w') as file:
    file.write('1') # = print(1, file = file)
    file.write('2') # = print(2, file = file)
    file.write('3') # = print(3, file = file)'''

#X access  almos the same as W
'''file = open('numbers.txt', 'x')
print(4, file = file)
print(2, file = file)
print(3, file = file)
file.close()'''

#A accsess
'''with open('numbers.txt', 'a') as file:
    print(100000, file = file)  #add information to the end of the file'''

#Exercise 1
'''def create_new_doc():
    with open('evens.txt', 'w') as file:
        numbers = 0
        for i in range(numbers, 11):
            file.write(f'{numbers} ')
            numbers += 2
        
create_new_doc()'''

#Excersice 2
'''with open('hello.txt', 'a') as file:
    print('Hello how are you doing this fine morning', file = file)'''



#Pickle Module
'''import pickle

def dumps_and_loads_function():
    data = ["Russia", "Canada", "China",
        "United States","Brazil","Australia",
        "India", "Argentina", "Peru"]

    bytestream = pickle.dumps(data) #Serilization
    print(bytestream)


    normal_data = pickle.loads(bytestream)  #Deserilization
    print(normal_data)

def wb_mode():
    data = ["Russia", "Canada", "China",
        "United States","Brazil","Australia",
        "India", "Argentina", "Peru"]
    
    with open('countriejs.bin','wb') as file:   #write
        pickle.dump(data, file)

    with open('countriejs.bin', 'rb') as file:  #read
        data = pickle.load(file)
        
'''#There are also more access modes, like 'xb', 'ab'...

'''dumps_and_loads_function()

wb_mode()'''

#Binary Access with Pickle
'''import pickle

with open('lists.bin', 'wb') as file:
    pickle.dump([1, 2, 3], file)
    pickle.dump([4, 5, 6], file)
    pickle.dump([7, 8, 9], file)

with open('lists. bin', 'rb') as file:
    print(pickle.load(file))
    print(pickle.load(file))
    print(pickle.load(file))'''

#Task 1 Investigations
'''with open('cities-europe.txt', encoding = 'UTF-8') as file:
    text = file.read()
    cities = 0

    for i in range(' ', ' '):
        cities += 1

print(cities)'''













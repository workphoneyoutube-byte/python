students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10001'] = 'Nia'
students_dict['X10002'] = 'Anita'

print(students_dict)         #print original dictionary

students_dict.pop("X10000")  #we remove the first entry
print(students_dict)         #print modified dictionary

person = students_dict.pop("X10001") #remove and store an entry
print(person)        #we display the element returned from the pop method
print(students_dict) #print the final dictionary to see changes

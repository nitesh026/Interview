from flask import jsonify
import MyModule as mm

def welcome(n1):
    print("welcome message in side calculator")
    return jsonify(n1)
price =49
txt = 'The price is {} dollars'
txt1 = 'The price is {:.2f} dollars'

print(txt.format(price))
print(txt1.format(price))
list_item = ['Nitesh']
list_item.append('Raju')
list_item.append('Mohit')
print(list_item)
print(mm.number_to_words(2022))




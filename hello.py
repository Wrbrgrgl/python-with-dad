#!python
#thisismyfirstpythonpogromitsays hello worlb

#favorite stuff yall
favorite_items = {'Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'Osama Bin Laden',}
my_string = "{} really loves {}!"

for person in favorite_items:
    print(my_string.format(person, favorite_items[person]))

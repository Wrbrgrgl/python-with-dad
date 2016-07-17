#!python
#thisismyfirstpythonpogromitsays hello worlb

#favorite stuff yall
favorite_items = {'Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'His spot on the couch',}
my_string = "{} really loves {}!"

for person in favorite_items:
    print(my_string.format(person, favorite_items[person]))

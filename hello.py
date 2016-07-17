#!python
#thisismyfirstpythonpogromitsays hello worlb
peoples = ['Claire', 'Alex', 'Blake', 'Dad', 'Mom']
#favorite stuff yall
favorite_items = {'Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'his spot on the couch',
                  'Mom':'napping',
                  }
my_string = "{} really loves {}!"

for person in sorted(peoples):
    if person in favorite_items.keys():
        print(my_string.format(person, favorite_items[person]))
    else:
        print "Error, {} has no favorites".format(person)

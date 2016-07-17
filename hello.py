#!python
"""thisismyfirstpythonpogromitsays hello worlb"""
from collections import defaultdict
from collections import OrderedDict


my_peoples = ['Claire', 'Alex', 'Blake', 'Dad', 'Mom']
alex_peoples = ['Alex','Blake', 'Dad,''Mom','Barthomule','Ashur']
#favorite stuff yall

peoples = set(my_peoples + alex_peoples)
only_in_alex = set(alex_peoples) - set(my_peoples)
only_in_mine = set(my_peoples) - set(alex_peoples)
all_our_people = set(alex_peoples) | set(my_peoples)

favorite_items = OrderedDict('Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'his spot on the couch',
                  'Mom':'napping',)
def fetch_misssing_data(person='Alex'):
    return "No likes found"
default_favorites = defaultdict(fetch_misssing_data, favorite_items)
my_string = "{} really loves {}!"
favorites = []
def main():
    tally_the_data()

def tally_the_data():
    for person in sorted(peoples):
        try:
            favorites.append(my_string.format(person, favorite_items[person]))
        except KeyError:
            favorite_items[person] = fetch_misssing_data(person)
        print(my_string.format(person, favorite_items[person]))


if __name__ == '__main__':
    main()

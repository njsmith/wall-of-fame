import sys
from pprint import pprint
import pickle

from wall_of_fame import get_heroes

def main():
    heroes = get_heroes("python-trio", exclude_repos=["trio-amqp"])
    pprint(heroes)
    pickle.dump(heroes, open("trio-heroes.pickle", "wb"), protocol=-1)

if __name__ == "__main__":
    main(*sys.argv[1:])

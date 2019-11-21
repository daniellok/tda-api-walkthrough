import pickle

with open("token.pickle", "rb") as pickle_test:
    content = pickle.load(pickle_test)

print(content)
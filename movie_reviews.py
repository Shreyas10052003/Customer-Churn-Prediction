import pickle

with open('stored_data.pkl', 'rb') as pickle_file:
    reviews = pickle.load(pickle_file)
    print("Data loaded successfully:", reviews)  # Optional: Print to verify


import pickle

# Read sav

with open('finalized_model.sav', 'rb') as f:
    difficulty = pickle.load(f)

# Predict some model

difficulty.predict([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
import pickle

# Read sav

with open('difficulty_predictor.sav', 'rb') as f:
    difficulty = pickle.load(f)

# Predict some model
	
result = difficulty.predict([[27, 7609.605477]])
print(f"Result {result}")
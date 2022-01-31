import pandas as pd
from tensorflow.python.keras.models import Sequential, load_model
from tensorflow.python.keras.layers import Dense

model = load_model("trainedModel.h5")

X = pd.read_csv("proposed_new_product.csv").values
prediction = model.predict(X)

# Grab just the first element of the first prediction (since we only have one)
prediction = prediction[0][0]

# Re-scale the data from the 0-to-1 range back to dollars
# These constants are from when the data was originally scaled down to the 0-to-1 range
prediction = prediction + 0.1159
prediction = prediction / 0.0000036968

print("Earnings Prediction for Proposed Product - ${}".format(prediction))


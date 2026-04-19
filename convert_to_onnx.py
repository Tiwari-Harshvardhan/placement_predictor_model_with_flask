import pickle
import numpy as np
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# 1. Load your existing model
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)

# 2. Define the input type
# The [None, 2] means: 
# None = unknown number of rows (batch size)
# 2 = your two features (CGPA, IQ)
initial_type = [('float_input', FloatTensorType([None, 2]))]

# 3. Convert to ONNX
# This is the standard method for scikit-learn models
onx = convert_sklearn(clf, initial_types=initial_type)

# 4. Save the model
with open("model.onnx", "wb") as f:
    f.write(onx.SerializeToString())

print("Model converted successfully to model.onnx!")
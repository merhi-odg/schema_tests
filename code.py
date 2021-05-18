# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc

import pandas as pd
import json
import pickle

# modelop.init
def begin():
    
    global params
    params = pickle.load(open("train_encoded_columns.pickle", "rb"))
    
    print("params: ", params, flush=True)
    pass

# modelop.score
def action(data):
    print("Entering Action", flush=True)
    # data = [{"A":1, "B":2}]
    
    data = data[0]
    print("after extraction", flush=True)
    # yield [{"prediction": data["A"] + data["B"], "input": json.dumps(data)}]

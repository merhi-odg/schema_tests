# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc

import pandas as pd
import json


# modelop.init
def begin():

    pass

# modelop.score
def action(data):
    
    # data = [{"A":1, "B":2}]
    
    data = data[0]
    
    yield [{"prediction": data["A"] + data["B"], "input": json.dumps(data)}]

# modelop.schema.0: input_schema.avsc
# modelop.schema.1: output_schema.avsc


#modelop.init
def begin():

    pass

def action(data):
    
    # data = [{"A":1, "B":2}]
    
    data = pd.DataFrame(data).iloc[0]
    
    
    yield [{"prediction": data["A"] + data["B"], "input": {data.to_dict(orient='records)}}]

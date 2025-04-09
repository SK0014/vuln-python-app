import pickle

def unsafe_deserialize(data):
    try:
        obj = pickle.loads(data.encode('latin1'))  # vulnerable to RCE
        return f"Deserialized: {obj}"
    except Exception as e:
        return f"Error: {e}"

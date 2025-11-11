from fastapi import HTTPException

@app.get("/api/private/pat")
def get_private_layer():
    # In production: authenticate via token, IP, or biometric
    if not is_pat_request():  # Your custom check
        raise HTTPException(403, "This garden is Pat's alone.")
    with open("lyra_personal_pat.json", "r") as f:
        return json.load(f)
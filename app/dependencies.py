from fastapi import Header, HTTPException


async def get_token_header(x_api_key: str = Header(...)):
    if x_api_key != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-API-KEY header invalid")

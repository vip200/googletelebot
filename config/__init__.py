import os

class Config:
    API_ID = int( os.getenv("api_id","4857965") )
    API_HASH = os.getenv("api_hash","801abaf29775cf564efd759def571091")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001497492623") )
    CHANNEL_USERNAME = int(os.getenv("channel_id","-1001838011684"))
    TOKEN = os.getenv("token","5007581156:AAE9_vOenr49VCuZp45RZaB5bFFP0oWj7hs")
    DOMAIN  = os.getenv("domain","35.203.169.150")

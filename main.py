import os
import uvicorn
from server.api import app

'''
This main file and we have to run this file and this application
runs on uvicorn server on 7000 port.
'''

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, lifespan="on", relouser=True)
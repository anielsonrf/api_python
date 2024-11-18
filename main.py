from fastapi import FastAPI
import ctypes

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"response": "pong"}

# Windows API functions
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Virtual-Key codes
VK_F11 = 0x7A       # Código para F11
VK_F12 = 0x7B       # Código para F12
VK_PAGE_UP = 0x21   # Código para Page Up
VK_PAGE_DOWN = 0x22 # Código para Page Down

# Key event flags
KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002

def press_key(hexKeyCode):
    user32.keybd_event(hexKeyCode, 0, KEYEVENTF_KEYDOWN, 0)
    user32.keybd_event(hexKeyCode, 0, KEYEVENTF_KEYUP, 0)

@app.get("/press_f11")
async def press_f11():
    press_key(VK_F11)
    return {"status": "Tecla F11 pressionada"}

@app.get("/press_f12")
async def press_f12():
    press_key(VK_F12)
    return {"status": "Tecla F12 pressionada"}

@app.get("/press_page_up")
async def press_page_up():
    press_key(VK_PAGE_UP)
    return {"status": "Tecla Page Up pressionada"}

@app.get("/press_page_down")
async def press_page_down():
    press_key(VK_PAGE_DOWN)
    return {"status": "Tecla Page Down pressionada"}

import pytesseract
import keyboard
import pyautogui
from openai import OpenAI

pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
client = OpenAI(api_key="")

def run_all():
    # Button coordinates -- store top-left and bottom-right that defines the BOX 
    # Found these variables using pyautoguy.locateOnScreen
    button_coords = {
        0: {"top_left": (0, 72), "bottom_right": (2475, 200)},
        1: {"top_left": (105, 1000), "bottom_right": (1219, 1118)},
        2: {"top_left": (1370, 1000), "bottom_right": (2500, 1127)},
        3: {"top_left": (100, 1200), "bottom_right": (1260, 1361)},
        4: {"top_left": (1370, 1175), "bottom_right": (2000, 1353)},
    }

    information=[]
    for button in button_coords:
        coords = button_coords[button]
        x1, y1 = coords["top_left"]
        x2, y2 = coords["bottom_right"]

        width = x2 - x1
        height = y2 - y1
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        screenshot_text = pytesseract.image_to_string(screenshot)
        if screenshot_text.strip() == "a\\":
            print("No text found.")
            continue
        if not screenshot_text.strip():
            print("No text found.")
            continue
        print(f"Text {button}: {screenshot_text}")
        information.append(screenshot_text)
        
    question = information[0]
    optionA=information[1][1:]
    optionB=information[2][1:]
    optionC = information[3][1:]
    optionD = information[4][1:]
    prompt = question + " A. " + optionA + " B. " + optionB + " C. " + optionC + " D. "+ optionD + " \n Choose among the choices; Just give me the answer as a letter "

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.2
    )
    
    ans = completion.choices[0].message.content
    print(ans[0])
    if ans[0]=='A':
        pyautogui.click(662,1059)
    elif ans[0]=="B":
        pyautogui.click(1935,1063)
    elif ans[0]=="C":
        pyautogui.click(680, 1280)
    elif ans[0]=="D":
        pyautogui.click(1685, 1264)

keyboard.add_hotkey("ctrl+alt+t",run_all)
keyboard.wait()
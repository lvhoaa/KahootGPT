# KahootChatGPT
Solve Kahoot Multiple-choice questions using ChatGPT

1. At every new question, click the key ctrl+alt+t to start the process
2. Use Pyautogui to capture the full screen, including questions and answer choices

![image](https://github.com/lvhoaa/KahootChatGPT/assets/87745938/80b3b774-913b-4268-9677-6153eecea146)


3. Use OCR (optical character recognition) to extract the TEXT questions and choices from the screenshot
4. Based on this information, prompt ChatGPT by sending API requests to OpenAI
5. Get back answer as ChatGPT response

![image](https://github.com/lvhoaa/KahootChatGPT/assets/87745938/82da407a-61de-41da-b5c9-da466b502f3a)


6. Choose the correct answer using Pyautoguy.click() on the screen

![image](https://github.com/lvhoaa/KahootChatGPT/assets/87745938/c0033cfb-fa18-4723-963f-e5fb482c89d0)

7. Repeat at each new question





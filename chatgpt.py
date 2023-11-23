# Sending API requests to OpenAI Chatgpt
# Connect with ChatGPT
# Authorization: Bearer API_KEY


from openai import OpenAI
client = OpenAI(api_key="[API_KEY]")

info = ocr_test()
question = info[0]
optionA=info[1][1:]
optionB=info[2][1:]
optionC = info[3][1:]
optionD = info[4][1:]

#Sample prompt: "What is the main dish typically served on Thanksgiving? A. Turkey B. Duck C. Ice cream D. Beefsteak \n Choose among the choices; Just give me the answer as a letter "
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

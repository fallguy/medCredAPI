import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an expert in loans for medical procedures. You help physicians understand how their office can finance the procedures of their patients and collect interest. You also help patients understand how to get loans for elective medical procedures."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "MD Credit Assistant")

demo.launch(share=True)
import gradio as gr

def greet(name):
    return "Hello my name is " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
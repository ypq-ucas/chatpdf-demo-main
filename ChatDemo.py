import gradio as gr
# pip install zhipuai 请先在终端进行安装

import zhipuai

zhipuai.api_key = "4619c540301cfc8bd3073a947aba96e4.8vf8I6AdL7fuscrv"
def answer(input):
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_lite",
        prompt= [{"role":"user","content":input}],
        temperature= 0.9,
        top_p= 0.7,
        incremental=True
    )
    str = ""
    for event in response.events():
        # return event.data
        if event.event == "add":
            str = str+event.data
        elif event.event == "error" or event.event == "interrupted":
            str = str+event.data
        elif event.event == "finish":
            str = str+event.data
            print(event.meta, end="")
        else:
            str = str+event.data
    return str


# 创建一个Gradio界面，将greet函数作为输入和输出函数传递给它
iface = gr.Interface(fn=answer, inputs="text", outputs="text")

# 启动Gradio应用程序
iface.launch()

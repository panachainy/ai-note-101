from langchain_community.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# There are many CallbackHandlers supported, such as
# from langchain.callbacks.streamlit import StreamlitCallbackHandler

callbacks = [StreamingStdOutCallbackHandler()]
model = GPT4All(model="./models/mistral-7b-openorca.Q4_0.gguf", n_threads=8)

# Generate text. Tokens are streamed through the callback manager.
model("Once upon a time, ", callbacks=callbacks)

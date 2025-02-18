# Document Summarizer

The code extracts important sentences from a document by calculating word frequencies and scoring sentences based on their relevance. 

## Steps involved include:

* Text Preprocessing – Tokenizing sentences and words, removing stopwords, and handling punctuation.
* Sentence Scoring – Assigning importance scores to sentences based on term frequency.
* Summarization – Extracting the most relevant sentences to form a summary.

* * *

# Alternative options to create a document summarizer

* Use of Pre-trained models (Hugging Face models, Open AI GPT-4)
* Use of NLTK, SpaCy (Extractive Summarization)

### Using Pre-Trained models - Hugging Face models

```python
import gradio as gr
import os
import io
from IPython.display import Image, display, HTML
from PIL import Image
import base64 
from dotenv import load_dotenv, find_dotenv

def summarize(input):
    output = get_completion(input)
    return output[0]['summary_text']

gr.close_all()
demo = gr.Interface(fn=summarize, 
                    inputs=[gr.Textbox(label="Text to summarize", lines=6)],
                    outputs=[gr.Textbox(label="Result", lines=3)],
                    title="Text summarization with distilbart-cnn",
                    description="Summarize any text using the `shleifer/distilbart-cnn-12-6` model under the hood!"
                   )
demo.launch(share=True, server_port=int(os.environ['PORT2']))
```
* * *

### Output API

![API_Output](https://github.com/nagakirankasi/doc-summarizer/blob/main/assets/images/NLP_Gradio_interface.png)





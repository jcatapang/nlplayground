# NLPlayground
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br>
NLPinas' abstracted library for interfacing on its Huggingface models and other modules

## Features
### Support for Tagalog/Taglish/English
- Translation is provided by Google Translate API instead to offload NLPinas's e-Salin API servers.

### Zero-shot classification
- Zero-shot model allows us to classify data, which wasn’t used to build a model.
- In zero-shot classification, you can define your own labels and then run classifier to assign a probability to each label.
- NLPlayground uses a Bart model proposed by researchers from Facebook: Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov and Luke Zettlemoyer on October 29, 2019 trained on the MultiNLI dataset. The model is further fine-tuned on a proprietary dataset of NLPinas.

### Table question-answering
- Formerly called the `NLPinas NLQ Engine`, announced last September 2020. The project announcement can be found [here](https://www.facebook.com/groups/NLPinas/permalink/2706512796284411).
- Table question-answering allows us to answer questions about tabular data using natural language, eliminating the use of query languages like SQL.
- NLPlayground uses a TAPAS model proposed by researchers from Google: by Jonathan Herzig, Paweł Krzysztof Nowak, Thomas Müller, Francesco Piccinno and Julian Martin Eisenschlos, fine-tuned in a chain on SQA, WikiSQL and finally WTQ. The model is further fine-tuned on a proprietary dataset of NLPinas.

### Summarization
- Summarization allows us to obtain the important points or highlights of a chunk of text.
- NLPlayground uses another Bart model similar to earlier but for conditional generation. The model is also further fine-tuned on a proprietary dataset of NLPinas.

## Instructions
1. Clone the repository.
2. Download the .zip file containing the `models` and `tokenizers` folders. The .zip file can be found [here]().
3. Place the folders in the main directory of the repository.
4. Done!

## NLPinas
You can join NLPinas on [Facebook](https://www.facebook.com/groups/NLPinas) or visit our [website](https://nlpinas.org.ph/).

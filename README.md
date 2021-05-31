# NLPlayground
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br>
[![DOI](https://zenodo.org/badge/370722014.svg)](https://zenodo.org/badge/latestdoi/370722014)

NLPinas' abstracted library for interfacing on its Huggingface models and other modules

### Importing the modules
```python
from nlplayground.zero_shot import ZeroShotClassifier
from nlplayground.translation import Translator
from nlplayground.tabular_qa import TabularQA
from nlplayground.summarization import Summarizer
```

## Features
### Support for Tagalog/Taglish/English
- Translation is provided by Google Translate API instead to offload NLPinas's e-Salin API servers.
```python
trans = Translator()
print(trans.translate("Ang saya ko ngayon.", src='tl', dest='en'))
print(trans.translate("This is a good example.", src='en', dest='tl'))
```

### Zero-shot classification
- Zero-shot model allows us to classify data, which wasn’t used to build a model.
- In zero-shot classification, you can define your own labels and then run classifier to assign a probability to each label.
- NLPlayground uses a Bart model proposed by researchers from Facebook: Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov and Luke Zettlemoyer on October 29, 2019 trained on the MultiNLI dataset. The model is further fine-tuned on a proprietary dataset of NLPinas.
```python
clf = ZeroShotClassifier()
clf.predict('Ako ay gumagamit ng computer ngayon.', ['emotions', 'technology', 'food'], language='tl')
```

### Table question-answering
- Formerly called the `NLPinas NLQ Engine`, announced last September 2020. The project announcement can be found [here](https://www.facebook.com/groups/NLPinas/permalink/2706512796284411).
- Table question-answering allows us to answer questions about tabular data using natural language, eliminating the use of query languages like SQL.
- NLPlayground uses a TAPAS model proposed by researchers from Google: by Jonathan Herzig, Paweł Krzysztof Nowak, Thomas Müller, Francesco Piccinno and Julian Martin Eisenschlos, fine-tuned in a chain on SQA, WikiSQL and finally WTQ. The model is further fine-tuned on a proprietary dataset of NLPinas.
```python
data = {'Full Names': ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"],
        'First Names': ["Brad", "Leonardo", "George"],
        'Last Names': ["Pitt", "di Caprio", "Clooney"],
        'Number of movies': ["87", "53", "69"]}
table = pd.DataFrame.from_dict(data)
queries = ["Ano ang buong pangalan ng pangalawang aktor?",
           "How many movies has Clooney played in?",
           "Sino masmaraming movies, si George or si Brad?",
           "Who has less than 70 movies?",
           "Ilang aktor ang nasa table?",
           "What is the average number of movies of the three actors?"]
```
```python
tqa = TabularQA()
display(table)
for question in queries:
    print(question+" -> "+str(tqa.predict(question, table)))
```

### Summarization
- Summarization allows us to obtain the important points or highlights of a chunk of text.
- NLPlayground uses another Bart model similar to earlier but for conditional generation. The model is also further fine-tuned on a proprietary dataset of NLPinas.
```python
article = "Si Rodrigo Roa Duterte (ipinanganak noong 28 Marso 1945),\
    kilala rin sa kanyang bansag na Digong, ay isang Pilipinong\
    abogado at politiko na kasalakuyang naninilbihan bilang ika-16\
    na Pangulo ng Pilipinas. Siya ang unang naging pangulo na mula\
    sa Mindanao. Si Duterte ay isa sa mga pinakamatagal na nanilbihang\
    alkalde sa Pilipinas at naging alkalde ng Lungsod ng Dabaw, isang\
    urbanisadong lungsod sa kapuluan ng Mindanao nang pitong termino o\
    mahigit 22 taon. Nagsilbi rin siyang bise-alkalde at kongresista ng lungsod."
summarizer = Summarizer()
summarizer.predict(article)
```

## Installation instructions
1. Clone the repository.
2. Download the .zip file containing the `models` and `tokenizers` folders. The .zip file can be found [here](https://drive.google.com/file/d/1tEobtChGf7vCc6MbL23H1S-aXry4LIOF/view?usp=sharing).
3. Place the folders in the main directory of the repository.
4. Install the dependencies found in `requirements.txt`.
5. Done!

## NLPinas
You can join NLPinas on [Facebook](https://www.facebook.com/groups/NLPinas) or visit our [website](https://nlpinas.org.ph/).

## Citing our work
You can cite our work using: [![DOI](https://zenodo.org/badge/370722014.svg)](https://zenodo.org/badge/latestdoi/370722014).


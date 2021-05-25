from nlplayground.misc import pipeline, set_verbosity_error
from nlplayground.translation import Translator

set_verbosity_error()

class ZeroShotClassifier():
	def __init__(self):
		self.classifier = pipeline("zero-shot-classification", model="nlplayground/models/zeroshotclassifier", tokenizer="nlplayground/tokenizers/zeroshotclassifier")

	def predict(self, sentence, candidates, language='en'):
		if language == 'en':
			print('Using English zero-shot classifier. . .')
			return self.classifier(sentence, candidates)
		elif language == 'tl':
			print('Using Tagalog zero-shot classifier. . .')
			translator = Translator()
			output_dict = self.classifier(translator.translate(sentence, 'tl', 'en'), candidates)
			revised_dict = dict()
			revised_dict['sequence'] = sentence
			revised_dict['labels'] = output_dict['labels']
			revised_dict['scores'] = output_dict['scores']
			return revised_dict
		else:
			return "Language not supported."
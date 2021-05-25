from nlplayground.misc import sum_tokenizer, sum_model, set_verbosity_error, sub

set_verbosity_error()

class Summarizer():
	def __init__(self):
		self.model = sum_model.from_pretrained('nlplayground/models/summarizer')
		self.tokenizer = sum_tokenizer.from_pretrained('nlplayground/tokenizers/summarizer')

	def predict(self, article, max_length=1024):
		inputs = self.tokenizer([article], max_length=max_length, return_tensors='pt', truncation=True)
		summary_ids = self.model.generate(inputs['input_ids'], num_beams=5, max_length=1024, early_stopping=True)
		output = [self.tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids][0]
		return sub("\s\s+" , " ", output)

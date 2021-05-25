from nlplayground.misc import tqa_tokenizer, tqa_model, set_verbosity_error
from nlplayground.translation import Translator

set_verbosity_error()

class TabularQA():
	def __init__(self):
		self.model = tqa_model.from_pretrained('nlplayground/models/tabularqa')
		self.tokenizer = tqa_tokenizer.from_pretrained('nlplayground/tokenizers/tabularqa')

	def agg(self, predicted_agg, answer):
		try:
			outputs = answer.split(", ")
		except:
			outputs = [answer]
		if predicted_agg == "SUM":
			total = 0
			for output in outputs:
				total += float(output)
			return int(total) if int(total) == total else total
		elif predicted_agg == "AVERAGE":
			total = 0
			for output in outputs:
				total += float(output)
			avg = total/len(outputs)
			return int(avg) if int(avg) == avg else avg 
		elif predicted_agg == "COUNT":
			return len(outputs)

	def predict(self, query, table):
		translator = Translator()
		query = translator.translate(query, 'tl', 'en')

		inputs = self.tokenizer(table=table, queries=[query], padding='max_length', return_tensors="pt")
		outputs = self.model(**inputs)
		predicted_answer_coordinates, predicted_aggregation_indices = self.tokenizer.convert_logits_to_predictions(
				inputs,
				outputs.logits.detach(),
				outputs.logits_aggregation.detach()
		)

		id2aggregation = {0: "NONE", 1: "SUM", 2: "AVERAGE", 3:"COUNT"}
		aggregation_predictions_string = [id2aggregation[x] for x in predicted_aggregation_indices]
		answers = []
		for coordinates in predicted_answer_coordinates:
			if len(coordinates) == 1:
				# only a single cell:
				answers.append(table.iat[coordinates[0]])
			else:
				# multiple cells
				cell_values = []
				for coordinate in coordinates:
					 cell_values.append(table.iat[coordinate])
				answers.append(", ".join(cell_values))
		for query, answer, predicted_agg in zip([query], answers, aggregation_predictions_string):
			if predicted_agg == "NONE":
				return answer
			else:
				return self.agg(predicted_agg, answer)
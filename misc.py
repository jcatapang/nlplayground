import google_trans_new as gt
import re
import transformers

# Translation
translation_module = gt.google_translator

# Regex
sub = re.sub

# Transformers
pipeline = transformers.pipeline
set_verbosity_error = transformers.logging.set_verbosity_error
tqa_model = transformers.TapasForQuestionAnswering
tqa_tokenizer = transformers.TapasTokenizer
sum_model = transformers.BartForConditionalGeneration
sum_tokenizer = transformers.BartTokenizer
from nlplayground.misc import translation_module

class Translator():
	def __init__(self):
		self.translator = translation_module()
			
	def translate(self, text, src='tl', dest='en'):
		try:
			translation = self.translator.translate(text, lang_src=src, lang_tgt=dest)
			return translation
		except:
			return "Connection error."
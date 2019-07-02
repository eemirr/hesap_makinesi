

# eval kullanarak hesap makinesi programı



class Calc:

	def __init__(self,data):

		self.data = data + "~"
		self._new_data = ''
		

	def evals(self):
		try:
			return eval(self._new_data)
		except Exception:
			return 'ERR Not Eval Method'

	def control(self):

		for i in self.data:
				
			if i.strip() in '1234567890*/%-+~':
				if i.strip() == '~':
					pass					
				else:
					self._new_data += i.strip()
			else:
				self._new_data = ''				

if __name__ == '__main__':

	value = input('example : 2+5/5+22 : ')	
	x = Calc(value)
	x.control()
	print(x.evals())
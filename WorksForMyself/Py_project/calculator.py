from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '500')
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from math import sqrt
class BoxApp(App):
	def up_leb(self):
		self.lbl.text = self.formula
	def cli(self, instance):
		if self.formula == '0':
			self.formula = ''
		self.formula += str(instance.text)
		self.up_leb()
	def resultation(self, instance):
		mas = []
		for i in self.formula:
			mas.append(i)
		for i in range(len(mas)-1):
			mas2 = []
			mas2.append(mas[i])
			mas2.append(mas[i+1])
			mas2 = ''.join(mas2)
			if mas2 == '/0':
				a = True
				break
			else:
				a = False
		if a == True:
			self.lbl.text = 'division by zero'
		else:
			res = str(eval(self.lbl.text))
			self.formula = res
			self.lbl.text = res
	def delite(self,instance):
		mas = []
		for i in self.formula:
			mas.append(i)
		mas2 = []
		for i in range(len(mas)-1):
			mas2.append(str(mas[i]))
		mas2 = ''.join(mas2)
		self.formula = mas2
		if self.formula == '':
			self.formula = '0'
		self.up_leb()
	def prozent(self, instance):
		res = str(eval(self.lbl.text))
		res = str(eval(f'{res}/100'))
		self.formula = res
		self.lbl.text = res
	def sqrty(self, instance):
		res = str(eval(self.lbl.text))
		res = str(sqrt(float(res)))
		self.formula = res
		self.lbl.text = res
	def rooty(self, instance):
		res = str(eval(self.lbl.text))
		res = str(eval(f'{res}*{res}'))
		self.formula = res
		self.lbl.text = res
	def ony(self, instance):
		res = str(eval(self.lbl.text))
		if res != '0':
			res = str(eval('1/'+res))
			self.formula = res
			self.lbl.text = res
		else:
			self.lbl.text = 'division by zero'
	def alldelt(self, instance):
		res = '0'
		self.formula = res
		self.lbl.text = res
	def delt(self, instance):
		mas = []
		for i in self.formula:
			mas.append(i)
		mas2 = []
		i = len(mas)-1
		while i != -1:
			if mas[i] == '/' or mas[i] == '*' or mas[i] == '+' or mas[i] == '-':
				a = i
				i = 0
				while i != a+1:
					mas2.append(mas[i])
					i += 1
				break
			i -= 1
		mas2 = ''.join(mas2)
		self.formula = mas2
		if self.formula == '':
			self.formula = '0'
		self.up_leb()
	def build(self):
		self.formula = '0'
		layout = GridLayout(cols = 4, padding = [5], spacing = 2)
		cam = ['%','CE','C','del','sh','po','sq','/','7','8','9','*','4','5','6','-','1','2','3','+','+/-','0','.','=']
		for i in range(0,24):
			if i == 0:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.prozent,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
			elif i == 6:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.sqrty,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
			elif i == 2:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.alldelt,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
			elif i == 1:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.delt,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
			elif i == 4:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.ony,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
			elif i == 5:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.rooty,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
			elif i == 23:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.resultation,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
			elif i == 3:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.delite,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
			else:
				layout.add_widget(
					Button(
						text=cam[i],
						font_size=25,
						on_press=self.cli,
						background_color=[.23,.23,.23, 1],
						background_normal=""))
		layout2 = BoxLayout(orientation = 'vertical')
		self.lbl = Label(text='0',size_hint = [1, .4],text_size=(400-100,500*.4-50),halign='right',font_size=30)
		layout2.add_widget(self.lbl)
		layout2.add_widget(layout)
		return layout2
if __name__ == "__main__":
	BoxApp().run()
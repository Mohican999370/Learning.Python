import sys
from collections import OrderedDict

from notebook import Notebook


__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'
__version_date__ = '15 September 2014'


class Menu:
	"""
	Represent a command-line user interface for Notebook application.
	"""

	def __init__(self):
		self.notebook = Notebook()
		self.choices = OrderedDict.fromkeys('12345')
		self.choices['1'] = {'display': 'Show notes',
							 'handler': self.show_notes}
		self.choices['2'] = {'display': 'Search notes',
							 'handler': self.search_notes}
		self.choices['3'] = {'display': 'Add notes',
							 'handler': self.add_note}
		self.choices['4'] = {'display': 'Modify notes',
							 'handler': self.modify_note}
		self.choices['5'] = {'display': 'Quit',
							 'handler': self.quit}

	def display_menu(self):
		"""
		Display the Notebook application's menu.
		"""
		print('==================')
		for k, v in self.choices.items():
			print(k, v.get('display'))

		choice = input('What do you want to do? ')
		action = self.choices.get(choice)

		if action:
			handler = action.get('handler')
			handler()
		else:
			print(choice, 'is not a valid choice')

	def run(self):
		"""
		Run the application: display the menu and respond to user's choice.
		"""
		while True:
			self.display_menu()
			pass

	def show_notes(self, notes=None):
		"""
		Display all notes in the notebook.
		"""

		if notes is None:
			notes = self.notebook.notes

		if len(notes) > 0:
			for note in notes:
				print(note, '\r\n')
		else:
			print("No note matches.")

	def search_notes(self):
		"""
		Search for a note in the notebook (by its content and tags).
		"""
		search_string = input('You want to search for ...? ')
		filtered_notes = self.notebook.search(search_string)
		self.show_notes(filtered_notes)

	def add_note(self):
		"""
		Add a new note to the notebook.
		"""
		memo = input('Enter the memo: ')
		tags = input('Enter the tags (separated by commas): ')
		self.notebook.create_note(memo, tags)
		print('Your note has been created.')

	def modify_note(self):
		"""
		Modify a note in the notebook.
		"""
		id = input('Enter the note id: ')

		note = self.notebook.find_note_by_id(id)

		if note is None:
			print('No note matches.')
		else:
			memo = input('Enter the new memo: ')
			tags = input('Enter the new tags (separated by commas): ')

			if memo:
				note.memo = memo

			if tags:
				note.tags = tags

	def quit(self):
		"""
		Exit the application.
		"""
		print("Thank you for using Notebook application.")
		sys.exit(0)


if __name__ == '__main__':
	Menu().run()
from datetime import date
import uuid

__copyright__ = 'Son-Huy TRAN'
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'
__version_date__ = '12 September 2014'


class Note:
	"""
	Represent a note in the notebook.
	Match against a string in searches and store tags for each note.

	:members: id, memo, tags, creation_date
	"""

	def __init__(self, memo: str='', tags: str=''):
		"""
		Initialize a note with memo and optional comma-separated tags.
		Automatically set the note's creation date and a unique id (a UUID).

		:param memo: the content of the note
		:type memo: str

		:param tags: comma-separated tags
		:type tags: str
		"""

		self.memo = memo
		"""
		:type memo: str
		The content of the note.
		"""
		self.tags = tags
		"""
		:type tags: str
		Comma-separated tags (instead of space-separated tags).
		"""
		self.creation_date = date.today()
		"""
		:type creation_date: date
		The date when this note is created (automatically set).
		"""
		self.id = uuid.uuid1()
		"""
		:type id: uuid.UUID
		The unique id of the note.
		Instead of an incremental id, I change it to a UUID (automatically set).
		"""

	def __str__(self):
		"""
		:return: the string representing this note
		"""

		return "[Note #" + str(self.id) + "] " + self.memo

	def __repr__(self):
		"""
		:return: the string representing this note
		"""

		return self.__str__()

	def match(self, search_string: str,
			  case_insensitive: bool=False,
			  search_in_tags: bool=True) -> bool:
		"""Determine if this note match the search string.

		:param search_string: the filter string to search
		:type search_string: str

		:param case_insensitive: set True if you want to search case-insensitively (default False)
		:type case_insensitive: bool

		:param search_in_tags: set True if you want to search in tags also (default True)
		:type search_in_tags: bool

		:return: True if a match exists, otherwise False
		:rtype: bool

		"""

		if case_insensitive:
			# Change all search_string, memo and tags to uppercase
			# to search case-insensitively

			search_string_i = search_string.upper()
			memo_i = self.memo.upper()

			if search_string_i in memo_i:
				return True
			elif search_in_tags:
				tags_i = self.tags.upper()
				return search_string_i in tags_i
			else:
				return False
		else:
			return search_string in self.memo or (search_in_tags and search_string in self.tags)


class Notebook:
	"""
	Represent a collection of notes that can be tagged, modified and searched.
	"""

	def __init__(self):
		"""Initialilze a notebook with an empty list."""

		self.id = uuid.uuid1()
		"""
		:type id: UUID
		The unique ID of the notebook (a UUID).
		"""
		self.notes = []
		"""
		:type notes: list
		The list of all notes in this notebook.
		"""

	def __str__(self):
		"""
		:return: the string representing this notebook
		"""

		return "[Notebook #" + str(self.id) + "]\r\n" + \
			   "\r\n".join([str(note) for note in self.notes])

	def __repr__(self):
		"""
		:return: the string representing this notebook
		"""

		return self.__str__()

	def find_note_by_id(self, note_id: str) -> Note:
		"""
		Find a note by its id.

		:param note_id:
		:type note_id: str

		:return: the note which has the given id if exits, otherwise None.
		:rtype: Note
		"""

		for note in self.notes:
			if note_id == str(note.id):
				return note

		# There is no note with this id.
		return None

	def create_note(self, memo: str='', tags: str='') -> None:
		"""
		Create a new note and add it to the list.

		:param memo: the content of the new note to create
		:type memo: str

		:param tags: the comma-separated tags of the new note to create
		:type tags: str
		"""

		new_note = Note(memo, tags)
		self.notes.append(new_note)

	def modify_memo(self, note_id: str, memo: str):
		"""
		Find the note with the given id
		and change its memo to the given value.

		:type note_id: str
		:param note_id: the id of the note to modify

		:type memo: str
		:param memo: the new content of the note
		"""

		note = self.find_note_by_id(note_id)

		if None != note:
			note.memo = memo

	def modify_tags(self, note_id: str, tags: str):
		"""
		Find the note with the given id
		and change it tags to the given value.

		:type note_id: str
		:param note_id: the id of the note to modify

		:type tags: object
		:param tags: the new comma-separated tags string
		"""

		note = self.find_note_by_id(note_id)

		if None != note:
			note.tags = tags

	def search(self, search_string: str) -> list:
		"""
		Find all notes that match the given search string.

		:type search_string: str
		:param search_string:

		:rtype: list
		:return: A list of all notes that match the given search string.
		"""

		return [note for note in self.notes if note.match(search_string)]
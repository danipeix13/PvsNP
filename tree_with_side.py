import json
from collections import defaultdict

class TreeWithSide():
	def __init__(self):
		self.conexions = [
			# (1, 1),
			(2, 1),
			(3, 5),
		]

		self.tree = defaultdict(list)

		# self.side = {}

	def insert(self, from_, to_):
		self.conexions.append((from_, to_))

	def show(self, sorted=False):
		print("=== LIST ===")
		if sorted: self.conexions.sort()
		for item_ in self.conexions:
			print(item_[0], "\t--->\t", item_[1])
		print("=== TREE ===")
		for k,v in self.tree.items():
			print(k, "\t-->\t", v)
		print("============")

	def save(self):
		# TODO: solo escritura
		with open("stored_tree.json", "w") as file:
			json.dump(self.tree, file)
			file.close()

	def load(self):
		self.tree = json.load("stored_tree.json")
		
	def list_to_tree(self):
		for v,k in self.conexions:
			self.tree[k].append(v)



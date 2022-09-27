import funcs as F
import tree_with_side as TWS

n = 0
tree = TWS.TreeWithSide()

if __name__ == '__main__':
#	while true:
#		threading.Thread(name=str(n), target=iter_func, args=n)
	for x in range(4, 10000):
		if F.is_prime(x):
			#n = (n + 1) % 30
			#if n == 0:
			#	os.system("clear")
			tree.insert(x, F.find_parent(x))

	tree.list_to_tree()
	tree.show()
	tree.save()


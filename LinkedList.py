class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
class LinkedList:
	def __init__(self):
		self.head = None

	def insertBeginning(self, data=None):
		node = Node(data=data, next=self.head)
		self.head = node

	def insertEnd(self, data=None):
		if self.head is None:
			node = Node(data=data, next=None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data=data, next=None)	# Insert after we reached the end

	def insertValues(self, dataLst):
		for data in dataLst:
			self.insertEnd(data)

	def printLn(self):
		if self.head is None:
			print("LinkedList is Empty.")
			return
		else:
			itr = self.head
			LinkedList = []
			while itr:
				LinkedList.append(itr.data)
				itr = itr.next
			print(LinkedList)
	def getLen(self):
		count = 0
		itr = self.head
		while itr:
			count+=1
			itr = itr.next
		return count
	def Remove(self, index):
		if index < 0 or index >= self.getLen():
			raise Exception("Invalid Index")
		elif index == 0:
			self.head = self.head.next
			return
		else:
			count = 0
			itr = self.head
			while itr:
				if count == index-1:
					itr.next = itr.next.next
					break
				count+=1
				itr = itr.next

	def Insert(self, data, index):
		if index < 0 or index >= self.getLen():
			raise Exception("Invalid Index")

		elif index == 0:
			self.insertBeginning(data)
			return

		else:
			count = 0
			itr = self.head
			while itr:
				if count == index-1:
					node = Node(data, itr.next)
					itr.next = node
					break
				itr = itr.next
				count+=1


ll = LinkedList()
ll.insertBeginning(1)
ll.insertBeginning(2)
ll.insertEnd(0)
ll.insertValues([9,8,7,6])

print(ll.getLen())
ll.Remove(3)
ll.Insert(index=3, data="h")
ll.printLn()
	# L = list(map(int, input().split()))
	# map(int, input().split())
	

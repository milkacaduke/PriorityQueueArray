# Priority queue implemented with min/max heap with array.
import sys

class PriorityQueue(object):
	
	def __init__(self, maxSize=10):
		self.size = 0
		self.max_size = maxSize
		self.min_heap = [None]*self.max_size

	def push(self, value):
		if self.size >= self.max_size:
			return False

		end_idx = self.size - 1
		pos = end_idx + 1
		self.min_heap[pos] = value
		# bubble up
		while pos > 0:
			parent_idx = ((pos + 1) // 2) - 1
			if self.min_heap[pos] < self.min_heap[parent_idx]: 
				# if value is smaller than parent, swap
				# swap
				temp = self.min_heap[parent_idx]
				self.min_heap[parent_idx] = self.min_heap[pos]
				self.min_heap[pos] = temp

				pos = parent_idx
			else:
				break

		self.size += 1
		# print("{} , size = {}".format(self.min_heap, self.size))


	def pop(self, ):
		if self.size == 0:
			return None

		result = self.min_heap[0]

		# taks last element and put at root and trikle down
		last_element = self.min_heap[self.size - 1]
		self.min_heap[0] = last_element

		# trikle down. 
		pos = 0
		while pos < (size / 2):

			left_child = (pos*2) + 1
			right_child = left_child = left_child + 1

			# TODO


		self.size -= 1
		return result


	def printQueue(self):
		if self.size == 0:
			return None
		
		print("{} , size = {}".format(self.min_heap, self.size))



# main stuff

# pq = PriorityQueue()
# pq.push(23)
# pq.push(35)
# pq.push(7)
# pq.push(15)
# pq.push(65)
# pq.printQueue()


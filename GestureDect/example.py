class Person:

	arr = []
	wqq = []

	def __init__(self,names,ages):
		self.names = names
		self.ages = ages

	def averageAge(self):
		age = 0
		for a in self.ages:
			age = age+a

		return age/len(self.ages)
	def minAge(self):
		i=self.ages[0]
		for j in self.ages:
			if i>=j:
				temp=i
				i=j
				j=temp

		return i

	def generateArr(self, num):
		for i in range(0,num):
			Person.arr.append(i)
		return Person.arr

	def readFile(self):
		with open('test.txt') as fp:
			for line in fp:
				Person.arr.append(line.split('_'))

			print Person.arr
				


if __name__ == "__main__":
	p = Person(["jack","john","steve"],[250])
	p.readFile()
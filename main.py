A = [96,53,56,64,67,62,27,93,54,34,21,69,75,81,39,13,33,14,84,75,21,49,6,38,74,38,23,2,76,64,65,95,15,59,79,37,39,87,83,23,66,1,202,94,89,99,17,94,22,22,41,88,38,12,54,46,51,18,57,26,58,37,95,49,84,72,64,16,18,3,38,39,10,76,70,12,548,654,15,74,19,77,45,88,57,16,68,23,51,00,29,40,71,28,92,50]
print(sorted(A))
for i in range(len(A)):
	A[i] = A[i:i+1]

B = []

def teste(L, R):
	tmp = []
	i = j = 0
	while i in range(len(L)) or j in range(len(R)):
		if(i == len(L)):
			tmp.append(R[j])
			j += 1
		elif(j == len(R)):
			tmp.append(L[i])
			i += 1
		elif(L[i] < R[j]):
			tmp.append(L[i])
			i += 1
		else:
			tmp.append(R[j])
			j += 1
	return tmp
			

def merge(A):
	if(len(A) == 1 or len(A) == 0):
		return A
		
	tmp = []

	for i in range(0,len(A) - 1,2):
		tmp.append(teste(A[i], A[i+1]))
	
	#Se for Ímpar
	if(len(A)%2 != 0):
		tmp.append(A[len(A) - 1])

	return merge(tmp)

B = merge(A)
print("Ordenado:", )
print(B)
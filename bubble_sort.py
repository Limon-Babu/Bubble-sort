def bubble_sort(L):
	
	n=len(L)
	
	for i in range(0,n-1):
		
		for j in range(0, n-i-1):
			
			if L[j]>L[j+1]:
				
				L[j],L[j+1]=L[j+1],L[j]
				
				
if __name__ == "__main__":
	L=[2,4,7,9,3,1,0,4,6,5]
	print("Before sorting:", L)
	bubble_sort(L)
	print("After sorting:", L)

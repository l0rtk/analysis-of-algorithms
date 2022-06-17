#include <stdio.h>

// O(N)
int sequential_sort(int array[],int arrSize, int target){

	int i;
	for (i = 0; i < arrSize; i++){
		if (array[i] == target){
			return i;
		}
	}

	return -1;
}

int main(){

	int arraySize;
	printf("Enter array size:");
	scanf("%d",&arraySize);

	int array[arraySize];
	int i;
	for (i = 0;i < arraySize;i++){
		printf("Enter %d element of the array: \n",i);
		scanf("%d",&array[i]);
	}
	
	int target;
	printf("Enter the target number: ");
	scanf("%d",&target);

	int search_result = sequential_sort(array,arraySize,target);
	if (search_result != -1){
		printf("index of element %d is: %d\n",target, search_result); 
	}else{
		printf("target not found\n");
	}

	return 0;
}

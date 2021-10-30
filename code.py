def get_count(arr,size,target_value):
  count=0
  for i in range(0,size):
    if arr[i]==target_value:
      count=count+1
    return count
my_list=[1,1,2,4,5,3,6,5,2,1,3,4,5,6,8,9,5,7,8,9,6,5,4,7,8,5,1,2,3,6,5,4,7,8,5,1,2,3,5,7,8,9,6,5,4,1,2]

print('1 occirance:  ',get_count((my_list),len(my_list),1))

# given tuple of list 
tup=([1,2], [1, 2])
tup1=([1,2,3], [3,2,1])
def rmse(inp_tuple):
  " This function takes in the tuple of two lists where first list is actual values and the second list is predicted values. This function returns the Room mean squared error"
  summ=0
  lst1=inp_tuple[0]
  lst2=inp_tuple[1]
  print(lst1)
  print(lst2)
  for i in range(len(lst1)):
    summ+=(lst2[i]-lst1[i])**2
  return summ/len(lst1)



print(rmse(tup1))

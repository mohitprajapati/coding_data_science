def mean_lst(lst):
  " This function helps calculating the mean of the numbers in the given list"
  summ=0
  if len(lst)>0:

    for i in lst:
      summ+=i
    summ/=len(lst)
    return summ
  else:
    return 'Nan'
  

a=[]
print(mean_lst(a))

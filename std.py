from math import sqrt
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
def std(arrr):
  " this function calculates the standard deviation of elements given in a list"
  meann=mean_lst(arrr)

  diff=0
  if meann!='Nan':
    for i in arrr:
      diff+=(i-meann)**2
    diff= (1/(len(arrr)-1))*diff
    diff=sqrt(diff)
    return diff
  else:
    return meann
 
arrr=[1,2,3,4]
print(std(arrr))

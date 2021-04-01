def ArrayChallenge(strArr):
  x = strArr[0]
  y = strArr[1]
  # code goes here
  count = 0
  for i in range(len(strArr[0])):
     if x[i] != y[i]:
       count = count + 1
      
  return count

# keep this function call here 
print ArrayChallenge(raw_input())

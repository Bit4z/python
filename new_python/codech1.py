def FindIntersection(strArr):

  firstArr = strArr[0].split(", ")
  secondArr = strArr[1].split(", ")

  intersection = []

  for number in firstArr:
    if number in secondArr:
      intersection.append(number)

  


  # code goes here
  if len(intersection) > 0:
    return ",".join(intersection)
  else:
    return "false"

# keep this function call here 
print(FindIntersection(raw_input()))


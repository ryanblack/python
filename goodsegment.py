l = 3   #start
r = 48  #end
lenght_temp_segment = 0    #temp lengh for each array you try
lenght_result_segment = 0  #result lenght of the target good segment   
bad_array = [7,15,20, 27]  #bad numbers given
temp_array = []            #temp array for each array you try  
good_array = []            #the result good segment we are looking for
i = 0                      #increment for first while loog
j = l                      #increment for inner while loop

#First we sort the array with badnumbers
bad_array.sort()
#1. Checking each segment, except the one in the end.
while i < r and i < len(bad_array):                
  while j < bad_array[i]:                          #checking each segment
    temp_array.append(j)
    j+=1
  lenght_temp_segment = len(temp_array)            #calc lenght of current segment
  #enable this print to seed all the good segments
  #print("j:", j, "/ lenght:", lenght_temp_segment, "/ Array:", temp_array)
  if lenght_result_segment < lenght_temp_segment:  #if lengh of the current segment is longer than any before => use current segment
    lenght_result_segment = lenght_temp_segment
    good_array = temp_array.copy()
    temp_array.clear()                             #clear temp_array to use one more time in the next loop
  j+=1
  i+=1

#2. Checking the segment: between badarray[-1] <> r
while j <= r:
  temp_array.append(j)
  j+=1
lenght_temp_segment=len(temp_array)                #calc lenght of current segment
#enable this print to seed all the good segments
#print("j:", j, "/ lenght:", lenght_temp_segment, "/ Array:", temp_array)
if lenght_result_segment < lenght_temp_segment:    #if lengh of the current segment is longer than any before => use current segment
    lenght_result_segment = lenght_temp_segment
    good_array = temp_array.copy()
    temp_array.clear()                             #clear temp_array to use one more time in the next loop

#3. Printing the result - lenght and longest good segment
print("Longest Good Segment:", good_array, "lenght =",lenght_result_segment)

#===========================================================================
# Output you'll get
# j: 7 / lenght: 4 / Array: [3, 4, 5, 6]
# j: 15 / lenght: 7 / Array: [8, 9, 10, 11, 12, 13, 14]
# j: 20 / lenght: 4 / Array: [16, 17, 18, 19]
# j: 27 / lenght: 10 / Array: [16, 17, 18, 19, 21, 22, 23, 24, 25, 26]
# j: 49 / lenght: 21 / Array: [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
# Longest Good Segment: [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48] lenght = 21
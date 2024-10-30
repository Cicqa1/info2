# while - is used to execute a block of code multiple times
i = 1
while i <= 5:
  print(i)
  i += 1
print("Done")   # 1 2 3 4 5 Done

# break - is used to exit a loop
i = 1
while i <= 5:
  print(i)
  if i == 3:
    break
  i += 1
print("Done")   # 1 2 3 Done

# continue - is used to skip the current block and return to the loop
i = 1
while i <= 5:
  if i == 3:
    i += 1
    continue
  print(i)
  i += 1
print("Done")   # 1 2 4 5 Done

# infinite loop
i = 1
while i <= 5:
  print(i) # i += 1
print("Done")   #

# while loop with else
i = 1
while i <= 5:
  print(i)
  i += 1
else:
  print("Done")   # 1 2 3 4 5 Done

# while loop with break
i = 1
while i <= 5:
  print(i)
  if i == 3:
    break
  i += 1
else:
  print("Done")
print("Done")   # 1 2 3 Done

# while loop with continue
i = 1
while i <= 5:
  if i == 3:
    i += 1
    continue
  print(i)
  i += 1
else:
  print("Done")
print("Done")   # 1 2 4 5 Done

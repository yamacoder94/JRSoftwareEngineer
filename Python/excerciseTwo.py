##1. Create a list of names and print the second item.
list_names = ['yamill','moran','arguello']
print(list_names)

#2. Create a list of sports and then replace the second item with another sport.
list_sports = ['futbol','tenis','basket']
list_sports[2] = 'ping pong'
print(list_sports)

#3. Create a list containing numbers and delete the fifth number from the array.
list_nums = [1,2,3,4,5,6]
list_nums[4] = 420
print(list_nums)

#4. Create two lists of numbers and merge them.
list_nums2 = [1,2,3,4,5,6]

print(list_nums + list_nums2)

#5. Create a list of numbers and find the length, minimum, and maximum.
list_nums3 = [1,2,3,4,5,6]
print(list_nums3)
print(len(list_nums3))
print(max(list_nums3))
print(min(list_nums3))

#6. Create a dictionary of students and scores and print out a student’s score.
direct01 = {'yamill': 10, 'alejandro': 9, 'francisco': 9}
print(direct01['yamill'])

#7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
direct02 = {'yamill': 30, 'alejandro': 16, 'francisco': 29}
del direct02['alejandro']
print(direct02)

#8. Create a dictionary of names and ages and then print out all the keys and values
direct03 = {'yamill': 30, 'alejandro': 16, 'francisco': 29}

print(direct03)

#9. Create a tuple of your favorite movies
tup = ('interstellar','the dark knight','babilon')
print(tup)

#10. Create a tuple and print all the items from the first to third index.
print(tup[0:1])
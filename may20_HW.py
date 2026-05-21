s = "I love Python Programming"
count = 0
v1 = "aeiouAEIOU"
for ch in s:
    if ch in v1:
        count = count + 1
print (f"Count of vowels {v1} in given string is ",count)

#Output
#Count of vowels aeiouAEIOU in given string is  7
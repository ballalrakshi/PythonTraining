# break and continue

#break: come out of the loop as soon as the condition is met
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)
# print("Program exited!")    #1 2 3 4

# continue: if you want to skip a few things in between, then use continue
for i in range(1,10):
    if i ==5:
        continue
    print(i)
print("program exited!")     # 1 2 3 4 6 7 8 9 - 5 skipped

# multiple skipped
#     for i in range (1, 10):
#     if i ==5 or i ==3 or i==6:
#         continue
#     print(i)
# print("Program exited!")   # 1 2 4 7 8 9
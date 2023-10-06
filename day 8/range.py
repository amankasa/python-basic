print("Enter the starting value:")
start=input()
print("Enter the ending value:")
end=input()
print("Enter the difference value:")
difference=input()

start=int(start)
end=int(end)
difference=int(difference)
print("The function generates:")
rng=[]
def range(start,end,difference):
    if(start<end):
        print(start)
        rng.append(start)
    if (start<end):
        start+=difference
        # print (start)
    else:
        return rng
    # print(start,end,difference)
    range(start,end,difference)
range(start,end,difference)
print(rng)
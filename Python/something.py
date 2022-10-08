arr = [1,2,4,56,75,86,87,100,170,680,750,755];
#      0 1 2  3 4  5  6   7  8    9   10  11
a = int(input("Enter number: "));

mid = 0         # stores middle term
start=0         # stores starting term
end= len(arr)-1;# stores end term
if(a in arr):
    while(arr[mid] != a):
        mid = int((start+end)/2)
        if (arr[mid] > a):
            end = mid;
        elif(arr[start] == a):
            mid = start;
            break;
        elif(arr[end] == a):
            mid = end;
            break;
        else:
            start = mid;
        
    print(mid)
else:
    print("Number not in list")
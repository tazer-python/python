element = input("Enter an element: ")
count = {}
string = "";
x = 0
something = "";
something_number = 0
if "(" in  element: 
    something = element[element.index("(")+1 : element.index(")")];
    something_number = int(element[element.index(")")+1])
for i in element:
    try:
        if string in something: 
            count[string] = int(i) * something_number
            string = "";
            x += 1;
        else:
            count[string] = int(i);
            string = "";
            x += 1;
            
    except ValueError:
        if i != "(" and i!= ")":
            string += i;
        else:
            pass
        try:
            if element[element.index(i)+1] == element[element.index(i)+1].upper() and element[element.index(i)+1] not in "123456789":
                if string in something: 
                    count[string] = something_number
                    string = "";
                    x += 1;
                else:
                    count[string] = 1
                    string = "";
                    x += 1;
        except IndexError:
            if string in something: 
                    count[string] = something_number
                    string = "";
                    x += 1;
            else:
                count[string] = 1
                string = "";
                x += 1;
    except:
        print("error")
try:
    for i in enumerate(count):
        if i[1] == "":
            del count[i[1]]
except RuntimeError:
    pass


print(count);
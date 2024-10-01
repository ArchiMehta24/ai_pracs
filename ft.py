hsc  = {'Avinash':.5,'Joshua':.6,'Hendrica': .3,'Jeffred': .1,'Pratvia': .4,'Joben': .2,'Nisha': .6,'Shubham': .5}
ssc  = {'Avinash':.3,'Joshua':.2,'Hendrica': .9,'Jeffred': .8,'Pratvia': .9,'Joben': .5,'Nisha': .6,'Shubham': .2}
cgpa = {'Avinash':.9,'Joshua':.7,'Hendrica': .1,'Jeffred': .6,'Pratvia': 1.,'Joben': .2,'Nisha': .3,'Shubham': .9}

# Use list comprehensions for concise and faster calculations
def intersection(dict1, dict2):
    temp = {}
    for key in dict1.keys() & dict2.keys():  # Use set intersection to avoid KeyError
        dict1val = dict1[key]
        dict2val = dict2[key]

        if dict1val < dict2val:
            temp[key] = dict1val
        else:
            temp[key] = dict2val
    return temp

def union(dict1, dict2):
    temp = {}
    for key in dict1.keys() & dict2.keys():  # Use set intersection to avoid KeyError
        dict1val = dict1[key]
        dict2val = dict2[key]

        if dict1val > dict2val:
            temp[key] = dict1val
        else:
            temp[key] = dict2val
    return temp

def alphacut(dict, a):
    result = []
    for k, v in dict.items():
        if v > a:
            result.append(k)
    return result

def complement(dict1):
    temp = {}
    for k, v in dict1.items():
        temp[k] = 1 - v
    return temp

# Example usage
result = alphacut(intersection(hsc, cgpa), 0.5)
print(result)
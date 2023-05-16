while True:
 print("Python program to calculate the key and the closure of a given relation: ")
 rel = input("Enter the name of the relation: ")
 attr = input("Enter the attributes of the relation, separated by commas: ").split(",")
 lhs = []
 rhs = []
 key = []
 print("Enter the functional dependencies of the relation, one at a time (enter '000' when finished): ")

 while True:
    fd = input().split("->")
    if fd[0] == '000':
        break
    elif fd[0] not in attr:
       print(str(fd[0])+' is not in the relation')
    elif fd[1] not in attr:
       print(str(fd[1]) +' is not in the relation')
       continue

    key.extend(fd[0].split(","))
    lhs.extend(fd[0].split(","))
    rhs.extend(fd[1].split(","))

 for i in range(len(attr)):
    if attr[i] not in lhs and attr[i] not in rhs:
        key.extend(attr[i].split(","))

 for k in key.copy():
    if k in rhs:
        key.remove(k)

 print("The key of the relation", rel, "is:", set(key))
 visited =[]
 def findclosure(attribute, lhs, rhs, visited=[]):
    i=0
    for attr in attribute:
        if attr in lhs and attr not in visited:
            visited.append(attr)
            indexofattr = lhs.index(attr)
            print(str(rhs[indexofattr]))
            findclosure(rhs[indexofattr].split(","), lhs, rhs, visited)
        else:
               return
        

 while True:
  attribute = input("Give an attribute: ").split(",")
  if attribute[0] not in attr:
     print(str(attribute) +' is not in the relation')
     continue
  print("From "+str(attribute) + " we get: " + str(attribute))
  findclosure(attribute, lhs, rhs,visited)
  visited = []

  visited = []
# # data structures in python

#  #names=["harry","mark"]
# print(names[0])
# print(f"Names{names}")
# names.append("Ron")
# print(f"names{names}")
# names.sort()
# print(f"names{names}")
# names.sort()
# print(f"names{names}")

# s=set()
# s.add(1)
# s.add(2)
# s.add(3)

# print(s)

# s.remove(3)

# print(f"set values are{s}")

# print(f"listlength is{len(names)},set length is {len(s)}")


# houses ={"Harry":"Griffyndor","mark":"slytherin"}

# print (houses["Harry"])

# houses["Ron"]="Griffyndor"

# print(houses["Ron"])


# def square(x):
#  return x*x

# for i in range(6):
#   print(f"The square value of {i} is {square(i)}")


# class Point():
#     def __init__(self,input1,input2):
#         self.x=input1
#         self.y=input2
# p = Point(2,8)
# print(p.x)
# print(p.y)


class Flight():
    def __init__(self,capacity):
       self.capacity=capacity
       self.passengers=[]

    def add_passengers(self,person):
      if not self.open_seats():
       return False
      else:   
       self.passengers.append(person)
       return True
      
    def open_seats(self):
     return self.capacity-len(self.passengers)

flight= Flight(3)

people=["harry","Mark","william","Ron"]
for person in people:
    success = flight.add_passengers(person)

    if success:
        print(f"{person} successfully added into the passengers")
    else:
        print(f"cannot add {person} in tha passengers")



    
    #  if success==True:
    #      print(f"{person} is successfully added into the passengers List")
    #  else
    #     print(f"seat not available for the person{person}")







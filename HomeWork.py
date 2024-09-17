#Theme 2:
# a= int(input())
# if a>100:
#     print("a is greater 100")
# elif a <100:
#     print("a is smaller 100")
# else:
#     print("a is 100")

#Theme 3:
# names=(1,2,3,4,"Hello", 3,"5")
# if 2 in names or "Hello" in names:
#     print(names[1:5:2])

#Theme 4:
#names= ['Ivan','Pavel','Jordan']

#while True:
    # new=input("Кого добавим?")
    # if new ==names:
    #     print(names)
    # else:
    #     names.append(new)
    #     print(f"{new} добавлен")

#Theme 5:
# nums=[1,2,3,4,5]
# my_list=[i for i in range(1,20) if i in nums]
#
# print(my_list)

#Theme 6:
# my= dict(name="Jordan", job="Developer", age=23)
# my2=my.copy()
# print(my2)

#Theme 7:
# def new_list():
#     my_list=[1,2,3,4,5]
#     return my_list
#
# new_list()
# print(new_list())


#Theme 8:
# def funcia(a):
#     print(a+12)
#
# funcia(12)

# a=lambda b,c:b*c
# print(a(10,2))

#Theme 9:
# class Car:
#     def init(self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
#
#
# maluba=Car('Malubu2', "Black","2021")
# print(vars(maluba))

# #Theme 10:
#
# class Figura:
#     def init(self,width,height):
#         self.width=width
#         self.height=height
#
#     @property
#     def viches(self):
#         return self.width*self.height
#
#
#
# pryamougl=Figura(4,5)
# print(pryamougl.viches)

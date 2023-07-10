from faker import Faker

faker = Faker()
print(faker.email())

dict_test = {"qa":"New Member", "devOps":"New One", "Dev":"old Team"}
print(dict_test.items())

dict_test1 =dict_test.copy()
print(dict_test1.items())
dict_test1.update({1:25})
print(dict_test1)
print(dict_test1.clear())

city = "Sunnyvale"
x = 0
while x <= len(city):
    print(city[0:x])
    x = x + 1
print("Done")

email = input("Enter your email adress: ")
print(type(email))



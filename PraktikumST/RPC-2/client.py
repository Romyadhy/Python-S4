import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://192.168.31.112:8000')

# Input value from user/client
print("Welcome to this server, in here you can calculate the area of the triangle, please enter the value thar you want to input :>")
alas = float(input("Enter lenght base of the triangle: "))
tinggi = float(input("Enter height of the triangle: "))

# Function to calculate
luas_segitiga = proxy.areaTriangle(alas, tinggi)
print(f"The area of triangle with base {alas} and height {tinggi} is: {luas_segitiga}")

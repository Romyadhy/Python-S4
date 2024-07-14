from xmlrpc.client import ServerProxy, Fault

server = ServerProxy("http://localhost:9876/")

try:
    r_add = server.add(5, 5)
    print("The result of the addition is: " + str(r_add))
    
    r_sub = server.sub(3, 5)
    print("The result of the subtraction is: " + str(r_sub))
    
    r_div = server.div(10, 2)
    print("The result of the divided is: " + str(r_div))
    
    r_mul = server.mul(5, 3)
    print("The result of the multiplication is: " + str(r_mul))
    
    r_pow = server.pow(5)
    print("The result of the powering is: " + str(r_pow))
    
except Fault as e:
    print("Error:", e)
    
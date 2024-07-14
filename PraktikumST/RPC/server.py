from xmlrpc.server import SimpleXMLRPCServer

# Function
def add(a, b):
    return a + b

def sub(a, b):  
    return a - b
    
def div(a, b):
    return a / b
    
def mul(a, b):
    return a * b

def pow(a):
    return a * a

# Server
server = SimpleXMLRPCServer(("localhost", 9876))
print("Listening on port 9876....")
# Export function to server 
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(div, "div")
server.register_function(mul, "mul")
server.register_function(pow, "pow")
# runing the server
server.serve_forever()


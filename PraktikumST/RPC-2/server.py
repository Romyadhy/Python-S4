from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Limiting the admission pathway
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Using the IP local in this computer
with SimpleXMLRPCServer(('192.168.31.112', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Calculate area of the triangle
    def areaTriangle(alas, tinggi):
        return 0.5 * alas * tinggi
    server.register_function(areaTriangle, 'areaTriangle')

    # Run Server
    print(f"Server running on IP '192.168.31.112' and port 8000...")
    server.serve_forever()

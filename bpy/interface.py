from http.server import BaseHTTPRequestHandler, HTTPServer

import threading

def execute(py_code):
    # isolate python code (first instance of)
    
    
    ## Run
    
        ## Take errors

        ## Run up until errors

        ## Offer attributes if AttributeError

        ## Reply with error, line # (, attributes)
    
    
    try:
        exec(py_code)
        return "OK"
    except Exception as e: # TODO: better error handling with library
        return str(e)
    

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        text = data.decode('utf-8')
        print("Processing...")
        error = execute(text)
        
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(error.encode('utf-8'))


def start_server():
    httpd = HTTPServer(('localhost', 8000), Handler)
    httpd.serve_forever()

if __name__ == "__main__":
    thread = threading.Thread(target=start_server, daemon=True)
    thread.start()
    print("Background server started...")
    



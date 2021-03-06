from http.server import BaseHTTPRequestHandler
import json
import random as rand
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    
    def name_gen(self, key):
          key = key.lower()
          if key == 'male':
            first_names = 'api/male_first_names.txt'
          elif key == 'female':
            first_names = 'api/female_first_names.txt'
            
          last_names = 'api/last_names.txt'

          f = open(str(first_names), "r")
          first_names = f.read().split()

          f = open(str(last_names), "r")
          last_names = f.read().split()

          first_names_size = len(first_names)
          last_names_size = len(last_names)
          first_index = rand.randint(0, first_names_size)
          last_index = rand.randint(0, last_names_size)

          name = first_names[first_index]+" "+last_names[last_index]
          output = {key:name}

          json_value = json.dumps(output, ensure_ascii = False)
          return json_value
    
    def do_GET(self):
        s = self.path
        gen = parse_qs(urlparse(s).query)['gender'][0]
        self.send_response(200)
        self.send_header('Content-type','application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        output = self.name_gen(gen)
        json_value = json.dumps(output, ensure_ascii = False)
        result = json.loads(json_value)
        self.wfile.write(result.encode('utf8'))
        return

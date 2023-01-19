import json
from reconng import Recon

r = Recon()
r.add_module('use recon/domains-hosts/baidu_site')
r.add_module('set target example.com')
r.add_module('run')

results = json.loads(r.export_json())

for result in results:
    print(result)

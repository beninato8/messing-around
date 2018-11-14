cmd = "3*(4-2)"

import subprocess
print(subprocess.run('/usr/local/bin/python3 -c \"print({})\"'.format(cmd), shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8'))
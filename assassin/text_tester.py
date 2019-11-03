import subprocess
import contacts
cmd = subprocess.run

person = contacts.test_person
s = "test1"
p = "$HOME/bin/text"
out = cmd(f'{p} {person} "{s}"', shell=True, executable='/bin/zsh', stdout=subprocess.PIPE).stdout.decode('utf8')
print(out)

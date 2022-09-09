import hashlib
from hmac import HMAC
import code
import zipimport
import ast
import tabnanny
#zipimport = zipimport.zipimporter.get_code()
#print(ast.dump(ast.parse('a if b else c', mode='eval'))
import dis
#h = hashlib.new('sha256')
#h.update(b"Nobody inspects the spammish repetition")
#h.hexdigest()
#print(h)
def myfunc(alist):
    return len(alist)
print(dis.dis(myfunc))


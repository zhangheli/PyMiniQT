import site , os , sys
cwd = os.getcwd()
new_ss = os.path.join(os.path.abspath(cwd), "site-packages")
print(new_ss)

site.addsitedir(new_ss)

import PyQt5
print(PyQt5)

sys.path.append(cwd)

import Optimism
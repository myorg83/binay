from os import environ
from subprocess import Popen, PIPE

bash_variable = "$(git rev-parse --short HEAD)"
capture = Popen(f"echo {bash_variable}", stdout=PIPE, shell=True)
std_out, std_err = capture.communicate()
return_code = capture.returncode

if return_code == 0:
    evaluated_env = std_out.decode().strip()
    environ["COMMITID"] = evaluated_env
else:
    print(f"Error: Unable to find environment variable {bash_variable}")
#
print(environ.get('COMMITID'))
###
###
from os import environ
from subprocess import Popen, PIPE

bash_variable2 = "$(git show --pretty="" --name-only 15a9f8f)"
capture = Popen(f"echo {bash_variable2}", stdout=PIPE, shell=True)
std_out, std_err = capture.communicate()
return_code = capture.returncode

if return_code == 0:
    evaluated_env = std_out.decode().strip()
    environ["FILELIST"] = evaluated_env
else:
    print(f"Error: Unable to find environment variable {bash_variable2}")
#
print(environ.get('FILELIST'))

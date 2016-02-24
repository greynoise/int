# The C language trainer(InformatikTRainer - INT) written in Python
# License LGPL
# Author: Daniel Lindstedt

from subprocess import *

# compile line - TODO: make more generic
comp_cmd = "clang -o tmp/int.out tmp/int.c"
# program execute command
run_cmd = "tmp/int.out"


def convert_list_types(types, values):
    



# initial code - assume the user created an external textfile called int.c in the tmp folder that contains the full
# C-code including the required IO stuffs

# first off, compile the code, check if errors occurred and warn the user
pv = Popen(comp_cmd, shell=True, stdout = PIPE, stderr = PIPE)
err_pipe = pv.stderr;
err_str = err_pipe.read()
pv.communicate()
while (pv.returncode == None):
    # wait for compilation to finish
    pass

csuccess = 0

if (pv.returncode != 0):
    print "Compilation failed!"
    print "Error string: "
    print err_str
elif (pv.returncode == 0):
    csuccess = 1
    if (err_str != ""):
        print "Compilation succeeded with warnings:"
        print err_str
    else:
        print "Compilation succeeded"

if (csuccess == 1):

    # generate list of arguments for the program and convert it to a string for communication via
    # stdin/out pipes
    args = [115,3]
    argtypes = ['i', 'i']
    argstr = ""
    for x in args:
        argstr = argstr + str(x) + "\n"

    # also, generate the expected results
    results = [args[0]+args[1]]
    restypes = ['i']
    


    # execute the program
    pv = Popen(run_cmd, shell=True, stdout = PIPE, stdin = PIPE, stderr = PIPE)

    # provide the arguments to the program from arglist and read back the input check string and the
    # results from the program (to ensure arguments were passed correctly, if that fails output a fatal error)
    # the C program must use stderr to return it's results and stdout for the check string
    pout = pv.communicate(argstr)
    print pout
    checklist = pout[0].split(';')
    # drop the last element from the checklist, because the c program output appends ; to the last
    # element
    checklist = checklist[:-1]
    #convert the checklist to the corresponding types
    for idx, x in enumerate(argtypes):
        if x == 'i':
            checklist[idx] = int(checklist[idx])

    if (checklist != args):
        print "FATAL ERROR: Argument list was not received correctly by user program"

    # get the result list
    resultlist = pout[1].split(';')
    resultlist = resultlist[:-1]
    # convert result list to the corresponding types
    for idx, x in enumerate(restypes):
        if x == 'i':
            resultlist[idx] = int(resultlist[idx])
    print resultlist



import sys
from subprocess import *



def add_org(org_name):
    command = 'sudo /usr/local/bin/RACaddorg {}'.format(org_name)

    output = None
    try:
        output = check_output(command, shell=True,stderr=STDOUT)
    except CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    
    if output is not None:

        for line in output.split('\n'):
            if line.startswith('org='):
                orgname = line[4:].strip()
                print orgname
                # check server for actual dir location for 2nd validation

                return (1, orgname) 
    return (0,'')

def add_user(machine_user_id, organization_machine_name):
    # try add add
    # possible check next account exist in LDAP

    command = 'sudo /usr/local/bin/RACadd2grp {} {}'.format(organization_machine_name,machine_user_id)

    output = None
    try:
        output = check_output(command, shell=True,stderr=STDOUT)
    except CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    # return results
    return True

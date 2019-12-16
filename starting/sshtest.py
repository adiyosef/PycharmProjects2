

import paramiko
import sys
import 


if len(sys.argv) < 3:
    print
    "args missing"
    sys.exit(1)
hostname = "10.90.225.82"
hostname = sys.argv[1]

username = "root"
port = 22

try:
    client =
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect(hostname, port=port, username=username, password="@daRit3Us3r")

    stdin, stdout, stderr = client.exec_command(mkdir /adi)
    print
    stdout.read(),

finally:
    client.close()
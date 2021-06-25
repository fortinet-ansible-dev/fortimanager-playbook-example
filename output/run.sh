#! /bin/bash
BLACK="\033[30m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
PINK="\033[35m"
CYAN="\033[36m"
WHITE="\033[37m"
NORMAL="\033[0;39m"

for yml in `ls *.yml`
do
    printf "[RUN] $yml ..."
    ansible-playbook -i hosts $yml 1>/tmp/runtime.stdout 2>/tmp/runtime.stderr
    if [ $? -eq 0 ]; then
        echo -e $GREEN succeed $NORMAL
    else
        echo -e $RED fail $NORMAL
    fi
done

set -x


setOutput()
{
    if [ $# -ne 2 ]
    then
        echo "Key and value required on setOutput function call"
        exit 1
    fi
    echo ${2} > "/home/oracle/application/localhost/work/10776/10282/internal/outputs/${1}"
}


cp /home/artifact/* .
ls -latr

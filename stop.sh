#!/bin/bash

PID=`ps -ef |grep "/usr/bin/python3 -m flask" |grep -v grep |awk '{ print $2 }'`

if [ -z ${PID} ]
then
  echo "app is not running"
else
  kill ${PID}
fi

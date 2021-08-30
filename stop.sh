#!/bin/bash

echo "Stopping" >> ./app.log

PID=`ps -ef |grep gunicorn |grep -v grep |awk '{ print $2 }'|sort|head -1`

if [ -z ${PID} ]
then
  echo "App is not running" >> ./app.log
else
  echo "Killing ${PID}" >> ./app.log
  kill ${PID}
fi

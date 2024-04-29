#!/bin/bash
# filename: entrypoint.sh

# Start AWS SSM Port Forwarding in the background
aws ssm start-session \
  --region us-west-1 \
  --target i-0a1570bc9e71f1443 \
  --document-name AWS-StartPortForwardingSessionToRemoteHost \
  --parameters '{"host":["'"$RDSHOST"'"],
  "portNumber":["5432"],
  "localPortNumber":["5432"]}' &
  
# SSM_PID=$!

sleep 5

echo "Running your main application..."
python3 db_access.py

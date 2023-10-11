#!/bin/bash

path=$(pwd)
python=$(which python3)

# start log monitors for the docker container logs
osascript -e 'tell app "Terminal" to do script "docker logs --follow qs-pubsub-order-processor-1"'
osascript -e 'tell app "Terminal" to do script "docker logs --follow qs-pubsub-payment-processor-1"'
osascript -e 'tell app "Terminal" to do script "docker logs --follow qs-pubsub-city-london-1"'
osascript -e 'tell app "Terminal" to do script "docker logs --follow qs-pubsub-city-manchester-1"'
osascript -e 'tell app "Terminal" to do script "docker logs --follow qs-pubsub-city-york-1"'

# run the original consumer.py script to observe the general logging output on that topic
$python "${path}/consumer.py"

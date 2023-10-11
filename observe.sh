#!/bin/bash

path=$(pwd)
python=$(which python3)

# start log monitors for the docker container logs
osascript -e 'tell app "Terminal" to do script "docker logs --follow ps-order-processor-1"'
osascript -e 'tell app "Terminal" to do script "docker logs --follow ps-payment-processor-1"'
osascript -e 'tell app "Terminal" to do script "docker logs --follow ps-city-london-1"'
osascript -e 'tell app "Terminal" to do script "docker logs --follow ps-city-manchester-1"'
osascript -e 'tell app "Terminal" to do script "docker logs --follow ps-city-york-1"'

# run the original consumer.py script to observe the general logging output on that topic
$python "${path}/consumer.py"

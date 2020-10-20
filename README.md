# kafkacatrunner

###Installing:
First clone the repository, at the root folder of the project run: 

`python3 setup.py clean develop`

After this you should be ready to use it

###Usage Example: 
`kafkacatRunner -aps ./my-environment-config-file.conf -m jq -t myTopic -o 9999 -p 0`

Params:

**-m --mode** Mode which the kafkacat will be used, right now they can be Consumer mode (kc), Producer mode (kp), or jq mode (jq), required.
**-aps --authPathSource** Path to the file that you will be using with kafkacat against the source.
**-apt --authPathTarget** Path to the file that you will be using with kafkacat against the target (producer mode, for feeding from the source topic).
**-t --topic** Topic name that you will be using as source and target.
**-p --partition** Partition where you will be getting from the source.
**-o --offset** Offset from where you will be getting from the source.
**-f --format** Format for the kafkacat against the source.
**-jqq --jqQuery** Query where you can be filtering the results with jq.



# kafkacatrunner

### Installing:
First clone the repository, at the root folder of the project run: 

`python3 setup.py clean develop`

After this you should be ready to use it

### Usage Examples: 
Basic Usage

`kafkacatRunner -aps ./my-environment-config-file.conf -m jq -t myTopic -o 9999 -p 0`

You can use config files too!
`kafkacatRunner -c ./config.txt`

Here is a little example of config.txt:
```
mode=jq
authPathSource=./ba-kafka-staging.conf
topic=oi.receipt.analyzer
offset=2888060
```

And if needed you can override a part of your config file:

`kafkacatRunner -c ./config.txt -o 9999999999`

Params:

**-c --config** Config file where you can put your arguments here too (yaml file or ini file), it will be override by the other args

**-m --mode** Mode which the kafkacat will be used, right now they can be Consumer mode (kc), Producer mode (kp), or jq mode (jq), required.

**-aps --authPathSource** Path to the file that you will be using with kafkacat against the source.

**-apt --authPathTarget** Path to the file that you will be using with kafkacat against the target (producer mode, for feeding from the source topic).

**-t --topic** Topic name that you will be using as source and target.

**-p --partition** Partition where you will be getting from the source.

**-o --offset** Offset from where you will be getting from the source.

**-f --format** Format for the kafkacat against the source.

**-jqq --jqQuery** Query where you can be filtering the results with jq.

### Whats next:
Ideally, I'm going to create a param to set the initial parameters as a config, that you can override with the previous params for more flexibility, and add better support for building jq queries.



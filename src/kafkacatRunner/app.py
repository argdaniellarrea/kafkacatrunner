import os
import configargparse

#Arguments setup
parser = configargparse.ArgumentParser()
parser.add('-c', '--config', is_config_file=True, help='File to be used as config for kafkacatRunner, can be overriden by kafkacatRunner args')
parser.add_argument('-m', '--mode', type=str, help="Mode of work for kafka, it can be jq, kc (kafkacat consumer), krp (kafkacat relay producer), kp (kafkacat producer, not ready yet)", choices=['jq', 'kc', 'kdp', 'kp'], required=True)
parser.add_argument('-aps', '--authPathSource', type=str, help="File to be used as config in the source kafkacat command", required=True)
parser.add_argument('-apt', '--authPathTarget', type=str, help="File to be used as config in the target kafkacat command (kafkacat producer)")
parser.add_argument('-t', '--topic', type=str, help="Topic which kafkacat will get, and send for kafkacat producer mode", required=True)
parser.add_argument('-p', '--partition', type=str, help="Partition which kafkacat will get along with the topic, default is 0", default="0")
parser.add_argument('-f', '--format', type=str, help="Custom String format for kafkacat consumer mode")
parser.add_argument('-o', '--offset', type=str, help="Offset for the source kafka topic", default="0")
parser.add_argument('-jqq', '--jqQuery', type=str, help="jq query string for filtering topics messages", default="'.'")

#Parse arguments and variables
args, unknown = parser.parse_known_args()

#args
authPathSource = args.authPathSource
mode = args.mode
topic = args.topic
offset = args.offset
partition = args.partition

#kc args
_format = args.format
authPathTarget = args.authPathTarget

#jq args
jqQuery = args.jqQuery

def main():
    #SourceKafkacat command build
    command = ""
    command = "kafkacat "
    if authPathSource:
        command += "-F " + authPathSource + " "
    if topic:
        command += "-t " + topic + " "
    if partition:
        command += "-p " + partition + " "
    if offset:
        command += "-o " + offset + " "
    if _format:
        command += "-f " + _format + " "
    if mode == "kc":
        #kafkacat consumer mode check get from local kafka topic
        command += "-C -J -u "
    elif mode == "kdp":
        #kafkacat producer mode check feed from qa file
        command += "-C "
        command += "| kafkacat -P "
        if authPathTarget:
            command += "-F " + authPathTarget + " "
        if topic:
            command += "-t " + topic + " "
        command += "-z snappy -K: "
    elif mode == "jq":
        #jq mode
        command += "-C -u "
        command += "| jq "
        command += jqQuery
    print("Running command: " + command)
    os.system(command)


import argparse
#Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', type=str, help="Mode of work for kafka, it can be jq, kc (kafkacat consumer), kp (kafkacat producer)", choices=['jq', 'kc', 'kp'], required=True)
parser.add_argument('-aps', '--authPathSource', type=str, help="File to be used as config in the source kafkacat command", required=True)
parser.add_argument('-apt', '--authPathTarget', type=str, help="File to be used as config in the target kafkacat command (kafkacat producer)")
parser.add_argument('-t', '--topic', type=str, help="Topic which kafkacat will get, and send for kafkacat producer mode")
parser.add_argument('-p', '--partition', type=str, help="Partition which kafkacat will get along with the topic, default is 0", default="0")
parser.add_argument('-f', '--format', type=str, help="Custom String format for kafkacat consumer mode")
parser.add_argument('-o', '--offset', type=str, help="Offset for the source kafka topic", default="0")
parser.add_argument('-jqq', '--jqQuery', type=str, help="jq query string for filtering topics messages")

#Parse arguments and variables
args = parser.parse_args()

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
    command = "kafkacat "
    if authPathSource:
        command += "-F " + authPathSource + " "
    if topic:
        command += "-t " + topic + " "
    if partition:
        command += "-p " + partition + " "
    if offset:
        command += "-o " + offset + " "
    if mode == "kc":
        #kafkacat consumer mode check get from local kafka topic
        command += "-C "
        if _format:
            command += "-f " + _format
    elif mode == "kp":
        #kafkacat producer mode check feed from qa file
        command += "| kafkacat "
        if authPathTarget:
            command += "-F " + authPathTarget + " "
        if topic:
            command += "-t " + topic + " "
    elif mode == "jq":
        #jq mode
        command += "| jq "
        if jqQuery:
            command += jqQuery
    print(command)


import os
import time
import boto3

s = True

"Obtener los datos de la instancia"
AWS_REGION = "us-east-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = '****************'
instance = EC2_RESOURCE.Instance(INSTANCE_ID)

while s == True:

    "Dado que la instancia cambia la ip al reiniciarse obtenemos la nueva ip de la instancia"
    hostname = instance.public_ip_address

    if hostname == None:
        hostname = "a"

    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        print(hostname, " Is Up :)")
        time.sleep(60)

    else:
        print(hostname, " Is Down :(")
        print("rebooting..............")

        "Stop the instance"
        instance = EC2_RESOURCE.Instance(INSTANCE_ID)
        instance.stop()
        print(f'Stopping EC2 instance: {instance.id}')
        instance.wait_until_stopped()
        print(f'EC2 instance "{instance.id}" has been stopped')

        time.sleep(60)

        "Star the instance"
        instance.start()
        print(f'Starting EC2 instance: {instance.id}')
        instance.wait_until_running()
        print(f'EC2 instance "{instance.id}" has been started')
        print("Done :D")

        time.sleep(60)
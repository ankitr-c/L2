import subprocess
import os
def create_vm(instance_name):
    # gcloud_path = r'C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd'
    command = [
        'gcloud.cmd',
        'compute',
        'instances',
        'create',
        instance_name,
        '--image-family',
        'ubuntu-2004-lts',
        '--image-project',
        'ubuntu-os-cloud',
        '--machine-type',
        'e2-standard-2',
        '--tags',
        'http-server,https-server',
        '--zone',
        'asia-south1-c'
    ]
    subprocess.run(command, check=True)

vm_names = ['vm-instance-1', 'vm-instance-2', 'vm-instance-3', 'vm-instance-4', 'vm-instance-5']
for vm_name in vm_names:
    print(f'Creating VM: {vm_name}')
    create_vm(vm_name)

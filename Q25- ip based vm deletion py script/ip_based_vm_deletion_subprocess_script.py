# gcloud compute instances list --filter="networkInterfaces.accessConfigs.natIP=10.138.0.2 OR networkInterfaces.networkIP=10.138.0.2"
# gcloud compute instances delete my-vm --zone=us-central1-a
import subprocess

def delete_vm_by_ip(ip_address):
    try:
        op = subprocess.check_output(['gcloud.cmd', 'compute', 'instances', 'list', '--filter', f'networkInterfaces.accessConfigs.natIP={ip_address} OR networkInterfaces.networkIP={ip_address}'], text=True)
        vm_name=op.split('\n')[0].split(":")[1].strip()
        print(vm_name)
        command=['gcloud.cmd', 'compute', 'instances', 'delete', vm_name]
        ans=subprocess.run(command, check=True)
        print(ans)
        print("Vm: ",vm_name,"Deleted...!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

ip_address = "10.138.0.2"
delete_vm_by_ip(ip_address)

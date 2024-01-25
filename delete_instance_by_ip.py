from google.cloud import  compute_v1
from collections import defaultdict

def delete_vm_by_ip(project, ip_address):
    client = compute_v1.InstancesClient()
    zones = client.aggregated_list(project=project)
    all_instances = defaultdict(list)
    
    for zone, response in zones:
        if response.instances:
            all_instances[zone].extend(response.instances)
            for instance in response.instances:
                network_ip=instance.network_interfaces[0].network_i_p
                internal_ip=instance.network_interfaces[0].access_configs[0].nat_i_p
                if network_ip==ip_address or internal_ip==ip_address:
                    operation = client.delete(project=project, zone=instance.zone.split("/")[-1], instance=instance.name)
                    operation.result()

                    print(f"Instance {instance.name} deleted..!")
                    return
    print(f"No instance found with IP address: {ip_address}")                

# Example usage
project_id = "master-project-410605"
# ip_address_to_delete = "35.202.38.132"  # Replace with the actual IP address

ip_address_to_delete=input("Enter IP address of Vm that is to be deleted::")
delete_vm_by_ip(project_id, ip_address_to_delete)



from unittest import skip
import boto3
import csv

l1=[]
client1=boto3.client('ec2')
response1 = client1.describe_regions()
for j in response1['Regions']:
    # print('Region Name=', j['RegionName'])
    l1.append(j['RegionName'])

with open('cluster_detail.csv','w',newline='') as f: 
    fieldnames=['RegionName','ClusterName'] 
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(l1)):
        client = boto3.client('eks',region_name=l1[i])
        response = client.list_clusters()
    
        for j in response['clusters']:
            if j==[]:
                skip
            else:
                str1 = "" 
                s=response['clusters']
    # traverse in the string  
                for ele in s: 
                    str1 += ele  
    
    # return string  
                        # return str1
                # print("region=",l1[i],"Cluster Name=",response['clusters'])
                writer.writerow({
                    'RegionName':l1[i],
                    'ClusterName':str1
                })
                




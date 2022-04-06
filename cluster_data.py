from unittest import skip
import pandas as pd
import xlsxwriter,boto3
import from_dict

writer = pd.ExcelWriter('multiple.xlsx', engine='xlsxwriter')



# r={'RegionName':[],'ClusterName':[]}
r1=[]
c=[]

l1=[]
client1=boto3.client('ec2')
response1 = client1.describe_regions()
for j in response1['Regions']:
    # print('Region Name=', j['RegionName'])
    l1.append(j['RegionName'])
df = pd.DataFrame({'Regions':l1})
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
                # r['RegionName'].extend(l1[i])
                # r['ClusterName'].extend(str1)
                r1.append(l1[i])
                c.append(str1)

# df1=pd.DataFrame(''.join(list(r.items())),columns=['RegionName','ClusterName'])
df1=pd.DataFrame({
    'RegionName':r1,
    'ClusterName':c
})
#df = pd.DataFrame(list(my_dict.items()),columns = ['column1','column2'])
df.to_excel(writer, sheet_name='AllRegions',index=False)
df1.to_excel(writer, sheet_name='ClusterInfo',index=False)

writer.save()

# print(df)
import boto3
import pandas as pd
import xlsxwriter
session = boto3.Session()

writer=pd.ExcelWriter('services.xlsx', engine='xlsxwriter')
l=[]
services = session.get_available_services()
for i in services:
    l.append(i)
    # print(i)

l1=['account','acm','autoscaling','cloudfront','cloudtrail','cloudwatch',\
    'ec2','ebs','ecr','eks','elasticache','elb','health',\
    'iam','lambda','logs','rds','route53','s3','ses','sns','support']
# print(l)
l2=['autoscaling','ec2','eks']



# s1=session.get_available_resources()
# for j in s1:
#     print(j)

# print('------------------------------')
# s2=session.get_available_regions(service_name='ec2')
# for k in s2:
#     print(k)

df=pd.DataFrame({'AllServices':l})
df1=pd.DataFrame({'UsedServices':l1})
df2=pd.DataFrame({'RunningServices':l2})

df.to_excel(writer,sheet_name='AllServices',index=False)
df1.to_excel(writer,sheet_name='UsedServices',index=False)
df2.to_excel(writer, sheet_name='RinningServices',index=False)
writer.save()


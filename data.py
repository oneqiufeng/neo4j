import csv
import py2neo
from py2neo import Graph,Node,Relationship,NodeMatcher,RelationshipMatcher
#py2neo、import、neo4j自带的语言

g=Graph('http://localhost:7474',user='neo4j',password='12345678',name='neo4j')
#输入neo4j的数据库信息

'''
# Wait 60 seconds before connecting using these details, or login to https://console.neo4j.io to validate the Aura Instance is available
NEO4J_URI=neo4j+s://fa496689.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=wob3tHrD2RNa1jOmxkcbbT-dS21pRm9WkTDWmr8HEig
AURA_INSTANCEID=fa496689
AURA_INSTANCENAME=Instance01
'''

with open('C:\Users\qiufe\Desktop\学者关联.csv','r',encoding='gbk')as f:
    reader=csv.reader(f)
    for item in reader:
        if reader.line_num==1:
            continue
        print("当前行数：",reader.line_num,"当前内容：",item)
#open文件，地址是"C:\Users\qiufe\Desktop\au2best.csv"

#创建节点
        node_1=Node(label='项目名称',name=item[0])
        node_1['发布时间']=item[2]
        node_1['招标编号']=item[3]
        node_1['招标估价']=item[5]
        node_1['中标金额']=item[6]
        node_1['采购类型']=item[9]
        node_1['评审专家']=item[10]
        node_2=Node(label='项目名称',name=item[1])
        node_3=Node(label='项目名称',name=item[4])
        node_4=Node(label='项目名称',name=item[7])
        node_5=Node(label='项目名称',name=item[8])

#创建关系
        relation_1 = Relationship(node_1,'发布年份',node_2)
        relation_2 = Relationship(node_1,'地区',node_3)            
        relation_3 = Relationship(node_1,'招标单位',node_4)
        relation_4 = Relationship(node_1,'中标单位',node_5)
        relationships=[relation_1,relation_2,relation_3,relation_4]

#neo4j中创建节点
#g.create(test_node_1)
#g.create(test_node_2)

#覆盖式创建节点
#自动匹配相同内容的node产生联系
        g.merge(node_1,"项目名称","name")
        g.merge(node_2,"发布年份","name")
        g.merge(node_3,"地区","name")
        g.merge(node_4,"招标单位","name")
        g.merge(node_5,"中标单位","name")
        g.merge(relation_1,"发布年份","name")
        g.merge(relation_2,"地区","name")
        g.merge(relation_3,"招标单位","name")
        g.merge(relation_4,"中标单位","name")
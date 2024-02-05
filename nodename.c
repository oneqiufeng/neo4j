// 增加标签啊
match (e{name:"Demi Moore"}) set e: 杰青 return e

// 搜索匹配的节点，然后对每个节点执行更新属性的操作
MATCH (n:Node{type:'type'}) 
SET n.date= today()

// 循环执行100次 
WITH range(1,100) AS it 
UNWIND it AS i 
MATCH 
// …

// 根据路径中节点数进行循环，使用nodes(path)函数 
// 如果是对边操作，可以用relationships(path)函数 
MATCH path = (a) -[:LIKES]-> (b) 
WITH nodes(path) AS nodes 
UNWIND nodes AS node 
// … …

// 二重循环: 生成九九乘法表 
WITH range(1,9) AS it1 
WITH range(1,9) AS it2 
UNWIND it1 AS i 
UNWIND it2 AS j 
RETURN i* j

// 标签是一个string数组，属性是一个map
UWNIND {batch} as row
CALL apoc.create.node(row.labels, row.properties) yield node
RETURN count(*)

// 在apoc.create.*方法中，也提供了设置／更新／删除属性和标签的功能
UWNIND {batch} as row
MATCH (from) WHERE id(n) = row.from
MATCH (to:Label) where to.key = row.to
CALL apoc.create.relationship(from, row.type, row.properties, to) yield rel
RETURN count(*)
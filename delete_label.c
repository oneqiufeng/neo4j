//删除节点的标签
match(n:youqing) remove n:youqing return n

//删除特殊节点
MATCH (r)
WHERE id(r) = 492
DELETE r
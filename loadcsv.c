// 跳过 NULL 值
LOAD CSV WITH HEADERS FROM 'file:///companies.csv' AS row
WITH row WHERE row.Id IS NOT NULL
MERGE (c:Company {companyId: row.Id});
// "C:///Users///qiufe///Desktop///学者关联.csv"

//  clear data
MATCH (n:Company) DELETE n;

//  为 NULL 值设置默认值
LOAD CSV WITH HEADERS FROM 'file:///companies.csv' AS row
MERGE (c:Company {companyId: row.Id, hqLocation: coalesce(row.Location, "Unknown")})

//  clear data
MATCH (n:Company) DELETE n;

//  设置空字符串为 NULL 值
LOAD CSV WITH HEADERS FROM 'file:///companies.csv' AS row
MERGE (c:Company {companyId: row.Id})
SET c.emailAddress = CASE trim(row.Email) WHEN "" THEN null ELSE row.Email END

// --- //

// 跳过 NULL 值
LOAD CSV WITH HEADERS FROM '"C:/Users/qiufe/Desktop/file:///学者关联.csv' AS row
WITH row WHERE row.Id IS NOT NULL
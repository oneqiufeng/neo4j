from neo4j import GraphDatabase

def batch_label_nodes(node_ids, labels):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "your_password"))
    
    def label_node(node_id, label):
        with driver.session() as session:
            query = f"match (n:{node_id}) set n:{label} return n"
            result = session.run(query)
            print(f"Label '{label}' applied to node ID: {node_id}")

    for node_id, label in zip(node_ids, labels):
        label_node(node_id, label)

    driver.close()

# 示例
node_ids = [1, 2, 3, 4, 5]
labels = ["label1", "label2", "label3", "label4", "label5"]
batch_label_nodes(node_ids, labels)

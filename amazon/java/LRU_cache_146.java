class DoubleLinkedNode() {
	int key;
	int value;
	DoubleLinkedNode pre;
	DoubleLinkedNode post;
}

private void addNode(DoubleLinkedNode node){
	node.pre = head;
	node.post = head.post;
	head.post.pre = node;
	head.post = node;
}

private void removeNode(DoubleLinkedNode node){
	DoubleLinkedNode pre = node.pre;
	DoubleLinkedNode post = node.post;
	pre.post = post;
	post.pre = pre;
}

private void moveToHead(DoubleLinkedNode node){
	this.removeNode(node);
	this.addNode(node);
}

private DoubleLinkedNode popTail(){
	DoubleLinkedNode res = tail.pre;
	this.removeNode(res);
	return res;
}

private Hashtable<Integer, DoubleLinkedNode>
	cache = new Hashtable<Integer, DoubleLinkedNode>();

private int count;
private int capacity;
private DoubleLinkedNode head, tail;

public LRUCache(int capacity){
	this.count = 0;
	this.capacity = capacity;
	head = new DoubleLinkedNode();
	head.pre = null;
	tail = new DoubleLinkedNode();
	tail.post = null;
	head.post = tail;
	tail.pre = head;
}

public int get(int key){
	DoubleLinkedNode node = cache.get(key);
	if (node == null){
		return -1;
	}
	this.moveToHead(node);
	return node.value;
}

public void set(int key, int value){
	DoubleLinkedNode node = cache.get(key);
	if (node = null){
		DoubleLinkedNode newNode = new DoubleLinkedNode();
		newNode.key = key;
		newNode.value = value;
		this.cache.put(key, newNode);
		this.addNode(newNode);
		count++;

		if (count>capacity){
			DoubleLinkedNode tail = this.popTail();
			this.cache.remove(tail.key);
			count--;
		} 
	} else {
		node.value = value;
		this.moveToHead(node);
	}
}
# Java算法技巧——HashMap

### 基本用法
```
HashMap<Integer, Integer> hash = new HashMap<>();
int key = 1001;
int value = 1002232;
hash.containsKey(key); // => false，是否包含某个键
hash.containsValue(value); // => false，是否包含某个值
hash.put(key, value); //=> 哈希表中添加键值对
hash.remove(key); // 删除键为key的键值对
hash.size();   // => 1, 大小
hash.clear();  // 清空哈希表
hash.isEmpty();  // => true, 判断是否为空
hash.values();  // => [],返回值的集合
```
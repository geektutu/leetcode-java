# Java算法技巧——List

## ArrayList
ArrayList是一个类似于数组的List，对于只需要末尾添加元素和要求高效随机访问时使用

### ArrayList基本用法
```java
List<Integer> result = new ArrayList<>();
int tmp;
int[] arr;
result.add(1);  // => [1]，添加元素
result.add(3);  // => [1, 3]，添加元素
tmp = result.size();  // => 2，大小
tmp = result.get(1);  // => 3，返回该位置值
tmp = result.set(0, 5); // => [5, 3]， 设置
tmp = result.remove(0);  // =>  5，删除并返回该位置值
result.clear();  // =>  清空
```


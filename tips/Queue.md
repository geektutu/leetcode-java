# Java算法技巧——队列

## Queue
### PriorityQueue（优先队列）
```java
// 默认小值先出队，如果需要大值先出队，则重写比较函数，如下
// 自定义类，则必须重写比较函数，升序大值优先，降序小值优先
Queue<Integer> queue = new PriorityQueue<>(10, new Comparator<Integer>() {
    @Override
    public int compare(Integer o1, Integer o2) {
        if (o1 < o2) return 1;
        if (o1 > o2) return -1;
        return 0;
    }
});
queue.add(5);
queue.add(3);
queue.offer(4); // 推荐使用offer而非add，poll而非remove，成否与否返回布尔值，不会抛异常
queue.peek(); // => 5，取栈顶元素
queue.poll(); // => 5，出队并返回栈顶元素
```
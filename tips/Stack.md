# Java算法技巧——栈

### 标准库（java.util.Stack）
```java
Stack<Character> stack = new Stack<Character>(); // => 泛型需要指定类型
stack.isEmpty(); // => true 判断是否为空
stack.empty();   // => true，在java中的实现为判断stack.size()是否为0
stack.push('c');
stack.push('d'); // => 入栈操作
stack.size(); // => 1，栈内有多少元素
char ch = stack.peek(); // ch == 'd'，获取栈顶元素
ch = stack.pop(); // ch == 'd'，出栈并返回栈顶元素
```


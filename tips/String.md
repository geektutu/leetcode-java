# Java算法技巧——字符串类

## String

### 字符串转数字
```java
String s = "123";
int value = Integer.parseInt(s); // => 123
value = Integer.valueOf(s) // => 123
```

### 数字转字符串
```java
int value = 123;
String s = Integer.toString(value); // => "123"
s = String.valueOf(value); // => "123"
s = "" + value // => "123"
```

### 字符串，转字符（数组）
```java
String s = "abc";
char[] chars = s.toCharArray(); // => ['a','b','c']
chars[2] == s.charAt(2) // => true
```

### 字符数组转字符串
```java
char[] a = {'1', '2', '3', '4'};
String str = String.valueOf(a); // => "1234" 调用valueOf方法
str = String.valueOf(a, 2 ,2);  // => "34"，valueOf(data[], offset, count) 
str = new String(a);  // => "1234" 构造函数转换
```

### 子串 
```java
String s = "abc"
String sub = s.substring(1, 3); // => "bc"
sub = s.substring(1,2); // => "b"，(start,end)，start->end-1，不包含end
```

### 分割
```java
public String[] split(String regex, int limit)
public String[] split(String regex)

String s = "ab-bc-cd-de"
String[] str = s.split("-") // => ["ab", "bc", "cd", "de"]
str = s.split("-", 2) // => ["ab","bc-cd-de"], 分割为2段，
str = s.split("-", 1) // => ["ab-bc-cd-de"]，1->不分割，0->全分割
```

> 参考：[java split](http://www.tutorialspoint.com/java/java_string_split.htm)

### 查找
```java
// 查找返回位置
String str = "abcdecdedf"
str.indexOf("cde") // => 2
str.indexOf("xyz") // => -1
str.lastIndexOf("cde") // => 5，从后往前
// 仅判断是否存在
str.contains("cde") // => true
str.contains("xyz") // => false
```

### 去除行首行末空格
```java
String str = "   hello  ".trim() // => "hello"
```

## StringBuilder
> String提供的字符串增删改功能不完善，且效率较低，StringBuilder提供了十分高效的方法

### StringBuilder常用方法

```java
StringBuilder result = new StringBuilder();
char[] chars = {'a', 'b', 'c', 'd', 'e'};
// 尾部添加
result.append(1);  // => "1"，自动将数字转为字符，不需要额外操作
result.append('2');  // => "12"，参数可以是 String, char[],double,int,char等
result.append(chars, 2, 2); // => "12cd"，append(chars[], offset, count),后2个参数可选
// 删除
result.delete(1,2);   // => "1cd", delete(start, end),不含end 
result.deleteCharAt(1);  // => "1d"
// 插入
result.insert(0, "abc"); // => "abc1d" // 在某个位置前插入char[]，String，int等
// 修改
result.setCharAt(1, 'B'); // => "aBc1d" // 修改
result.setLength(3);  // => "aBc"，后面的字符将被删除 
```




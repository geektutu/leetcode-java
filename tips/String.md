# Java算法技巧——字符串类

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



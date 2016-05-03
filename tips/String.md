# Java算法技巧——字符串类

### 字符串转数字
```java
String s = "123";
int value = Integer.parseInt(s); // => 123
```

### 数字转字符串
```java
int value = 123;
String s = Integer.toString(value); // => "123"
```

### 字符串，转字符（数组）
```java
String s = "abc";
char[] chars = s.toCharArray(); // => ['a','b','c']
chars[2] == s.charAt(2) // => true
```

### 子串 
```java
String s = "abc"
String sub = s.substring(1, 3); // => "bc"
sub = s.substring(1,2); // => "b"，(start,end)，start->end-1，不包含end
```
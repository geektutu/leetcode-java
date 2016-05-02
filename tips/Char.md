# Java算法技巧——字符类

### 字符转数字

```java
// 方法一
char ch = '1';
int value = Character.getNumericValue(ch);  // => 1
// 方法二
char ch = '9';
int value = ch - '0'; // => 9
```

### 数字转字符

```java
int value = 3;
char ch = value + '0'; // => '3'
```
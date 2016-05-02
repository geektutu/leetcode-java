# Java算法技巧——输入输出类

### 基本类库
```java
import java.io.*;  
import java.util.*;  
import java.math.*; 
```

> 参考：[java在ACM中的使用](http://blog.csdn.net/sssogs/article/details/8526384)

### 读取数据
```java
Scanner cin=new Scanner(System.in);  
// 或  Scanner cin=new Scanner(new BufferedInputStream(System.in));  
int n;  
n = cin.nextInt();  
System.out.println(n);  
```

### 输出结果
```java
int n = 10
System.out.println("Hello,ACM"); //自带换行符
System.out.print(n);  // 不带换行符
```

### 标准输入输出重定向
```java
// 获取当前类所在的路径
FirstApp.class.getResource("/").getFile()
// 输入(System.in)重定向到文件
System.setIn(new FileInputStream("filePath"));
// 输出(System.out)重定向到文件
System.setOut(new PrintStream(new FileOutputStream("filePath")));
```
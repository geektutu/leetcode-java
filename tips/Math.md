# Java算法技巧——数学类

### 高精度(java.math.BigInteger)
1. 加减乘除余

    ```java
    BigInteger a1 = new BigInteger("233");
    BigInteger a2 = new BigInteger("10");
    BigInteger result;
    result = a1.add(a2); // => 243
    result = a1.multiply(a2); // => 2430
    result = a1.subtract(a2); // => 223
    result = a1.divide(a2); // => 23
    result = a1.mod(a2); // => 3
    ```

2. 打印与转换
    
    ```java
    BigInteger a1 = new BigInteger("233");
    String s = a1.toString(); // => "233"，转换为字符串
    System.out.println(a1); // => 233，可直接输出 
    ```

3.比较
    
    ```java
    int value;
    value = a1.compareTo(a2); // 1, 前者大于后者 返回1
    value = a2.compareTo(a1); // -1, 前者小于后者，返回 -1
    value = a1.compareTo(a1); // 0, 数值上相等，则返回0
    ```



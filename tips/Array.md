### 数组的排序
```java
Arrays.sort(Type[] a, int fromIndex, int toIndex) 
```

### 数组的复制
```java
// 方法一
System.arraycopy(sourceArray, 0, targetArray, 0, sourceArray.length);  
// 方法二
int[] targetArray = (int[])sourceArray.clone(); // 返回是一个对象，需要强制类型转换
```
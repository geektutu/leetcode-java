# Java算法技巧——数组类

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

### Array 与 ArrayList的相互转换
```java
// int/Integer
List<Integer> list = Arrays.asList(1,2,3,4); // => ArrayList: [1,2,3,4]
Integer[] arr = {1,2,3}; // arr不能是int[]，否则，arr将当作一个int[]对象处理
List<Integer> list = Arrays.asList(arr); // => ArrayList: [1,2,3,4]
Integer[] intArr = (Integer[])list.toArray(); // => Integer[]: [1,2,3,4]
```

```java
// String
String[] strs = {"abc", "def"};
List<String> list = Arrays.asList(strs); // => ArrayList: ["abc", "def"]
String[] strArr = (String[]) list.toArray(); // => String[]: ["abc", "def"]
```
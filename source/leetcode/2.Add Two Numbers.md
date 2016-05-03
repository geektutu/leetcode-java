### [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

> You are given two linked lists representing two non-negative numbers.  <br/>
> The digits are stored in reverse order and each of their nodes contain a single digit. <br/>
> Add the two numbers and return it as a linked list. <br/>
> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) <br/>
> Output: 7 -> 0 -> 8

题目大意：给定2个链表代表2个整数（整数反转之后每一位存在链表的一个节点中，例如2->4->3 代表342），将这两个数相加，以链表形式返回结果

题目难度：Mediun

```java
import java.math.BigInteger;

/**
 * Created by gzdaijie on 16/5/2
 * 思路是依次读取链表中的值,将其还原为一个整数,需要用到BigInteger类
 * 最后,2个数相加,将和还原为链表，返回头指针即可
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        BigInteger result = new BigInteger("0");
        BigInteger n = new BigInteger("1");
        BigInteger times = new BigInteger("10");

        // 使用n记录位数,每进一位乘10
        while (l1 != null) {
            result = result.add(new BigInteger(Integer.toString(l1.val)).multiply(n));
            n = n.multiply(times);
            l1 = l1.next;
        }

        n = new BigInteger("1");
        while (l2 != null) {
            result = result.add(new BigInteger(Integer.toString(l2.val)).multiply(n));
            n = n.multiply(times);
            l2 = l2.next;
        }

        String s = result.toString();
        int len = s.length();
        char ch = s.charAt(len - 1);
        
        // head 保存头指针
        // tmp 指向尾部,不断新增节点
        ListNode head = new ListNode(Character.getNumericValue(ch));
        ListNode tmp = head;
        head.next = null;

        for (int i = len - 2; i > -1 ; i--) {
            ch = s.charAt(i);
            tmp.next = new ListNode(Character.getNumericValue(ch));
            tmp = tmp.next;
            tmp.next = null;
        }
        return head;
    }
}
```
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@email:     jayzhen_testing@163.com
@site:      https://github.com/gitjayzhen
@software:  PyCharm & Python 3.7
@file:      find_loop_port
@time:      4/9/21 3:13 PM

/找到链表中环的入口点
    public static Node findLoopPort(Node head){
        //首先判断头结点是否为null
        if(head==null||head.next==null)
            return null;
        Node fast = head,slow=head;
        //找到相遇点fast
        while (true) {
            if (fast == null || fast.next == null) {
                return null;
            }
            //找到
            slow = slow.next;
            fast = fast.next.next;

            if(fast == slow)
                break;
        }
        //相遇点与链表头分别设定一个指针,每次各走一步,相遇第一个点即为环入口点
        slow = head;//slow back to start point
        while(slow != fast){
            slow = slow.next;
            fast = fast.next;
        }
        return slow; //when slow == fast, it is where cycle begins
    }
"""


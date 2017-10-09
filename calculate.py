#-*- coding: utf-8 -*-
import random
from fractions import Fraction
import sys
import time


def initFix():#生成表达式（能生成随机数量的操作符1-10个）
    tmp = []
    opers = ['+', '-', '*', '/']
    n = random.randint(3, 10)
    flag = 1
    while n >= 0:
        if flag == 1:
            tmp.append(random.randint(1, 100))
            flag = 0
            if n == 0:
                break
        else:
            op = opers[random.randint(0, 3)]
            tmp.append(op)
            n -= 1
            flag = 1
    return tmp


def printFix(fix):#把表达式中元素全部转换成字符类型
    # for i in range(len(fix)):
    #     if type(fix[i]) == 'str':
    #         print fix[i],
    #     else:
    #         print str(fix[i]),
    # print '=',
    fixCopy = []
    for i in range(len(fix)):
        if type(fix[i]) == int:
            fixCopy.append(str(fix[i]))
        else:
            fixCopy.append(fix[i])
    fixCopy.append('=')
    return fixCopy


def Prior(op1, op2):#计算优先级
    if op1 == '*' and op2 == '+' or op1 == '*' and op2 == '-':
        return True
    if op1 == '/' and op2 == '+' or op1 == '/' and op2 == '-':
        return True
    return False


def changeToPostfix(exp):#转换后缀表达式
    stack = []
    postfix = []
    for i in range(len(exp)):
        if type(exp[i]) == int:
            postfix.append(exp[i])
        if type(exp[i]) == str:
            if stack:
                if Prior(exp[i], stack[-1]):
                    stack.append(exp[i])
                else:
                    while stack:
                        if Prior(exp[i], stack[-1]):
                            stack.append(exp[i])
                            break
                        else:
                            postfix.append(stack[-1])
                            stack.pop()
                    if not stack:
                        stack.append(exp[i])
            else:
                stack.append(exp[i])
    if stack:
        stack = stack[::-1]
        postfix.extend(stack)
    print postfix
    return postfix


def CalculatePostfix(exp):#计算后缀表达式
    stack=[]
    for i in range(len(exp)):
        if type(exp[i]) == int:
            stack.append(exp[i])
        if type(exp[i]) == str:
            # print exp[i]
            temp = calculate(exp[i], stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(temp)
    return stack[0]


def calculate(op, num1, num2):#计算元运算（+、-、*、/）
    if op == '+':
        restmp = Fraction(num1, 1) + Fraction(num2, 1)
    if op == '-':
        restmp = Fraction(num1, 1) - Fraction(num2, 1)
    if op == '*':
        restmp = Fraction(num1, 1) * Fraction(num2, 1)
    if op == '/':
        restmp = Fraction(num1, 1) / Fraction(num2, 1)
    return restmp


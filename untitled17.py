# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 20:14:51 2025

@author: Win 10
"""

import pandas as p
u=0
z='s'
while u==0:
 register= input('Signup\t / \t   Already a Customer:Login\n')
 if register=='Signup'or register=='signup' or register=='SIGNUP':
    usrname=input('username:')
    password=str(input('Password:'))
    idc={'Username':[usrname],'Password':[password]}
    a=p.DataFrame(idc).csv
    data=p.read_csv("C:\\Users\\Win 10\\OneDrive\\Documents\\gdsc.csv")
    list1=[]
    for i in range(len(data)):
        list1.append(data['Username'][i])
    if usrname in list1:
        print('this username has already been registered.Choose a different username or sign-up')
        z='failure'
    elif usrname not in list1:
        b= a.to_csv("C:\\Users\\Win 10\\OneDrive\\Documents\\gdsc.csv",index=False, header=False, mode='a')
        print('You have been registered. Enjoy your shopping')
        z='success'
 elif register=='Log-in' or register=='log-in' or register=='login'or register=='Login':
    usrname=input('username:')
    password=str(input('Password:'))
    data=p.read_csv("C:\\Users\\Win 10\\OneDrive\\Documents\\gdsc.csv")
    list2=[]
    list3=[]
    for i in range(len(data)):
      list2.append(data['Username'][i])
      list3.append(data['Password'][i])
    if usrname not in list2 :
      print('kindly  signup')
      z='failure'
    elif usrname in list2 and password !=list3[list2.index(usrname)]:
        print('Your password is wrong')
        print('Log in again or Create a new account and Sign in')
        z='failure'
    elif usrname in list2 and password ==list3[list2.index(usrname)]:
      print('Enjoy your shopping. You have been logged in')
      z='success'
 while z=='success':
     print("Choose the person with whom you want to chat")
     print(data["Username"])
     p=input("")
     if p not in data["Username"]:
         print("No such recipient found in your contacts")
     print("Type a message")
     s=input("")
     data['inbox'][p]=s
     q=input("Do u want to reply?")
     if q=="yes":
         r=input("Reply to the message")
         data["reply"][p]=r
     
     
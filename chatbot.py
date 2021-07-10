import pandas as pd
from tkinter import *
import csv
import string
import random
import os
import sys
import tkinter

str=''
stats=''
stats_req=''

class Botclass:

    def __init__(self,root):
        self.root = root
        self.DF = pd.read_csv(r'C:\Users\ABC\Desktop\Project Bot\Data\Replys.csv')
        self.que = list(self.DF['Question'])
        self.ans = list(self.DF['Answer'])
        self.info=''
        self.count = 0
        global str
        self.textarea = Label(self.root,text= str)
        self.textarea.pack()
        self.tbox = Entry(self.root, width=40)
        self.tbox.place(relx = 0.0,rely = 1.0,anchor ='sw')
        self.send = Button(self.root, text= 'send', command = self.clean, bg = 'red')
        self.send.pack(anchor='s',side=tkinter.RIGHT)
        self.bot_start()
    
    def check(self):
        self.yes = ['yes','y','ok','true']
        self.no = ['no','n','cancel','abort']
        for x in self.data:
          if x in self.yes:
            return True
          elif x in self.no:
            return False
        return 0
      
    def clean(self):
        global str
        global stats
        global stats_req
        self.data = self.tbox.get().lower()
        if len(self.data)==0:return
        self.data = self.data.replace('  ', ' ')
        self.data = ''.join([x for x in self.data if x not in string.punctuation]).split()
        if len(stats)!=0:
          if stats=='close':
             if self.check()==True:
               if stats_req=='':
                 str+= '\n' + ' '*25 + self.tbox.get().lower() +'\n' + 'Thank you!'
                 sys.exit(0)
               elif stats_req=='return':str+= '\n' + ' '*25 + self.tbox.get().lower() +'\n' + 'Your return request has been \n placed successfully!'
               else:str+= '\n' + ' '*25 + self.tbox.get().lower() +'\n' + 'Your order has been cancelled!'
               self.textarea['text'] = str
               self.tbox['text']=''
               return
             
             elif self.check()==False:
               str+= '\n' + ' '*25 + self.tbox.get().lower() +'\n' + 'Ok, let us continue...'
               stats = ''
               self.textarea['text'] = str
               self.tbox['text']=''
               return
             
             else:
               str+= '\n' + ' '*25 + self.tbox.get().lower() +'\n' + 'Invalid choice please enter yes or no'
               self.textarea['text'] = str
               self.tbox['text']=''
               return
             
          elif stats=='call':
             if self.check()==True:
               str+= '\n' + ' '*25 + self.tbox.get().lower() +'\n' + 'You will recieve a call from our executive shortly \n Thank you'
               self.textarea['text'] = str
               self.tbox['text']=''
               return
             
             elif self.check()==False:
               str+= '\n' + ' '*25 + self.tbox.get().lower() +'\n' + 'Ok, let us continue...'
               stats = ''
               self.textarea['text'] = str
               self.tbox['text']=''
               return
             
             else:
               str+= '\n' + ' '*25 + self.tbox.get().lower() +'\n' + 'Invalid choice please enter yes or no'
               self.textarea['text'] = str
               self.tbox['text']=''
               return
               
            
        self.bot_start()
               
                
        
    def bot_start(self):
        global str
        global stats
        global stats_req
        
        self.textarea['text'] = str
        
        if str == '':
          self.count=1
          self.tbox['state'] = 'disabled'
          n = random.randint(0,1)
          str+= '\n' + ' '*25 + self.que[n] +'\n' + self.ans[n]+'\n'
          self.sugg = Button(self.root,text = self.que[n],command = self.bot_start,fg='white',bg='blue')
          self.sugg.pack()
        
        elif self.count == 1:
          self.sugg.destroy()
          self.tbox['state'] = 'normal'
          self.count = 0
        
        else:
          for x in self.data:
             for y in self.que:
               z = y.lower()
               if x in z and len(x)>=4:
                  if 'close' in x or 'exit' in x or 'return' in x or 'cancel' in x:
                     stats = 'close'
                     if 'request' in x:
                       stats_req = 'return'
                     elif 'cancel' in x:
                       stats_req = 'cancel'
                  ndx = self.que.index(y)
                  str+= '\n' + ' '*25 +  self.tbox.get() +'\n' + self.ans[ndx]+'\n'
                  self.tbox['text']=''
                  self.count=1
                  self.textarea['text'] = str
                  break
             if self.count==1: break
          
          if self.count==0:
            if os.path.isfile(r'C:\Users\ABC\Desktop\Project Bot\Updates\to_be_updated.csv')==True:
              with open(r'C:\Users\ABC\Desktop\Project Bot\Updates\to_be_updated.csv','a') as a:
                      wrt = csv.writer(a)
                      wrt.writerow([''.join(self.data)])
            else:
              with open(r'C:\Users\ABC\Desktop\Project Bot\Updates\to_be_updated.csv','w') as a:
                      headerList=['Question']
                      wr=csv.DictWriter(a,delimiter=',',fieldnames=headerList)
                      wr.writeheader()
              with open(r'C:\Users\ABC\Desktop\Project Bot\Updates\to_be_updated.csv','a') as w:
                      wrt = csv.writer(w)
                      wrt.writerow([''.join(self.data)])
            
            str+= '\n' +' '*25 + self.tbox.get() + '\n' + 'This is an automated reply! \n Do you want to request a call \n from our executive?\n'
            self.tbox['text']=''
            self.textarea['text']=str
            stats='call'

      

root = Tk()
root.title('Chatbot')
root.geometry("240x250")
bot = Botclass(root)       
root.mainloop()
# =====================================
# Kakao Plus Friend 2.0
# Toolkit
# Author: Taekyung Kim(kimtk@suwon.ac.kr)
# Last update: 2018-04-09 
# 2018-03-18
#======================================
# == LIBRARY ========================================
from flask import Flask, request, jsonify
# == MessageBox
class MessageBox:
    """
> MessageBox.call("hi")
> MessageBox.callkeyboad("hi",['yes','no'])
    """
    @classmethod
    def call(cls,msg):
        return {"message":{"text":msg}}
    @classmethod
    def callpic(cls,msg,photo_url,buttons):
        return {"message":{"text":msg,"photo":{"url":photo_url,"width":640,"height":480}},"keyboard":{"type":"buttons","buttons":buttons}}
    @classmethod
    def callpicbutton(cls,msg,photo_url,label,url,buttons):
        return {"message":{"text":msg,"photo":{"url":photo_url,"width":640,"height":480},"message_button":{"label":label,"url":url}},"keyboard":{"type":"buttons","buttons":buttons}}
    @classmethod
    def callbutton(cls,msg,label,url):
        return {"message":{"text":msg,"message_button":{"label":label,"url":url}}}
    @classmethod
    def callkeyboard(cls,msg,buttons):
        return {"message":{"text":msg},"keyboard":{"type":"buttons","buttons":buttons}}
    @classmethod
    def callbuttonkeyboard(cls,msg,label,url,buttons):
        return {"message":{"text":msg,"message_button":{"label":label,"url":url}},"keyboard":{"type":"buttons","buttons":buttons}}
    @classmethod
    def start(cls,buttons):
        return {"type":"buttons","buttons":buttons}
# == Message
class Pic:
    def __init__(self,photo_url):
        self.photo_url=photo_url
    def get_photo_url(self):
        return self.photo_url
class PicButton:
    def __init__(self,photo_url,label,url):
        self.photo_url=photo_url
        self.label=label
        self.url=url
    def get_photo_url(self):
        return self.photo_url
    def get_label(self):
        return self.label
    def get_url(self):
        return self.url
class MessageButton:
    def __init__(self,label,url):
        self.label=label
        self.url=url
    def get_url(self):
        return self.url
    def get_label(self):
        return self.label
class Message:
    """
# Message Set
all_msg=[]
# Dialog Design
msg_child1=Message("chlid1?","child1!")
msg_child2=Message("child2?","child2!")
msg_super=Message("super?",super!",toMesssages=[msg_child1,msg_child2])
msgTop=Message("HOME","",toMessages=[msg_super,])
#hook
msg_child1.hook(msg_super)
msg_child1.hook(msgTop)
msg_child2.hook(msg_super)
msg_child2.hook(msg_super)
msg_super.hook(msgTop)
# Appending messages
all_msg.append(msg_child1)
all_msg.append(msg_child2)
all_msg.append(msg_super)
all_msg.append(msgTop)
# Communication
content="..."
considered_message=[m for m in all_msg if m.question == content]
if len(considered_message) > 0:
    msg=considered_message[0]
    response_to_kakaotalk=msg.echo()
    """
    def __init__(self,question,message,Ext=None,toMessages=None):
        self.message=message
        self.question=question
        self.ext=Ext
        self.kb=[]
        self.toMessages=toMessages
        self.generate_keys()
    def generate_keys(self):
        toMessages=self.toMessages
        if toMessages == None:
            return
        keys=[]
        append_key=keys.append
        #update keys
        for msg in toMessages:
            append_key(msg.question)
        self.kb=keys
    def hook(self,hooks):
        assert isinstance(hooks,list),"Hooks should be list"
        append_key=self.kb.append
        for hook in hooks:
            append_key(hook.question)
    def home(self):
        return MessageBox.start(self.kb)
    def echo(self):
        if len(self.kb)==0:
            if isinstance(self.ext,MessageButton):
                return MessageBox.callbutton(self.message,self.ext.get_label(),self.ext.get_url())
            else:
                return MessageBox.call(self.message)
        else:
            if isinstance(self.ext,MessageButton):
                return MessageBox.callbuttonkeyboard(self.message,self.ext.get_label(),self.ext.get_url(),self.kb)
            elif isinstance(self.ext,Pic):
                return MessageBox.callpic(self.message,self.ext.get_photo_url(),self.kb)
            elif isinstance(self.ext,PicButton):
                return MessageBox.callpicbutton(self.message,self.ext.get_photo_url(),self.ext.get_label(),self.ext.get_url(),self.kb)
            else:
                return MessageBox.callkeyboard(self.message,self.kb)

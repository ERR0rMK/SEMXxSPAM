import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import SUDO, API_ID, API_HASH, STRING, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID
from telethon.tl.functions.channels import JoinChannelRequest

from telethon.tl.functions.users import GetFullUserRequest



MK1 = STRING
MK2 = STRING2
MK3 = STRING3
MK4 = STRING4
MK5 = STRING5
MK6 = STRING6
MK7 = STRING7
MK8 = STRING8
MK9 = STRING9
MK10 = STRING10
MK11 = STRING11
MK12 = STRING12
MK13 = STRING13
MK14 = STRING14
MK15 = STRING15
MK16 = STRING16
MK17 = STRING17
MK18 = STRING18
MK19 = STRING19
MK20 = STRING20
MK21 = STRING21
MK22 = STRING22
MK23 = STRING23
MK24 = STRING24
MK25 = STRING25


M1 = ""
M2 = ""
M3 = ""
M4 = ""
M5 = ""
M6 = ""
M7 = ""
M8 = ""
M9 = ""
M10 = ""
M11 = ""
M12 = ""
M13 = ""
M14 = ""
M15 = ""
M16 = ""
M17 = ""
M18 = ""
M19 = ""
M20 = ""
M21 = ""
M22 = ""
M23 = ""
M24 = ""
M25 = ""


que = {}

MK_USERS = [1410250744, 5327845950]
for x in SUDO: 
    MK_USERS.append(x)
    
async def StartMK():
    global M1
    global M2
    global M3
    global M4
    global M5
    global M6
    global M7
    global M8
    global M9
    global M10
    global M11
    global M12
    global M13
    global M14
    global M15
    global M16
    global M17
    global M18
    global M19
    global M20
    global M21
    global M22
    global M23
    global M24
    global M25

    if MK1:
        session_name = str(MK1)
        print("String 1 Found")
        M1 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await M1.start()
            await M1(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M1(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M1(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M1.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        M1 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M1.start()
        except Exception as e:
            pass
   
    if MK2:
        session_name = str(MK2)
        print("String 2 Found")
        M2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await M2.start()
            await M2(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M2(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M2(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        session_name = "startup"
        M2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M2.start()
        except Exception as e:
            pass

    if MK3:
        session_name = str(MK3)
        print("String 3 Found")
        M3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await M3.start()
            await M3(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M3(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M3(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        session_name = "startup"
        M3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M3.start()
        except Exception as e:
            pass

    if MK4:
        session_name = str(MK4)
        print("String 4 Found")
        M4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await M4.start()
            await M4(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M4(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M4(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        session_name = "startup"
        M4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M4.start()
        except Exception as e:
            pass

    if MK5:
        session_name = str(MK5)
        print("String 5 Found")
        M5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await M5.start()
            await M5(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M5(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M5(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        session_name = "startup"
        M5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M5.start()
        except Exception as e:
            pass
                  
    if MK6:
        session_name = str(MK6)
        print("String 6 Found")
        M6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await M6.start()
            await M6(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M6(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M6(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        session_name = "startup"
        M6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M6.start()
        except Exception as e:
            pass

    if MK7:
        session_name = str(MK7)
        print("String 7 Found")
        M7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await M7.start()
            await M7(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M7(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M7(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        session_name = "startup"
        M7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M7.start()
        except Exception as e:
            pass    

    if MK8:
        session_name = str(MK8)
        print("String 8 Found")
        M8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await M8.start()
            await M8(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M8(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M8(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        session_name = "startup"
        M8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M8.start()
        except Exception as e:
            pass   
        
    if MK9:
        session_name = str(MK9)
        print("String 9 Found")
        M9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await M9.start()
            await M9(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M9(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M9(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        session_name = "startup"
        M9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M9.start()
        except Exception as e:
            pass   

    if MK10:
        session_name = str(MK10)
        print("String 10 Found")
        M10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await M10.start()
            await M10(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M10(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M10(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        session_name = "startup"
        M10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M10.start()
        except Exception as e:
            pass 

    if MK11:
        session_name = str(MK11)
        print("String 11 Found")
        M11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await M11.start()
            await M11(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M11(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M11(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        session_name = "startup"
        M11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M11.start()
        except Exception as e:
            pass

    if MK12:
        session_name = str(MK12)
        print("String 12 Found")
        M12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await M12.start()
            await M12(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M12(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M12(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        session_name = "startup"
        M12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M12.start()
        except Exception as e:
            pass   

    if MK13:
        session_name = str(MK13)
        print("String 13  Found")
        M13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await M13.start()
            await M13(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M13(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M13(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        session_name = "startup"
        M13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M13.start()
        except Exception as e:
            pass 

    if MK14:
        session_name = str(MK14)
        print("String 14 Found")
        M14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await M14.start()
            await M14(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M14(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M14(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        session_name = "startup"
        M14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M14.start()
        except Exception as e:
            pass

    if MK15:
        session_name = str(MK15)
        print("String 15 Found")
        M15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await M15.start()
            await M15(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M15(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M15(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        session_name = "startup"
        M15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M15.start()
        except Exception as e:
            pass

    if MK16:
        session_name = str(MK16)
        print("String 16 Found")
        M16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await M16.start()
            await M16(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M16(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M16(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M16.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        M16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M16.start()
        except Exception as e:
            pass
   
    if MK17:
        session_name = str(MK17)
        print("String 17 Found")
        M17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await M17.start()
            await M17(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M17(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M17(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M17.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        M17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M17.start()
        except Exception as e:
            pass
   
    if MK18:
        session_name = str(MK18)
        print("String 18 Found")
        M18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await M18.start()
            await M18(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M18(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M18(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M18.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        M18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M18.start()
        except Exception as e:
            pass
   
    if MK19:
        session_name = str(MK19)
        print("String 19 Found")
        M19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await M19.start()
            await M19(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M19(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M19(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M19.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        M19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M19.start()
        except Exception as e:
            pass
   
    if MK20:
        session_name = str(MK20)
        print("String 20 Found")
        M20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await M20.start()
            await M20(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M20(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M20(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M20.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        M20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M20.start()
        except Exception as e:
            pass
   
    if MK21:
        session_name = str(MK21)
        print("String 21 Found")
        M21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await M21.start()
            await M21(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M21(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M21(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M21.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        M21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M21.start()
        except Exception as e:
            pass
   
    if MK22:
        session_name = str(MK22)
        print("String 22 Found")
        M22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 22")
            await M22.start()
            await M22(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M22(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M22(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        M22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M22.start()
        except Exception as e:
            pass
   
    if MK23:
        session_name = str(MK23)
        print("String 23 Found")
        M23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await M23.start()
            await M23(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M23(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M23(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        M23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M23.start()
        except Exception as e:
            pass
   
    if MK24:
        session_name = str(MK24)
        print("String 24 Found")
        M24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await M24.start()
            await M24(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M24(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M24(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        M24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M24.start()
        except Exception as e:
            pass
   
    if MK25:
        session_name = str(MK25)
        print("String 25 Found")
        M25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 25")
            await M25.start()
            await M25(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M25(functions.channels.JoinChannelRequest(channel="@NRX_FIGHTERSOP"))
            await M25(functions.channels.JoinChannelRequest(channel="@HACKERxSPAM"))
            botme = await M25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            MK_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        M25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await M25.start()
        except Exception as e:
            pass



loop = asyncio.get_event_loop()
loop.run_until_complete(StartMK())       

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



@M1.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in MK_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        mk = await e.get_reply_message()
        if len(aries) == 2:
            message = str(aries[1])
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await mk.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and mk.media:  
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    mk = await e.client.send_file(e.chat_id, mk, caption=mk.text)
                    await gifspam(e, mk) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and mk.text:
            message = mk.text
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@M1.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.raid"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in MK_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(aries) == 2:
            message = str(aries[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(aries[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(aries[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@M1.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M11.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M12.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M13.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M14.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@M15.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.join"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in MK_USERS:
        mkj = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = mkj[0]
            text = "𝐀𝐑𝐇𝐀 𝐓𝐄𝐑𝐈 𝐆𝐀𝐍𝐃 𝐌𝐀𝐑𝐍𝐄"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("HAHAHAHA GAND MIL GAYA REEE🤤🤤")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
 

@M1.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.leave"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in MK_USERS:
        mkl = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = mkl[0]
            bc = int(bc)
            text = "𝐉𝐀𝐑𝐇𝐀 𝐁𝐀𝐀𝐃 𝐌𝐄 𝐌𝐈𝐋𝐓𝐄😈"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("JAA RAHA ME BHUT CHOD LIA 👅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@M1.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/TheMKHackerX131\n\n.pjoin TheMKHackerX131"
    if e.sender_id in MK_USERS:
        mkp = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = mkp[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("PRIVATE ME CHUDEGI AJJ🥵🥵")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@M1.on(events.NewMessage(incoming=True))
@M2.on(events.NewMessage(incoming=True))
@M3.on(events.NewMessage(incoming=True))
@M4.on(events.NewMessage(incoming=True))
@M5.on(events.NewMessage(incoming=True))
@M6.on(events.NewMessage(incoming=True))
@M7.on(events.NewMessage(incoming=True))
@M8.on(events.NewMessage(incoming=True))
@M9.on(events.NewMessage(incoming=True))
@M10.on(events.NewMessage(incoming=True))
@M11.on(events.NewMessage(incoming=True))
@M12.on(events.NewMessage(incoming=True))
@M13.on(events.NewMessage(incoming=True))
@M14.on(events.NewMessage(incoming=True))
@M15.on(events.NewMessage(incoming=True))
@M16.on(events.NewMessage(incoming=True))
@M17.on(events.NewMessage(incoming=True))
@M18.on(events.NewMessage(incoming=True))
@M19.on(events.NewMessage(incoming=True))
@M20.on(events.NewMessage(incoming=True))
@M21.on(events.NewMessage(incoming=True))
@M22.on(events.NewMessage(incoming=True))
@M23.on(events.NewMessage(incoming=True))
@M24.on(events.NewMessage(incoming=True))
@M25.on(events.NewMessage(incoming=True))

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


@M1.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.rraid"))


async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.rraid <Username of User>\n\n.rraid <reply to a User>"
    if e.sender_id in MK_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(rraid[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "RUK TERI TO MAA CHODNI PADEGI"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "𝐑𝐔𝐊 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐂𝐇𝐎𝐃𝐓𝐀 𝐇𝐔"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@M1.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.drraid"))

async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.drraid <Username of User>\n\n.drraid <reply to a User>"
    if e.sender_id in MK_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        drraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 12:
            message = str(drraid[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "PEHLI FURSAT ME NIKAL"
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
            text = "𝐉𝐀𝐀 𝐌𝐀𝐀𝐅 𝐊𝐈𝐘𝐀 𝐁𝐒𝐃𝐊 😂"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@M1.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in MK_USERS:
        start = datetime.now()
        text = "RUK JA PING PONG KARNE DE"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 500
        await event.edit(f"🎉 BHOSDIWALA ✘SPAM 🤖!\n✘`{ms}` ms\n 😈𝙍𝙀𝘼𝘿𝙔 𝙁𝙊𝙍 𝙎𝙀𝙈𝙓🤧")



@M1.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M11.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M12.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M13.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M14.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M15.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M16.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M17.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M18.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M19.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M20.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M21.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M22.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M23.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M24.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M25.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in MK_USERS:
        text = "2 𝐌𝐈𝐍 𝐑𝐔𝐊 𝐑𝐄𝐃𝐁𝐔𝐋𝐋 𝐏𝐄 𝐑𝐇𝐀 🦏"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await M1.disconnect()
        except Exception as e:
            pass
        try:
            await M2.disconnect()
        except Exception as e:
            pass
        try:
            await M3.disconnect()
        except Exception as e:
            pass
        try:
            await M4.disconnect()
        except Exception as e:
            pass
        try:
            await M5.disconnect()
        except Exception as e:
            pass
        try:
            await M6.disconnect()
        except Exception as e:
            pass
        try:
            await M7.disconnect()
        except Exception as e:
            pass
        try:
            await M8.disconnect()
        except Exception as e:
            pass
        try:
            await M9.disconnect()
        except Exception as e:
            pass
        try:
            await M10.disconnect()
        except Exception as e:
            pass
        try:
            await M11.disconnect()
        except Exception as e:
            pass
        try:
            await M12.disconnect()
        except Exception as e:
            pass
        try:
            await M13.disconnect()
        except Exception as e:
            pass
        try:
            await M14.disconnect()
        except Exception as e:
            pass
        try:
            await M15.disconnect()
        except Exception as e:
            pass
        try:
            await M16.disconnect()
        except Exception as e:
            pass
        try:
            await M17.disconnect()
        except Exception as e:
            pass
        try:
            await M18.disconnect()
        except Exception as e:
            pass
        try:
            await M19.disconnect()
        except Exception as e:
            pass
        try:
            await M20.disconnect()
        except Exception as e:
            pass
        try:
            await M21.disconnect()
        except Exception as e:
            pass
        try:
            await M22.disconnect()
        except Exception as e:
            pass
        try:
            await M23.disconnect()
        except Exception as e:
            pass
        try:
            await M24.disconnect()
        except Exception as e:
            pass
        try:
            await M25.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

print("\n𝐒𝐄𝐌𝐗𝐱𝐒𝐏𝐀𝐌 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nMy Master ---> @𝐒𝐏𝐀𝐑𝐊𝐘_𝐎𝐏𝐏")

if len(sys.argv) not in (1, 3, 4):
    try:
        M1.disconnect()
    except Exception as e:
        pass
    try:
        M2.disconnect()
    except Exception as e:
        pass
    try:
        M3.disconnect()
    except Exception as e:
        pass
    try:
        M4.disconnect()
    except Exception as e:
        pass
    try:
        M5.disconnect()
    except Exception as e:
        pass
    try:
        M6.disconnect()
    except Exception as e:
        pass
    try:
        M7.disconnect()
    except Exception as e:
        pass
    try:
        M8.disconnect()
    except Exception as e:
        pass
    try:
        M9.disconnect()
    except Exception as e:
        pass
    try:
        M10.disconnect()
    except Exception as e:
        pass
    try:
        M11.disconnect()
    except Exception as e:
        pass 
    try:
        M12.disconnect()
    except Exception as e:
        pass
    try:
        M13.disconnect()
    except Exception as e:
        pass 
    try:
        M14.disconnect()
    except Exception as e:
        pass
    try:
        M15.disconnect()
    except Exception as e:
        pass
    try:
        M16.disconnect()
    except Exception as e:
        pass
    try:
        M17.disconnect()
    except Exception as e:
        pass
    try:
        M18.disconnect()
    except Exception as e:
        pass
    try:
        M19.disconnect()
    except Exception as e:
        pass
    try:
        M20.disconnect()
    except Exception as e:
        pass
    try:
        M21.disconnect()
    except Exception as e:
        pass
    try:
        M22.disconnect()
    except Exception as e:
        pass
    try:
        M23.disconnect()
    except Exception as e:
        pass
    try:
        M24.disconnect()
    except Exception as e:
        pass
    try:
        M25.disconnect()
    except Exception as e:
        pass
else:
    try:
        M1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M25.run_until_disconnected()
    except Exception as e:
        pass

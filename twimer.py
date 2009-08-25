# twimer V0.0.1 
# Schedule ur tweets to be posted at a defined time or make twitter send u a reminder as a DM at set time.

# Author:Merin Loukrakpam
# Code license: Apache License 2.0


import twitter       # need python-twitter api for this
import time,sys



api=twitter.Api(username='m3Ryn',password='singjamei')    # making an instance of twitter.Api class with login credentials

mesg=str(raw_input("Press 't' to tweet,'r' for reminder,'q' to quit: "))


if mesg=='q':	
	print "Have a Great time!"
	sys.exit()
elif mesg== 't':
	hour,minute= [int(x) for x in raw_input("enter (hh:mm): ").split(":")]     # input the time u want ur tweets to be sent
 	tweet=raw_input("Type ur Tweet: ")                                         # input your tweet
elif mesg== 'r':
	hour,minute= [int(x) for x in raw_input("enter (hh:mm): ").split(":")]     # input the time u want ur tweets to be sent
	dmesg=raw_input("Type ur Reminder: ")     	                           # set your reminder

x=1
while x==1:
	var1=time.strftime("%H", time.localtime()) # call the present hour in 24hr format
	var2=time.strftime("%M", time.localtime()) # call the present minute

	var1,var2 =[ int(var1),int(var2)]     # converting into integer for comparision
	
	if (minute==var2) and (hour==var1):
		if mesg=='t':
			x=0
			status = api.PostUpdate(tweet,'m3Ryn')     # post ur tweet
			print status.text                         # print your tweet
		elif mesg=='r':
			x=0
			directMesg= api.PostDirectMessage('m3Ryn',dmesg)
			print directMesg.text
	else:
		x=1
	
print time.strftime("%d/%m/%y  %H:%M:%S", time.localtime())  # print the day and time of ur post (optional).


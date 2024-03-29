import websockets
import asyncio
import time
import json
from PrintColors import bcolors

class MyServer:

    def __init__(self, Domain, port, file="logs.txt") -> None:
        #Class initializer.
        self.Domain = Domain    #this is the domain through which I access the websocket
        self.port = port        #this is an extension of the domain
        self.file = file        #File to log events
        self.connections = {}   #A Dictionary (aka hashmap) of the websocket objects connected ot the server


    def start(self): 
        #you can make your outputs fun colors
        print(bcolors.WARNING + "About to start the server" + bcolors.ENDC)

        with open(self.file, "w") as file:
            file.writelines(bcolors.WARNING + "About to start the server" + bcolors.ENDC)

        """THIS INITIALIZES THE SERVER"""
        self.server = websockets.serve(self.handlerFunc, self.Domain, self.port)

        """THIS"""
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()


    async def handlerFunc(self, websocket):
        self.logMsg(bcolors.OKGREEN + "The server is up and running" + bcolors.ENDC)
        async for message in websocket:
            message = json.loads(message)
            if(message["Type"] == "Join" and len(self.connections) < 25):
                self.logMsg(bcolors.OKGREEN + "CONNECTION SUCCESSFUL" + bcolors.ENDC)

                tempID = message["Message"]

                await self.NewUserAlert(tempID)

                self.connections[tempID] = websocket
                await self.Pong(websocket, message)
                

    async def Pong(self, websocket, message):
        
        others = self.connections.keys()

        self.logMsg(bcolors.BOLD + str(self.connections) + bcolors.ENDC)        

        await websocket.send(self.genMsg("Welcome", list(self.connections)[-1], msg=list(others)))

        self.logMsg(bcolors.OKCYAN + "Got here just fine" + bcolors.ENDC)
        
        message = await websocket.recv()
        message = json.loads(message)

        while (message["Type"] == "PING" or message["Type"] == "Command"):

            if(message["Type"] == "Command"):
                await self.Talk(message)

            if(message["Type"] == "Close"):
                del self.connections[message["Sender"]]
                return 0


            time.sleep(2)
            await websocket.send(self.genMsg("PONG", message["Sender"]))
            self.logMsg(bcolors.HEADER + "PONG" + bcolors.ENDC)
            message = await websocket.recv()
            message = json.loads(message)

            
    async def NewUserAlert(self, ID):
        for device in self.connections:
            print(device)
            await self.connections[device].send(self.genMsg("New_User", device, msg=ID))
            

    async def Talk(self, msg):
        ID = msg["Recipient"]
        if ID not in self.connections:
            await websocket.send(self.genMsg("Command", msg["Sender"], "Selected User is not in the server"))
            return
        websocket = self.connections[ID]
        message = msg["Message"]
        self.logMsg("About to send a message")
        await websocket.send(self.genMsg("Command", ID, message, msg["Sender"]))
        self.logMsg("sent the message")

    def genMsg(self, Tpe, Recvr, msg="PONG", Sendr="Server"):
        newMsg = {"Type": Tpe, "Sender": Sendr, "Recipient": Recvr, "Message": msg}
        return json.dumps(newMsg)

    def logMsg(self, logstr):
        print(logstr)
        with open(self.file, "a") as file:
            file.writelines(logstr + "\n")
        


#I set up this server in its own file since I'm only ever going to need one of these.
print("\n" * 5)
server = MyServer("localhost", 8080)
server.start()


""" TO-DO:

"""

"""Done:
Ping-Pong
Integrated Messaging (Before JSON)
Alerts users when a new connection joins
Implemeted JSON messaging instead of strings
Text file logs
Closable Connections
Client To client communacation
"""
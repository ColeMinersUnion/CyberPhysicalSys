import websockets as ws
import asyncio
import json #not nessecary but common practice

class MyServer:

    def __init__(self, dom, port):
        self.Domain = dom
        self.port = port
        self.connections = {} #storing websocket objects


    async def start(self):
        async with ws.serve(self.handler, self.Domain, self.port):
        #this creates the server that runs a handler func at ws://Domain:port
            asyncio.get_event_loop().run_forever()

    async def handler(self, websocket): 
        message = await websocket.recv()
        msg = json.loads(message) #takes the json obj and turns it into a dictionary
        if(msg["Purpose"] == "Join" and not msg["Sender"] in self.connections.keys()): 
            self.connections[msg["Sender"]] = websocket
            #in here you can also assign roles and privileges to certain join codes
            await self.UpdateContacts(msg["Sender"])
        else:
            match msg["Purpose"]:
                case "Close":
                    await self.connections.pop(msg["Sender"]).send(self.goodbye())
                
                        
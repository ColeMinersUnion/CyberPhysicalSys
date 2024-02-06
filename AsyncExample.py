import asyncio 
"""
Asynchronous Events
wait's for a 'task' to be done
"""

#synchronous Task
def syncFunction():
    print("This happens immediately when called")

async def asyncFunction():
    await asyncio.sleep(10) #in this case, the task waiting to be done is sleep
    print("Prints immediately anyway")



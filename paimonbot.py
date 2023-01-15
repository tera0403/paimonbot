import discord
from discord.ext import commands
import datetime

with open('paimon.txt', 'r') as f:
    paimon_list = f.read().split("\n")
    

TOKEN = paimon_list[0]
CHANNELID = paimon_list[1]


client = discord.Client(intents=discord.Intents.all())
bot = discord.Client(intents=discord.Intents.all())

message_content = ['こんにちわ','非常食','えへっ']
message_command = ['/paimon','/help','.雷電','.天草雲','.刀鍔','.赤い実','.サウマラタ','.ルッカデヴァータ','.遺跡守衛','.計算機','.夜蘭','.イェラン']



@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    channel = client.get_channel(CHANNELID)
    if message.author.bot:
        return
    
    #送られてきたメッセージへの処理
    
    if message.content == message_command[0]:
        await channel.send('よお！')
        
    if message.content == message_command[1]:
        await channel.send('コマンドの一覧だぜ！')
        await channel.send('------------------------')
        for x in message_command:
            await channel.send(x)
            
    if message.content == message_command[2]:
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="雷電将軍",# タイトル
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="雷電将軍の情報だぜ！", # Embedの説明文 必要に応じて
                        url="https://gamewith.jp/genshin/article/show/287125" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # サムネイルを追加する(URL指定なので注意！)
        #embed.set_thumbnail(url="https://img.gamewith.jp/img/fda6cd39fba8291505a19ac8a7059771.jpg")

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://img.gamewith.jp/img/fda6cd39fba8291505a19ac8a7059771.jpg")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://gamewith.jp/genshin/article/show/287125", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url

        await channel.send(embed=embed)
        
    if message.content == message_command[3]:
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="天雲草の実",# タイトル
                        color=0x00ff00, # フレーム色指定
                        description="天雲草の実の情報だぜ！", # Embedの説明文 必要に応じて
                        url="https://gamewith.jp/genshin/article/show/292485" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # 画像を追加する(こちらもURL)
        embed.set_thumbnail(url="https://img.gamewith.jp/img/022110ad061d61e2ab6ab9b54246352e.png")
        embed.set_image(url="https://img.gamewith.jp/img/9418911c184d53072c22de7231397693.png")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://gamewith.jp/genshin/article/show/292485", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url
        
        await channel.send(embed=embed)
        
    if message.content == message_command[4]:
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="刀鍔",# タイトル
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="刀鍔の情報だぜ！", # Embedの説明文 必要に応じて
                        url="https://www.hoyolab.com/article/13809367" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/0bdbf348f82b021bb61d635e588baa0f_5396982415146486675.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://www.hoyolab.com/article/13809367", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url
        
        await channel.send(embed=embed)
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/1c374dee0f886d8995f0da8a5f4fe373_7197274479892978279.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/16610030544735a80181e1f9117f8653_2182888528560630452.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/992f1a54b70a9f9bacfc6d10247ddfe8_5401642829328036641.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/f16656407677f4e916d5976ffc7130d4_103736459511938218.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/b749785342215dfb7e8440d866090aa0_566033259319774004.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/2983bab27d1f0469581beeeed4391381_5548921170923808753.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/344360f7cccafb9a920badfa5f99f5fb_3425772511112380242.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/e4d9fa46806b1d79c0468b0771523fe7_4316742133624894622.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/a8349cea643d87951cadb350565b6273_1700839706604656660.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/2c69d544cf1c58c94e2397b29edb0de1_2517215513674068064.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/837ca4e982095ce9cb8d8a7cd2a98cb2_870191610713170062.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/6c1e291d7f58261a6749ca807fe46c9c_559118777242034229.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/b8732b83f38bfd9cbdf878baaf8b819e_7081968681150130539.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/b07299dc8b694bac581e73fa50a74a6f_1967334510178506639.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/11/18/248396084/aedff1ce5e0e8c3d571e6a5c78ec5a4a_5958577838016612890.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")


    if message.content == message_command[5]:
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="赤念の実",# タイトル
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="赤念の実の情報だぜ！", # Embedの説明文 必要に応じて
                        url="https://www.hoyolab.com/article/9989311" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396084/8dffa76810763cce4c9e221adfe08a2f_4425139616147654096.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://www.hoyolab.com/article/9989311", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url
        
        await channel.send(embed=embed)
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396084/7ed4a4ea063a48ba3693907305e58e58_6514793194574996233.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396084/ad87b74d40d4facfee7b12ec7f6006c3_903593131050884573.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396084/7d1e543a6426b03b92eb884f0404cdca_2795837053192481210.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396084/0655b2226d9e921e909d2bd5635024bd_6835690862603258744.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396084/6dcc9a28a9f46b96c4cc74f3b48a9de1_7505372884071138007.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396084/c0bd514cebdae8c56e061e156b64143e_1003629101913797629.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")
        await channel.send("https://upload-os-bbs.hoyolab.com/upload/2022/12/06/248396084/ae14a0c6a362132205b0c605b58ddf11_1325295468137296113.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

    if message.content == message_command[6]:
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="サウマラタ蓮",# タイトル
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="サウマラタ蓮の情報だぜ！", # Embedの説明文 必要に応じて
                        url="https://www.hoyolab.com/article/7256191" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://upload-os-bbs.hoyolab.com/upload/2022/08/28/16050299/91480e0d5332abeebdfd17023e94b1dc_2394650211200870185.png?x-oss-process=image/resize,s_1000/quality,q_80/auto-orient,0/interlace,1/format,png")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://www.hoyolab.com/article/7256191", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url
        
        await channel.send(embed=embed)

    if message.content == message_command[7]:
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="ルッカデヴァータダケ",# タイトル
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="ルッカデヴァータダケの情報だぜ！64個ルートだ！", # Embedの説明文 必要に応じて
                        url="https://gamewith.jp/genshin/article/show/360127" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://img.gamewith.jp/img/af6f6060df562974537daf1c888540b8.png")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://gamewith.jp/genshin/article/show/360127", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url
 
 
 
        await channel.send(embed=embed)
        await channel.send("https://img.gamewith.jp/img/865a302e6c9d7f9f5bb6236300a2492e.png")
        await channel.send("https://img.gamewith.jp/img/762008797ad1047a1ea66c77eeb7a5ec.png")
        await channel.send("https://img.gamewith.jp/img/47137717364f89c2f070e5dbcbf4d094.png")
        await channel.send("https://img.gamewith.jp/img/98b5ce721902aa93140f8cd9bb200683.png")

    if message.content == message_command[8]:
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="遺跡守衛",# タイトル
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="遺跡守衛の情報だぜ！", # Embedの説明文 必要に応じて
                        url="https://gamewith.jp/genshin/article/show/235746" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://img.gamewith.jp/img/c1817b17736c98bd7c0580b368c78b0e.jpg")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://gamewith.jp/genshin/article/show/235746", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url
        
        await channel.send(embed=embed)

    if message.content == message_command[9]:
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="育成計算機",# タイトル
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="育成計算機だぜ！", # Embedの説明文 必要に応じて
                        url="https://act.hoyolab.com/ys/event/calculator-sea/index.html?bbs_presentation_style=fullscreen&bbs_auth_required=true&utm_source=hoyolab&utm_medium=tools&lang=ja-jp&bbs_theme=light&bbs_theme_device=1#/" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://webstatic-sea.hoyoverse.com/upload/op-public/2022/08/04/22ca6086e52960c5a4eb727dac10d4dc_8090486626259571985.png")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://act.hoyolab.com/ys/event/calculator-sea/index.html?bbs_presentation_style=fullscreen&bbs_auth_required=true&utm_source=hoyolab&utm_medium=tools&lang=ja-jp&bbs_theme=light&bbs_theme_device=1#/", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url
        
        await channel.send(embed=embed)

    if (message.content == message_command[10]) or (message.content == message_command[11]):
        #送られてきたメッセージへの処理
        
        embed = discord.Embed( # Embedを定義する
                        title="イェラン",# タイトル
                        color=0x00ff00, # フレーム色指定(今回は緑)
                        description="イェランの情報だぜ！", # Embedの説明文 必要に応じて
                        url="https://gamewith.jp/genshin/article/show/326055" # これを設定すると、タイトルが指定URLへのリンクになる
                        )
        embed.timestamp = datetime.datetime.now()

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://img.gamewith.jp/article/thumbnail/rectangle/326055.png?date=1648462380")

        # 上側のユーザー情報を追加
        embed.set_author(name=client.user, url="https://gamewith.jp/genshin/article/show/326055", icon_url=client.user.avatar.url)
        #最新versionだとicon_url=client.user.avatar.urlだが古いverだとicon_url=client.user.avatar_url
        
        await channel.send(embed=embed)


    if message.content == message_content[0]:
        await channel.send('こんにちわっ！')
        
    if message.content == message_content[1]:
        await channel.send('おい！おいらは非常食じゃないぞっ！')
        
    if message.content == message_content[2]:
        await channel.send('えへってなんだよ！')
        


client.run(TOKEN)

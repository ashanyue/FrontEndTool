import requests
import json

# AE_LIST =
# https://game.fafafa3388.com/launch_demo?s=107027esfo&game_id=106
# for item in AE_LIST['GameList']:
#     response = requests.get('https://www.816396.com:6443/tb2d1/image/aeg/'+item['Code']+'.png')
#     with open('AE/'+item['Code']+'.png','wb') as file:
#         file.write(response.content)
# print(item['Code'])
# print(response.content)
# PP_LIST =
# http://demogames.pragmaticplay.net/gs2c/openGame.do?lang=cn&cur=CNY&gameSymbol=vs1fortunetree&lobbyURL=
# for item in PP_LIST['GameList']:
#     response = requests.get('https://www.816396.com:6443/tb2d1/image/ppg/'+item['Code']+'.png')
#     with open('PP/'+item['Code']+'.png','wb') as file:
#         file.write(response.content)

# MG_LIST = {}
# with open('MG.text', 'r') as file:
#     MG_LIST = json.load(file)
#     print(MG_LIST)
# # https://mobile22.gameassists.co.uk/MobileWebServices_40/casino/game/launch/lehucom/aDarkMatter/zh-cn?loginType=VanguardSessionToken&isPracticePlay=true&casinoId=2712&isRGI=true&authToken=
# for item in MG_LIST['data']['dataList']:
#     imageUrl = item['imageUrl']
#     game_code = item['gameCode']
#     remote_img = requests.get(imageUrl)
#     with open("MG/{}.jpg".format(game_code),'wb') as img_file:
#         img_file.write(remote_img.content)

# DT_LIST = {}
# with open('DT.text', 'r') as file:
#     DT_LIST = json.load(file)
#     print(DT_LIST)
# # http://play.dreamtech8.com/playSlot.aspx?gameCode=chess&isfun=1&type=dt&language=zh_CN
# for item in DT_LIST['data']['dataList']:
#     imageUrl = item['imageUrl']
#     game_code = item['gameCode']
#     remote_img = requests.get(imageUrl)
#     with open("DT/{}.jpg".format(game_code),'wb') as img_file:
#         img_file.write(remote_img.content)

# PNG_LIST = {}
# with open('PNG.text', 'r') as file:
#     PNG_LIST = json.load(file)
#     print(PNG_LIST)
# # https://bsicw.playngonetwork.com/casino/PlayMobile?pid=365&gid=rainforestmagicmobile&lang=zh_CN&practice=1&brand=e&width=100%&height=100%lobby=null
# for item in PNG_LIST['data']['dataList']:
#     imageUrl = item['imageUrl']
#     game_code = item['gameCode']
#     print(imageUrl)
#     remote_img = requests.get(imageUrl)
#     with open("PNG/{}.jpg".format(game_code),'wb') as img_file:
#         img_file.write(remote_img.content)

NT_LIST = {}
with open('NT.text', 'r') as file:
    NT_LIST = json.load(file)
    print(NT_LIST)
# https://yx678.load.xamahaha.com/disk2/netent/demo.html?game=eldorado_mobile_html&language=cn&lobbyUrl=null
for item in NT_LIST['data']['dataList']:
    imageUrl = item['imageUrl']
    game_code = item['gameCode']
    print(imageUrl)
    remote_img = requests.get(imageUrl)
    with open("NT/{}.jpg".format(game_code),'wb') as img_file:
        img_file.write(remote_img.content)
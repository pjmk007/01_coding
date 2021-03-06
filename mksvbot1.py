# -*-coding: utf-8-*-
import asyncio
# from asyncio.tasks import sleep
import discord
from discord.ext import commands
import sys
import random
import urllib.request
from bs4 import BeautifulSoup
# import json
# from urllib import parse
from urllib.parse import quote_plus
# from collections import OrderedDict
# # google calendar
# from google_calendar_api import GCalendar
# import datetime
# # google calendar

version = "0.3.9"
# client = discord.Client()
client = commands.Bot(command_prefix='...')


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("mk.svbot.1")
    await client.change_presence(status=discord.Status.online, activity=game)

    for guild in client.guilds:
        for channel in guild.text_channels:
            await channel.send(f"{channel.name}채널이 준비가 되었습니다...")


@client.command(name="자기소개")
async def self_intro(ctx):
    await ctx.send(f"저는 mk님이 최초로 창조한 봇 『svbot.1』 이라고 합니다...\n자비로운 주인님께서는 호형을 허락하셨기에, 저는 주인님을 형님으로 칭하고 있습니다...\n현재 10개의 명령어 셋을 제공하고 있으며, 이 명령어들은 주인님의 편의와 유희를 위한 기능을 제공하고 있습니다...\n주인님은 '...'로 명령어를 시작하며, 저는 대답을 '...'로 종결하도록 프로그래밍 되었습니다...\nVersion = {version}...")


@client.command(name="목록")
async def order_list(ctx):
    embd_ol = discord.Embed(title="**명령어 목록...**", description="명령어와 설명은 아래와 같아요...", color=0x62c1cc)
    embd_ol.add_field(name="*...자기소개*", value="`봇의 정보를 간략히 소개합니다...`", inline=False)
    embd_ol.add_field(name="*...목록*", value="`봇에게 내릴 수 있는 명령어 목록을 출력합니다...`", inline=False)
    embd_ol.add_field(name="*...안녕*", value="`주인을 맞이하는 인사를 합니다...`", inline=False)
    embd_ol.add_field(name="*...쉬어*", value="`주인의 명을 받들어 잠시 대기합니다...`", inline=False)
    embd_ol.add_field(name="*...ㅈ같냐?*", value="`한숨을 쉬고 의견을 피력합니다...`", inline=False)
    embd_ol.add_field(name="*...차려*", value="`긴장하며 오와 열을 맞춥니다...`", inline=False)
    embd_ol.add_field(name="*...팔벌려뛰기*", value="`입력받은 횟수까지 팔벌려뛰기를 합니다. 마지막 구호를 외칠 시 재수행 합니다...`", inline=False)
    embd_ol.add_field(name="*...업뎃*", value="`봇을 잠시 중지하고 업데이트 합니다...(구현중)`", inline=False)
    embd_ol.add_field(name="*...일정*", value="`구글캘린더에 저장된 오늘의 일정을 메시지로 출력합니다...(구현중)`", inline=False)
    embd_ol.add_field(name="*...주가*", value="`현재 주가 지수를 메시지로 출력합니다...`", inline=False)
    embd_ol.add_field(name="*...날씨*", value="`날씨정보를 네이버 검색 기준으로 메시지를 출력합니다. 명령어 뒤에 한칸 띄고 지역명을 입력하세요...`", inline=False)
    await ctx.send(embed=embd_ol)


@client.command(name="안녕")
async def hello(ctx):
    await ctx.send("형님. 잘 지내셨어요?...")


@client.command(name="쉬어")
async def relax(ctx):
    await ctx.send("감사합니다. 형님...")


@client.command(name="ㅈ같냐?")
async def ruAnnoy(ctx):
    embed_anoy = discord.Embed(title="", description="하...", color=0x62c1cc)
    embed_anoy.set_image(url="https://i.imgur.com/kT3fZtJ.png")

    await ctx.send(embed=embed_anoy)


@client.command(name="차려")
async def Charyut(ctx):
    await ctx.send("차렷!...")


@client.command(name="팔벌려뛰기")
async def wide_arm_jump(ctx, count):
    count_int = int(count)
    bIs_dude = random.randint(0, 1)
    for i in range(count_int - 1 + bIs_dude):
        await ctx.send(f"{i+1}!")
        await asyncio.sleep(1.0)
    if bIs_dude == 1:
        await ctx.send("정신을 못차렸는지 마지막 구호를 외쳤습니다;; 처음부터 다시!!...")
        await asyncio.sleep(1.0)
        await wide_arm_jump(ctx, count)
    else:
        await ctx.send(f"흡..(속으로 {count_int}!)!!!...")
        await asyncio.sleep(0.5)
        await ctx.send("팔벌려뛰기 완료!!!...")
    # sleep(10.0)


@client.command(name="업뎃")
async def update(ctx):
    await ctx.send("업데이트를 시작합니다. 5초 뒤에 봇이 종료되고 10초 뒤에 재시작합니다...")
    await asyncio.sleep(15.0)
    await ctx.send("재시작이 완료되었습니다...(구현중)")
    pass


@client.command(name="일정")
async def schedule(ctx):
    await ctx.send("오늘 일정은 아래와 같습니다...(구현중)")
    pass


@client.command(name="주가")
async def stock_index(ctx):
    basic_url = "https://finance.naver.com/sise/"
    fp = urllib.request.urlopen(basic_url)
    source = fp.read()
    fp.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("span", class_="num")
    kospi_value = soup[0].string
    kosdaq_value = soup[1].string
    # await ctx.send(f"현재 KOSPI는 {kospi_value} 이고,\n현재 KOSDAQ은 {kosdaq_value}입니다...")
    embd_si = discord.Embed(title="**주가 지수...**", description="현재의 주가 지수를 출력합니다...", color=0x62c1cc)
    embd_si.add_field(name="KOSPI", value=f"`{kospi_value}`", inline=True)
    embd_si.add_field(name="KOSDAQ", value=f"`{kosdaq_value}`", inline=True)
    await ctx.send(embed=embd_si)
    pass


@client.command(name="날씨")
async def weather(ctx, input):
    defaultUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
    plusUrl = str(input) + '날씨'
    basic_url = str(defaultUrl) + str(quote_plus(plusUrl))
    fp = urllib.request.urlopen(str(basic_url))
    source = fp.read()
    fp.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup_tmp = soup.findAll("span", class_="todaytemp")
    soup_num = soup.findAll("span", class_="num")
    # soup_uv = soup.findAll("span",class_="indicator")
    soup_rain = soup.findAll("span", class_="rainfall")
    # soup_forDust = soup.findAll("dd",class_="lv1")
    # soup_forMdust = soup.findAll("dd",class_="lv1")
    soup_detail = soup.findAll("div", class_="detail_box")
    crnt_temp = soup_tmp[0].string
    crnt_sensible = soup_num[2].string

    if len(soup.findAll("span", class_="rainfall")) == 0:
        crnt_rain = "None"
    else:
        soup_rain = soup.findAll("span", class_="rainfall")
        crnt_rain = soup_rain[0].text

    if len(soup.findAll("span", class_="indicator")) == 0:
        crnt_uv = "None"
    else:
        soup_uv = soup.findAll("span", class_="indicator")
        crnt_uv = soup_uv[0].text

    crnt_detail = soup_detail[0].text
    crnt_detail_str = crnt_detail.split(" ")
    detail_1 = crnt_detail_str[2] + " " + crnt_detail_str[3]
    detail_2 = crnt_detail_str[4] + " " + crnt_detail_str[5]
    detail_3 = crnt_detail_str[6] + " " + crnt_detail_str[7]
    embd_wtr = discord.Embed(title=f"**현재 {input}의 날씨는...**", description="해당 지역의 현재 날씨 정보를 출력합니다...", color=0x62c1cc)
    embd_wtr.add_field(name="**현재 기온**", value=f"`{crnt_temp} ℃`", inline=True)
    embd_wtr.add_field(name="**체감 온도**", value=f"`{crnt_sensible} ℃`", inline=True)
    embd_wtr.add_field(name="**강수 현황**", value=f"`{crnt_rain}`", inline=False)
    embd_wtr.add_field(name="**자외선 현황**", value=f"`{crnt_uv}`", inline=True)
    embd_wtr.add_field(name="**부가정보**", value=f"`{detail_1}`\n`{detail_2}`\n`{detail_3}`", inline=False)
    await ctx.send(embed=embd_wtr)

if __name__ == "__main__":
    client.run(sys.argv[1])

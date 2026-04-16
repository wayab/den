import discord
from discord.ext import commands
import requests

# --- AYARLAR ---
TOKEN = 'MTQ3NzYyNzk0MzEyNjU2NDkzNg.GPg-4M.etQksI2Lb2z4MZeeCSdkGM_AVesPrSXk7kth-s'
HEDEF_SUNUCU_ID = 1459257626817990802
HEDEF_KANAL_ID = 1482379115653763265
# GitHub RAW Linki (Doğrudan metni okumak için bu link kullanılır)
GITHUB_URL = "https://raw.githubusercontent.com/wayab/den/main/dogru.txt"
# ---------------

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'------------------------------------')
    print(f'BOT AKTİF: {bot.user.name}')
    print(f'VERİ KAYNAĞI:  (dogru.txt)')
    print(f'------------------------------------')

@bot.command(name="craftrise")
async def craftrise(ctx):
    # Sunucu ve Kanal Kontrolü
    if ctx.guild.id != HEDEF_SUNUCU_ID or ctx.channel.id != HEDEF_KANAL_ID:
        return

    try:
        # GitHub'dan veriyi çekiyoruz
        response = requests.get(GITHUB_URL)

        if response.status_code == 200:
            # Metni satırlara bölüyoruz
            satirlar = response.text.strip().split('\n')

            if not satirlar or satirlar[0] == "":
                await ctx.send("❌ GitHub dosyasında hesap bulunamadı!")
                return

            # NOT: GitHub dosyasından silme işlemi yapılamaz (Sadece okuma)
            # Bu yüzden rastgele bir hesap seçelim veya ilkini verelim
            import random
            hesap = random.choice(satirlar).strip()

            # Kullanıcıya DM Gönder
            embed = discord.Embed(
                title="🎮 VAYONUR PROJECT - GitHub Teslimatı",
                description=f"**Hesap Bilgilerin:**\n```\n{hesap}\n```",
                color=0x00ff00
            )
            embed.set_footer(text="VayOnur Project İyi Oyunlar Diler")

            await ctx.author.send(embed=embed)
            await ctx.send(f"✅ {ctx.author.mention} Hesabın DM kutuna gönderildi!")

        else:
            await ctx.send(f"❌ GitHub dosyasına ulaşılamadı! (Hata Kodu: {response.status_code})")

    except discord.Forbidden:
        await ctx.send(f"❌ {ctx.author.mention} DM kutun kapalı! Hesabı gönderemedim.")
    except Exception as e:
        await ctx.send(f"⚠️ Bir hata oluştu: {e}")

bot.run(TOKEN)

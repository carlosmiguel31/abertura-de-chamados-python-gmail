import os
from dotenv import load_dotenv
import discord
from discord import app_commands, SelectOption, TextStyle
from discord.ext import commands
from discord.ui import Select, View, Modal, TextInput
import aiohttp

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

GUILD_ID = 758638309164711956

N8N_WEBHOOK = "https://n8n-prd.aws-useast-01.une.vc/webhook/demanda"

async def send_to_n8n(payload: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(N8N_WEBHOOK, json=payload) as resp:
            if resp.status == 200:
                try: 
                    data = await resp.json()
                    print("Debug Webhook:", data)
                    protocol = data.get("Protocolo")
                    return protocol.strip() if protocol else None
                except Exception as e:
                    print(f"Erro JSON: {e}")
            else:
                text = await resp.text()
                print("Erro ao enviar para n8n:", resp.status)
                print("Resposta:", text)
    return None

class TicketModal(Modal):
    def __init__(self):
        super().__init__(title="Abertura de Chamados ao Setor de TI")

        self.nome = TextInput(label='Colaborador', placeholder='Digite seu nome completo')
        self.setor = TextInput(label='Setor', placeholder='Digite seu setor de trabalho')
        self.assunto = TextInput(label='Titulo da Demanda', placeholder='Digite o titulo da demanda', style=TextStyle.short)
        self.demanda = TextInput(label='Descrição da Demanda', placeholder='Descreva sua demanda com detalhes', style=TextStyle.long)

        self.add_item(self.nome)
        self.add_item(self.setor)
        self.add_item(self.assunto)
        self.add_item(self.demanda)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        payload = {
            "name": self.nome.value,
            "setor": self.setor.value,
            "assunto": self.assunto.value,
            "demanda": self.demanda.value,
            "usuario_discord": str(interaction.user),
            "discord_id": str(interaction.user.id),
        }

        Protocolo = await send_to_n8n(payload)

        embed = discord.Embed(
            title="✅ Ticket criado com sucesso",
            description="Seu chamado foi registrado no setor de TI.",
            color=0x2ecc71  # verde
        )

        embed.add_field(
            name="📄 Protocolo",
            value=f"`{Protocolo}`",
            inline=False
        )

        embed.add_field(
            name="📬 Acompanhe por e-mail",
            value="Todas as atualizações do chamado serão enviadas para seu e-mail corporativo.",
            inline=False
        )

        embed.set_footer(text="Equipe de Tecnologia da Informação")

        await interaction.followup.send(embed=embed)


@bot.tree.command(name="abertura_chamado", description="Abertura de Chamados ao Setor de TI")
@app_commands.guilds(discord.Object(id=GUILD_ID))
async def abertura_chamado(interaction: discord.Interaction):
    await interaction.response.send_modal(TicketModal())

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Comandos sincronziados: {len(synced)}")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")

bot.run(os.getenv("DISCORD_TOKEN"))

import customtkinter as ctk
import threading
from modules import main
from PIL import Image


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------- Janela ----------
janela = ctk.CTk()
janela.title("Assistente Saturno")
janela.geometry("600x400")

# ---------- Funções ----------
status = ctk.StringVar(value="Status: Pronto")
fala_usuario = ctk.StringVar(value=" ")
resposta_assistente = ctk.StringVar(value=" ")

assistente_rodando = False

def atualizar_status(texto):
    status.set(f"Status: {texto}")

def atualizar_fala_usuario(fala):
    if fala:
        fala_usuario.set(f"Você: {fala}")
        frame_usuario.pack(pady=5, anchor="w")
    else:
        fala_usuario.set("")
        frame_usuario.pack_forget()

def atualizar_resposta(resposta):
    if resposta:
        resposta_assistente.set(f"Saturno: {resposta}")
        frame_assistente.pack(pady=5, anchor="w")
    else:
        resposta_assistente.set("")
        frame_assistente.pack_forget()

def verificar_rodando():
    return assistente_rodando

def rodar_assistente():
    atualizar_status("Ouvindo...")
    main.iniciar_assistente(
        atualizar_status, atualizar_fala_usuario, atualizar_resposta, verificar_rodando
    )
    atualizar_status("Pronto")

def iniciar_assistente():
    global assistente_rodando
    if not assistente_rodando:
        assistente_rodando = True
        thread = threading.Thread(target=rodar_assistente, daemon=True)
        thread.start()


def pausar_assistente():
    global assistente_rodando
    assistente_rodando = False
    atualizar_status("Pausado")

def sair():
    janela.destroy()

# ---------- Layout ----------
# -- Status
label_status = ctk.CTkLabel(janela, textvariable=status, font=("Arial", 16))
label_status.pack(pady=10, anchor="n")

# -- Frame dos diálogos
frame_dialogos = ctk.CTkFrame(janela, fg_color="transparent")
frame_dialogos.pack(pady=10, expand=True)

# -- Frame do usuário
frame_usuario = ctk.CTkFrame(frame_dialogos, fg_color="transparent")

user_imagem = ctk.CTkImage(
    light_image=Image.open("image/perfil.png"),
    size=(20, 20)
)

label_imagem_usuario = ctk.CTkLabel(frame_usuario, image=user_imagem, text="")
label_imagem_usuario.pack(side="left", padx=5)

label_usuario = ctk.CTkLabel(
    frame_usuario, textvariable=fala_usuario, font=("Arial", 14),
    wraplength=450, justify="left"
)
label_usuario.pack(side="left")


# -- Frame do assistente
frame_assistente = ctk.CTkFrame(frame_dialogos, fg_color="transparent")

saturno_imagem = ctk.CTkImage(
    light_image=Image.open("image/saturno.png"),
    size=(20, 20)
)

label_imagem_assistente = ctk.CTkLabel(frame_assistente, image=saturno_imagem, text="")
label_imagem_assistente.pack(side="left", padx=5)

label_assistente = ctk.CTkLabel(
    frame_assistente, textvariable=resposta_assistente, font=("Arial", 14),
    wraplength=450, justify="left"
)
label_assistente.pack(side="left")


# botões
frame_botoes = ctk.CTkFrame(janela, fg_color="transparent")
frame_botoes.pack(pady=10, side="bottom")

btn_iniciar = ctk.CTkButton(frame_botoes, text="Ativar Saturno", command=iniciar_assistente)
btn_iniciar.pack(pady=5)

btn_pausar = ctk.CTkButton(frame_botoes, text="Pausar Saturno", command=pausar_assistente)
btn_pausar.pack(pady=5)

btn_sair = ctk.CTkButton(frame_botoes, text="Sair", command=sair)
btn_sair.pack(pady=5)

janela.mainloop()

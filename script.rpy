# The script of the game goes in this file.

# GAME VARIABLES

init:
    default persistent.cherryclearA = False
    default persistent.citrusclearA = False
    default persistent.blueberryclearA = False
    $ cherry_points = 0
    $ citrus_points = 0
    $ blueberry_points = 0
    $ cherry_alcohol = 0
    $ citrus_alcohol = 0
    $ blueberry_alcohol = 0
    $ clearpoints = 0
    $ challenge = "Normal"
    $ alcohol = 0
    $ gender = "Male"
    $ player_name = "Querido"
    $ player_tits = False
    $ player_genital = True
    $ pronomes = ""

init python:
    if not persistent._volume_initialized:
        renpy.music.set_volume(0.5, channel='music')
        renpy.music.set_volume(0.5, channel='sound')
        renpy.music.set_volume(0.5, channel='voice')
        persistent._volume_initialized = True

# Bleeps
init python:
    def bleep_date(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.music.play("audio/BLEEPS/bleep_date.ogg", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps", fadeout=0.25)

init python:
    def bleep_cherry(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.music.play("audio/BLEEPS/bleep_cherry.ogg", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps", fadeout=0.25)

init python:
    def bleep_citrus(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.music.play("audio/BLEEPS/bleep_citrus.ogg", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps", fadeout=0.25)

init python:
    def bleep_blueberry(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.music.play("audio/BLEEPS/bleep_blueberry.ogg", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps", fadeout=0.25)

init python:
    def bleep_apple(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.music.play("audio/BLEEPS/bleep_apple.ogg", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps", fadeout=0.25)

init python:
    def bleep_rando(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.music.play("audio/BLEEPS/bleep_rando.ogg", channel="bleeps", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="bleeps", fadeout=0.25)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character('[player_name]', color="#fcc200", callback=bleep_date)
define A = Character('Apple', color="#e2062c", callback=bleep_apple)
define XMC = Character('MC', color="#36454f", callback=bleep_date)
define NAR = Character('Narrador', color="#88cbf8", callback=bleep_date)
define CH = Character('Cherry', color="#de3163", callback=bleep_cherry, image="cherry")
define XCH = Character('???', color="#de3163", callback=bleep_cherry,image="cherry")
define CI = Character('Citrus', color="#46cb18", callback=bleep_citrus,image="citrus")
define XCI = Character('???', color="#46cb18", callback=bleep_citrus, image="citrus")
define BB = Character('Blueberry', color="#5C53F7", callback=bleep_blueberry, image="blueberry")
define CBB = Character('Citrus&Blueberry', color="#5C53F7", callback=bleep_blueberry)
define XBB = Character('???', color="#5C53F7", callback=bleep_blueberry, image="blueberry")
define Bouncer = Character('Bouncer', color="#36454f", callback=bleep_rando)
define Student = Character('Student', color="#36454f", callback=bleep_rando)

#CUSTOM TRANSITIONS

# Transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define flashu = Fade(0.1, 0.0, 0.2, color="#fff")
define flashO = Fade(0.1, 5.0, 0.5, color="#fff")
define flashi = Fade(0.1, 1.0, 0.5, color="#fff")
define kiss = Fade(0.1, 5.0, 1.5, color="#FF56AF")
define kisso = Fade(0.1, 2.5, 1.5, color="#FF56AF")

define Reveal = Dissolve(2.0, alpha=False, time_warp=None)
define Reveal1 = Dissolve(1.5, alpha=False, time_warp=None)
define Reveal2 = Dissolve(5.0, alpha=False, time_warp=None)
define Plap1 = Dissolve(0.30, alpha=False, time_warp=None)
define Plap2 = Dissolve(0.35, alpha=False, time_warp=None)
define Plap3 = Dissolve(0.20, alpha=False, time_warp=None)
define Plap4 = Dissolve(0.25, alpha=False, time_warp=None)
define Plap5 = Dissolve(0.05, alpha=False, time_warp=None)
define Plap6 = Dissolve(0.10, alpha=False, time_warp=None)

#EXTRA AUDIO CHANNELS

init python:
    renpy.music.register_channel("LoNoise", "sfx",)

init python:
    renpy.music.register_channel("LoNoise2", "sfx",)

init python:
    renpy.music.register_channel("LoNoise3", "sfx",)

init python:
    renpy.music.register_channel("sound2", "sfx", loop=False)

init python:
    renpy.music.register_channel("sound3", "sfx", loop=False)

init python:
    renpy.music.register_channel("bleeps", "sfx", loop=False)

# BACKGROUNDS

image Black = "images/BGs/Black.jpg"
image White = "images/BGs/White.jpg"
image SplashA = "images/BGs/Splash A.jpg"
image SplashB = "images/BGs/Splash B.jpg"

image quartoCitrus = "images/BGs/quarto.jpg"
image mesaBebidas = "images/BGs/mesa_bebidas.jpg"
image mesaComidas = "images/BGs/mesa_comidas.jpg"
image sala = "images/BGs/sala.jpg"
image sexshop = "images/BGs/fundo_sexshop0.jpg"
image shop1 = "images/BGs/sexPart1.png"
image shop2 = "images/BGs/sexPart2.png"
image shop3 = "images/BGs/sexPart3.png"

image BB_sombra = "images/CHs/BB_sombra.png"
image CH_sombra = "images/CHs/CH_sombra.png"
image CI_sombra = "images/CHs/CI_sombra.png"

image Pessoas = "images/BGs/fundo_crowd.png"
image continua = "images/BGs/CONTINUA.png"

transform semi_transparente:
    alpha 0.8

transform fly_in_and_shake(x_target, y_target):
    xpos 1.2 ypos y_target  
    linear 0.8 xpos x_target  
    pause 0.1
    xoffset 5
    pause 0.03
    xoffset -5
    pause 0.03
    xoffset 5
    pause 0.03
    xoffset -5
    pause 0.03
    xoffset 5
    pause 0.03
    xoffset -5
    pause 0.03
    xoffset 5
    pause 0.03
    xoffset -5
    pause 0.03
    xoffset 5
    pause 0.03
    xoffset -5
    pause 0.03
    xoffset 5
    pause 0.03
    xoffset -5
    pause 0.03
    xoffset 0

##Composite Title Screen
image TitleBase = "gui/Title Screen/Title Base A.jpg"
image TitleBaseTitle = "gui/Title Screen/Title Base A.jpg"
image TitleChBlush = ConditionSwitch(
    "persistent.cherryclearA == False", "gui/Title Screen/Blank.png",
    "persistent.cherryclearA == True", "gui/Title Screen/Blush Cherry.png")
image TitleCiBlush = ConditionSwitch(
    "persistent.citrusclearA == False", "gui/Title Screen/Blank.png",
    "persistent.citrusclearA == True", "gui/Title Screen/Blush Citrus.png")
image TitleBBBlush = ConditionSwitch(
    "persistent.blueberryclearA == False", "gui/Title Screen/Blank.png",
    "persistent.blueberryclearA == True", "gui/Title Screen/Blush BlueBerry.png")

layeredimage JUICYTITLE:

    always:
        "TitleBase"

    group CherryClear:
        attribute CHB default:
            "TitleChBlush"

    group CitrusClear:
        attribute CIB default:
            "TitleCiBlush"

    group BlueBerryClear:
        attribute BBB default:
            "TitleBBBlush"

# CG IMAGES

image Invite = "images/CGs/Invite.jpg"
image BigReveal = "images/CGs/Unveal.jpg"

# ITEM IMAGES

image CherryInvite = "images/CGs/ITEMS/Cherry's Invite.png"


# CHARACTER IMAGES

#APPLE BUBBLE

image AppleBubbleA = "images/CHs/APPLE BUBBLE/BubbleA.png"
image AppleBubbleB = "images/CHs/APPLE BUBBLE/BubbleB.png"
image AppleBubble:
    "AppleBubbleA"
    pause 1.0
    "AppleBubbleB"
    pause 1.0
    repeat
image AppleBase = "images/CHs/APPLE BUBBLE/Base.png"
image AppleSmile = "images/CHs/APPLE BUBBLE/Smile.png"
image AppleLaugh = "images/CHs/APPLE BUBBLE/Laugh.png"
image AppleAngry = "images/CHs/APPLE BUBBLE/Angry.png"
image AppleAnnoy = "images/CHs/APPLE BUBBLE/Annoy.png"

layeredimage Apple:

    group bubble:
        attribute 01 default:
            "AppleBubble"

    group face:
        attribute 02 default:
            "AppleBase"

    group facial:
        attribute Smile:
            "AppleSmile"
        attribute Laugh:
            "AppleLaugh"
        attribute Angry:
            "AppleAngry"
        attribute Annoy:
            "AppleAnnoy"


#CHERRY

image CH0a = "images/CHs/CHERRY/0A.png"
image CH1a = "images/CHs/CHERRY/1A.png"
image CH1b = "images/CHs/CHERRY/1B.png"
image CH2a = "images/CHs/CHERRY/2A.png"
image CH3a = "images/CHs/CHERRY/3A.png"
image CH3b = "images/CHs/CHERRY/3B.png"
image CH4Angry = "images/CHs/CHERRY/4Angry.png"
image CH4Laugh = "images/CHs/CHERRY/4Laugh.png"
image CH4Mischief = "images/CHs/CHERRY/4Mischief.png"
image CH4Mou = "images/CHs/CHERRY/4Mou.png"
image CH4Normal = "images/CHs/CHERRY/4Normal.png"
image CH4Sad = "images/CHs/CHERRY/4Sad.png"
image CH4Shy = "images/CHs/CHERRY/4Shy.png"
image CH4Smile = "images/CHs/CHERRY/4Smile.png"
image CH4Surprise = "images/CHs/CHERRY/4Surprise.png"
image CH4Think = "images/CHs/CHERRY/4Think.png"
image CH5a = "images/CHs/CHERRY/5A.png"
image CH6a = "images/CHs/CHERRY/6A.png"
image CH6b = "images/CHs/CHERRY/6B.png"
image CH7a = "images/CHs/CHERRY/7A.png"
image CHLD = "images/CHs/CHERRY/LD.png"
image CHLU = "images/CHs/CHERRY/LU.png"
image CHRD = "images/CHs/CHERRY/RD.png"
image CHRU = "images/CHs/CHERRY/RU.png"
image CH8a = "images/CHs/CHERRY/8A.png"
image CH8b = "images/CHs/CHERRY/8B.png"
image CH9a = "images/CHs/CHERRY/9A.png"
image CH9b = "images/CHs/CHERRY/9B.png"
image CH9c = "images/CHs/CHERRY/9C.png"
image CH9d = "images/CHs/CHERRY/9D.png"
image CH9e = "images/CHs/CHERRY/9E.png"

layeredimage CH:

    group hair:
        attribute 0A default:
            "CH0a"

    group body:
        attribute 1A default:
            "CH1a"
        attribute 1B:
            "CH1b"

    group lingerie:
        attribute 2A default:
            "CH2a"
        attribute 2N:
            Null()

    group behindarms:
        attribute 8A:
            "CH8a"
        attribute 8B:
            "CH8b"
        attribute 8N:
            Null()

    group dress:
        attribute 3A default:
            "CH3a"
        attribute 3B:
            "CH3b"
        attribute 3N:
            Null()

    group blushing:
        attribute 6A:
            "CH6a"
        attribute 6B:
            "CH6b"
        attribute 6N:
            Null()

    group face:
        attribute 4Normal default:
            "CH4Normal"
        attribute 4Angry:
            "CH4Angry"
        attribute 4Laugh:
            "CH4Laugh"
        attribute 4Mischief:
            "CH4Mischief"
        attribute 4Mou:
            "CH4Mou"
        attribute 4Sad:
            "CH4Sad"
        attribute 4Shy:
            "CH4Shy"
        attribute 4Smile:
            "CH4Smile"
        attribute 4Surprise:
            "CH4Surprise"

    group bangs:
        attribute 7A default:
            "CH7a"

    group frontarms:
        attribute 9A default:
            "CH9a"
        attribute 9B:
            "CH9b"
        attribute 9C:
            "CH9c"
        attribute 9N:
            Null()

#CITRUS

image CI0a = "images/CHs/CITRUS/0A.png"
image CI1a = "images/CHs/CITRUS/1A.png"
image CI2a = "images/CHs/CITRUS/2A.png"
image CI3a = "images/CHs/CITRUS/3A.png"
image CI4Angry = "images/CHs/CITRUS/4Angry.png"
image CI4Laugh = "images/CHs/CITRUS/4Laugh.png"
image CI4Mischief = "images/CHs/CITRUS/4Mischief.png"
image CI4Mou = "images/CHs/CITRUS/4Mou.png"
image CI4Normal = "images/CHs/CITRUS/4Normal.png"
image CI4Sad = "images/CHs/CITRUS/4Sad.png"
image CI4Smile = "images/CHs/CITRUS/4Smile.png"
image CI4Surprise = "images/CHs/CITRUS/4Surprise.png"
image CI6a = "images/CHs/CITRUS/6A.png"
image CI7a = "images/CHs/CITRUS/7A.png"
image CILD = "images/CHs/CITRUS/LD.png"
image CILU = "images/CHs/CITRUS/LU.png"
image CI8a = "images/CHs/CITRUS/8A.png"
image CI8b = "images/CHs/CITRUS/8B.png"
image CI8c = "images/CHs/CITRUS/8C.png"
image CI8d = "images/CHs/CITRUS/8D.png"
image CI8e = "images/CHs/CITRUS/8E.png"
image CI8f = "images/CHs/CITRUS/8F.png"
image CI9a = "images/CHs/CITRUS/9A.png"
image CI9b = "images/CHs/CITRUS/9B.png"

layeredimage CI:

    group hair:
        attribute 0A default:
            "CI0a"

    group body:
        attribute 1A default:
            "CI1a"

    group lingerie:
        attribute 2A default:
            "CI2a"
        attribute 2N:
            Null()

    group dress:
        attribute 3A default:
            "CI3a"
        attribute 3N:
            Null()

    group blushing:
        attribute 6A:
            "CI6a"
        attribute 6N:
            Null()

    group face:
        attribute 4Normal default:
            "CI4Normal"
        attribute 4Angry:
            "CI4Angry"
        attribute 4Laugh:
            "CI4Laugh"
        attribute 4Mischief:
            "CI4Mischief"
        attribute 4Mou:
            "CI4Mou"
        attribute 4Sad:
            "CI4Sad"
        attribute 4Smile:
            "CI4Smile"
        attribute 4Surprise:
            "CI4Surprise"

    group bangs:
        attribute 7A default:
            "CI7a"

    group leftarm:
        attribute LU:
            "CILU"
        attribute LD default:
            "CILD"

    group lefthand:
        attribute 8A:
            "CI8a"
        attribute 8B:
            "CI8b"
        attribute 8C:
            "CI8c"
        attribute 8D:
            "CI8d"
        attribute 8E:
            "CI8e"
        attribute 8F default:
            "CI8f"

    group righthand:
        attribute 9A default:
            "CI9a"
        attribute 9B:
            "CI9b"


#BLUEBERRY

image BB0a = "images/CHs/BLUEBERRY/0A.png"
image BB1a = "images/CHs/BLUEBERRY/1A.png"
image BB2a = "images/CHs/BLUEBERRY/2A.png"
image BB3a = "images/CHs/BLUEBERRY/3A.png"
image BB4Angry = "images/CHs/BLUEBERRY/4Angry.png"
image BB4Laugh = "images/CHs/BLUEBERRY/4Laugh.png"
image BB4Mischief = "images/CHs/BLUEBERRY/4Mischief.png"
image BB4Mou = "images/CHs/BLUEBERRY/4Mou.png"
image BB4Normal = "images/CHs/BLUEBERRY/4Normal.png"
image BB4Sad = "images/CHs/BLUEBERRY/4Sad.png"
image BB4Shy = "images/CHs/BLUEBERRY/4Shy.png"
image BB4Smile = "images/CHs/BLUEBERRY/4Smile.png"
image BB4Surprise = "images/CHs/BLUEBERRY/4Surprise.png"
image BB5a = "images/CHs/BLUEBERRY/5A.png"
image BB6a = "images/CHs/BLUEBERRY/6A.png"
image BB6b = "images/CHs/BLUEBERRY/6B.png"
image BB7a = "images/CHs/BLUEBERRY/7A.png"
image BBLD = "images/CHs/BLUEBERRY/LD.png"
image BBLU = "images/CHs/BLUEBERRY/LU.png"
image BBRD = "images/CHs/BLUEBERRY/RD.png"
image BBRU = "images/CHs/BLUEBERRY/RU.png"
image BB8a = "images/CHs/BLUEBERRY/8A.png"
image BB8b = "images/CHs/BLUEBERRY/8B.png"
image BB8c = "images/CHs/BLUEBERRY/8C.png"
image BB8d = "images/CHs/BLUEBERRY/8D.png"
image BB8e = "images/CHs/BLUEBERRY/8E.png"
image BB9a = "images/CHs/BLUEBERRY/9A.png"
image BB9b = "images/CHs/BLUEBERRY/9B.png"
image BB9c = "images/CHs/BLUEBERRY/9C.png"
image BB9d = "images/CHs/BLUEBERRY/9D.png"
image BB9e = "images/CHs/BLUEBERRY/9E.png"

layeredimage BB:

    group hair:
        attribute 0A default:
            "BB0a"

    group body:
        attribute 1A default:
            "BB1a"

    group lingerie:
        attribute 2A default:
            "BB2a"
        attribute 2N:
            Null()

    group dress:
        attribute 3A default:
            "BB3a"
        attribute 3N:
            Null()

    group blushing:
        attribute 6A:
            "BB6a"
        attribute 6B:
            "BB6b"
        attribute 6N:
            Null()

    group face:
        attribute 4Normal default:
            "BB4Normal"
        attribute 4Angry:
            "BB4Angry"
        attribute 4Laugh:
            "BB4Laugh"
        attribute 4Mischief:
            "BB4Mischief"
        attribute 4Mou:
            "BB4Mou"
        attribute 4Sad:
            "BB4Sad"
        attribute 4Shy:
            "BB4Shy"
        attribute 4Smile:
            "BB4Smile"
        attribute 4Surprise:
            "BB4Surprise"

    group glasses:
        attribute 5A default:
            "BB5a"
        attribute 5N:
            Null()

    group bangs:
        attribute 7A default:
            "BB7a"

    group leftarm:
        attribute LU default:
            "BBLU"
        attribute LD:
            "BBLD"

    group rightarm:
        attribute RU:
            "BBRU"
        attribute RD default:
            "BBRD"

    group lefthand:
        attribute 8A default:
            "BB8a"
        attribute 8B:
            "BB8b"
        attribute 8C:
            "BB8c"
        attribute 8D:
            "BB8d"
        attribute 8E:
            "BB8e"

    group righthand:
        attribute 9A:
            "BB9a"
        attribute 9B :
            "BB9b"
        attribute 9C:
            "BB9c"
        attribute 9D:
            "BB9d"
        attribute 9E default: 
            "BB9e"

# PREGAME SPLASHSCREEN

label splashscreen:
    scene black
    pause 2.0
    scene white with Reveal1
    pause 1.5
    scene SplashA with Reveal1
    pause 3.0
    scene white with dissolve
    pause 1.5
    play music "audio/BGM/Title Scene.ogg"
    pause 2.0
    scene TitleBase with Reveal2
    pause 0.5
    scene TitleBaseTitle with flash
    pause 6.0
    return

label start:
    $ quick_menu = False
    stop music fadeout 4.0
    scene black with Reveal2
    pause 3.0
    $ quick_menu = True
    NAR "Olá! Bem vindo ao Juicy Party!"
    NAR "Antes de começar,{w=0.3} eu e as meninas precisamos saber algumas coisas sobre você, ok?"
    # NAR "Nessa versão ainda usamos os pronomes ele/dele para referenciar a você jogador,{w=0.3} mas,{w=0.3} futuramente poderá selecionar o pronome de sua preferência,{w=0.3} pedimos desculpas."

    NAR "Me conte sobre você!"
    NAR "Qual seu nome?"
    pause 1.0
    call screen name_input_screen
    $ player_name = _return.strip() if _return else "Querido" 
    play sound "audio/SFX/success.wav"
    NAR "É um prazer te conhecer [player_name]!"
    NAR "Quais são os seus pronomes?"
    menu:
        "Quais são os seus pronomes?"

        "Ele/Dele":
            $ renpy.block_rollback()
            $ pronomes = "ELE"

        "Ela/Dela":
            $ renpy.block_rollback()
            $ pronomes = "ELA"
        
        "Elu/Delu":
            $ renpy.block_rollback()
            $ pronomes = "ELU"
            
    NAR "Agora,{w=0.3} me conte,{w=0.3} como é seu corpo?"
    menu:
        "Como é seu torso?"

        "Eu tenho seios!":
            $ renpy.block_rollback()
            $ player_tits = True
        
        "Tenho o torso plano!":
            $ renpy.block_rollback()
            $ player_tits = False
   
    menu:
        "Como é sua genitalia?"

        "Eu tenho pênis!":
            $ renpy.block_rollback()
            $ player_genital = True
        
        "Eu tenho vagina!":
            $ renpy.block_rollback()
            $ player_genital = False
   
    NAR "Ótimo!{w=0.3} Suas escolhas foram salvas!"
    NAR "Agora vamos dar início a essa festa!"
    scene black with Reveal2
    pause 0.5
    play music "audio/BGM/apple_inicio.ogg" fadein 2.0
    pause 0.5
    A "Vaaaaai,{w=0.3} seja sincero,{w=0.3} qual foi a última vez que você ficou com alguém?"
    MC "Humm…{w=0.3} eu não lembro, acho que a uns 8 meses…{w=0.3} não precisa jogar na cara não viu Apple???"
    show Apple Annoy at truecenter
    A "Não é jogar na cara,{w=0.3} estou tentando jogar {i}{b}você {/b}{/i} para um pouco de diversão!"
    pause 0.5
    MC ".{w=0.3}.{w=0.3}.{w=0.3}"
    MC "Mas…{w=0.3} o convite é para você,{w=0.3} não?"
    pause 0.5
    show Apple Smile
    A "Não é nominal,{w=0.3} para de procurar problemas!{w=0.3} Alem de que dúvido que a pessoa que me chamou vá se importar" 
    A "Basta entregar ao segurança e {i}voilà{/i}!"
    pause 0.5
    MC "Ok{w=0.3} ok.{w=0.3}.{w=0.3}.{w=0.3}" 
    MC"É a festa de inauguração do que mesmo?"
    show Apple Laugh
    A "Ah...{w=0.3} Sobre isso...{w=0.3}"
    pause 0.5
    stop music fadeout 2.0
    scene Black with Reveal
    A "Você nem imagina..."
    pause 3.0

    scene White with Reveal
    show shop1 at fly_in_and_shake(0.0, 0.0)
    pause 0.2
    play sound "audio/SFX/bonk.ogg"
    pause 0.5
    MC "O QUE?!?!?!"
    pause 1.5
    show shop2 at fly_in_and_shake(0.33, 0.0)
    pause 0.2
    play sound "audio/SFX/bonk.ogg"
    pause 0.5
    MC "Isso aqui é..."
    pause 1.5
    show shop3 at fly_in_and_shake(0.7, 0.0)
    pause 0.2
    play sound "audio/SFX/bonk.ogg"
    pause 0.5
    MC "UM SEX SHOP!?{w=0.3} EU VOU MATAR A APPLE!"
    pause 1.5
    scene sexshop
    play music "audio/BGM/eletronico.ogg" fadein 1.5 volume 1.0
    "Salão do Sex Shop {i}{b}Citrus Dreams{/i}{/b}"
    pause 2.0
    show Pessoas at semi_transparente with Reveal
    pause 1.5
    MC "Eu tô na festa de inauguração de um {i}sex shop{/i} na avenida principal… {b}Citrus Dreams.{/b}"
    MC "O que a Apple tava pensando me jogando aqui?{w=0.3}" 
    MC "Não conheço ninguém.."
    MC "Festa estranha... {w=0.3} com gente esquisita..."
    MC "O que eu vou fazer?..."
    NAR "Uma conversa chama sua atenção..."
    pause 0.5
    show CI_sombra with Reveal:
        xalign 0.5 yalign 1.0
    pause 0.5
    XCI black "Ah,{w=0.3} eu já podia imaginar…"
    pause 0.5
    show CH_sombra with Reveal:
        xalign 0.5 yalign 1.0
    pause 0.5
    XCH black "M-me desculpe…{w=0.3} eu conferi tudo antes de sair,{w=0.3} não sei o que aconteceu com meu convite…"
    pause 0.5
    show BB_sombra with Reveal:
        xalign 0.5 yalign 1.0
    pause 0.5
    XBB black "Você precisa tomar mais cuidado,{w=0.3} mas o importante é que conseguiu entrar."
    pause 1.0
    XCI "Mas pelo menos nossa pequena Cherry está aprendendo a usar as vantagens que tem hihihi"
    XCH "E-eu…{w=0.3} eu não queria ter tido que entrar pelos fundos…"
    pause 1.0
    MC "Acho que estou assistindo algum tipo de conversa comum de amigas,{w=0.3} mas estão bem animadas!{w=0.3}" 
    MC "Quem será que são?"
    pause 0.5
    hide CI_sombra with Reveal
    pause 0.5
    show CI LU 8A 4Smile with Reveal:
        xalign 0.95 yalign 1.0
    pause 0.5
    hide CH_sombra with Reveal
    pause 0.5
    show CH 3B 9A 6A 4Sad with Reveal:
        xalign 0.1 yalign 1.0
    pause 0.5
    hide BB_sombra with Reveal
    pause 0.5
    show BB LD 8E RD 9D 4Smile with Reveal:
        xalign 0.5 yalign 1.0
    pause 0.5
    show CI LD 8F 4Surprise
    pause 0.5
    XCI normal "Ah, Oi!{w=0.3}" 
    pause 0.5
    show CI 4Normal
    show BB 4Normal
    show CH 4Normal
    XCI "Você deve ter acabado de chegar"
    show BB LU 8A 9E 4Mischief
    show CH 6N 4Surprise
    pause 1.0
    show CI 8E
    CI normal "eu sou Citrus,{w=0.3} dona da loja e organizadora,{w=0.3} espero que goste da festa!{w=0.3} Qual seu nome?"
    MC "Essa não!{w=0.3} Fui pego!"
    pause 1.0
    show CI LU 8A 4Mischief:
        xalign 0.95 yalign 1.0
    show CH 3A 9N 8A 4Smile:
        xalign 0.1 yalign 1.0
    show BB LD 8E RD 9E 4Normal:
        xalign 0.5 yalign 1.0
    pause 2.0
    MC "Boa noite! Eu sou [player_name],{w=0.3} prazer em conhecer vocês!"
    pause 0.5
    MC "Eu fiquei sabendo da loja hoje,{w=0.3} mas não esperava…"
    pause 1.5
    menu:

        "O que é mais surpreendente?"

        "Que seria uma mulher como propriataria...":
            $ renpy.block_rollback()
            show CI 4Surprise 8F LD 9B
            show CH 4Angry 9B 8N 3B
            show BB 4Mou LU 8C RD 9D
            MC "Ahn, desculpe mas…{w=0.3} não esperava uma mulher como dona de um sex shop…"
            show CI 4Angry
            show BB 4Angry
            CI " Acredite,{w=0.3} nenhum homem saberia vender e atender bem nesse ramo como eu,{w=0.3} ainda mais com esse pensamento."
            XBB sombra "Bom,{w=0.3} meninas, vamos pegar algumas bebidas?{w=0.3} Aproveite a festa [player_name]!"
            XCH sombra "Vamos! Boa Noite!"
            CI "Aproveite a festa"
            scene Black with flash
            NAR "Você perdeu a chance de se aproximar de pessoas legais!"
            play sound "audio/SFX/game_over.wav"
            "Fim de Jogo!"
            return

        "Que Citrus é seu nome...":
            $ cherry_points += 2
            $ citrus_points += 2
            $ blueberry_points += 2
            $ renpy.block_rollback()
            MC "Que Citrus fosse seu nome...{w=0.3} sabe, o próprio nome na loja?"
            pause 0.5
            show CI LU 8B 4Laugh
            show BB 4Smile
            show CH 4Surprise
            XCH sombra "Eu disse a ela!"
            XBB sombra "Eu dei várias sugestões criativas! rsss"
            show CI LU 8D 4Laugh
            show BB 4Laugh
            show CH 4Smile
            CI "Você é minha artista favorita BB,{w=0.3}  mas eu não colocaria o nome de {i}Doces & Travessuras{/i}"
            CI "Eu queria algo discreto ok?"
            MC "E colocou logo seu nome?"
            show CI LD 8E 4Mischief
            show CH 4Laugh
            show BB 4Laugh
            $ citrus_points += 4
            CI "Assim vão lembrar de mim em seus momentos de prazer, gosto disso!"
            jump Presentations

        "Uma pessoa tão nova":
            $ renpy.block_rollback()
            show CI LD 8E 4Mischief
            CI "Uma mulher?"
            show CH 4Mischief
            show BB 4Mischief
            MC "Anh?{w=0.3}  Ah não não,{w=0.3}  na verdade eu não esperava alguém tão nova!"
            show CI 8F 4Surprise
            show BB 4Normal
            show CH 4Surprise
            MC "Você deve estar próxima da minha idade,{w=0.3}  é realmente incrível!"
            $ cherry_points += 2
            $ citrus_points += 2
            $ blueberry_points += 2
            pause 1.0
            show CI LU 8A 4Smile
            show BB 4Smile
            show CH 4Normal
            CI "Olha, ele pensa rápido rsss"
            XBB sombra "Citrus é ótima com negócios!{w=0.3}  Tudo que ela coloca a mão parece dar certo!"
            XCH sombra "O dono da última empresa que ela trabalhou quase chorou quando ela pediu para sair e abrir a própria loja."
            pause 0.5
            show CI 8D 4Normal
            CI "Ainda há muito o que fazer para que a loja realmente seja um sucesso,{w=0.3} estamos apenas começando!"
            MC "Para mim parece um ótimo começo!"
            jump Presentations
    return

label Presentations:
    show CI LU 8A 4Mischief:
        xalign 0.95 yalign 1.0
    show CH 3B 9N 8A 4Smile:
        xalign 0.1 yalign 1.0
    show BB LD 8E RD 9E 4Normal:
        xalign 0.5 yalign 1.0
    CI normal "Ah!{w=0.3} Deixa eu te apresentar,{w=0.3} essas são minhas amigas"
    CI "Essa é Blueberry…"
    show BB LU 8B RD 9E 4Smile
    BB normal "Ooiiiieee! Um prazer te conhecer! <3"
    CI "…E essa é a Cherry!"
    show BB LD 8D 4Normal
    show CH 3A 9A 6A 8N 4Smile
    CH normal "Oie oie!"
    show CH 6N
    show CI 4Surprise
    CI "Eu...{w=0.3} não conheço você,{w=0.3} como conseguiu o convite?"
    show BB 4Surprise
    show CH 4Surprise
    MC "Ah, sobre isso…{w=0.3} o convite era de uma pessoa que tenho amizade,{w=0.3} Apple,{w=0.3} disse que eu precisava conhecer pessoas novas…"
    show CI 4Smile
    show BB 4Smile
    show CH 4Smile
    MC "Então criei coragem e vim!{w=0.3} Mas não sabia o que era a loja até chegar aqui para ser bem sincero."
    show CH 4Surprise
    CH "Nossa sua amiga é má!"
    show BB 4Laugh
    BB "Bom,{w=0.3} não pode dizer que não deu certo rsss"
    CI "Apple…{w=0.3} Acho que me lembro, comprou algumas coisas interessantes…"
    if citrus_points >= 5:
        CI "Mas ela não me falou que tinha um amigo bonitinho assim…"
    show CH 4Smile
    show BB 4Smile
    CI "Está ótimo aqui,{w=0.3} mas preciso conferir algumas coisas"
    CI "Que tal conhecer alguns itens [player_name]?{w=0.3} Aposto que algum vai te interessar."
    show CH 4Surprise 6A
    CH "E-eu acho que prefiro ir pegar algumas bebidas…{w=0.3} você…{w=0.3} prefere vir junto comigo [player_name]?"
    BB "Hhmm{w=0.3} Já vi que a noite vai ser longa,{w=0.3} vocês vão precisar comer alguma coisa,{w=0.3} vou na cozinha pegar alguns petiscos para a gente,{w=0.3} quer me ajudar [player_name]??"
    menu:

        "Quem vou acompanhar primeiro?"

        "Ir com Citrus":
            jump CaminhoCitrus
        "Ir com Cherry":
            jump CaminhoCherry
        "Ir com Blueberry":
            jump CaminhoBlueberry

    return

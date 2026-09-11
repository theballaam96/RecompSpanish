from pathlib import Path
import json
from enum import IntEnum

json_files = list(Path("./jsonstorage").glob("*.json"))

class Icons(IntEnum):
    """Icons enum."""

    WaterfallTall = 0x0
    WaterfallShort = 0x1
    Water = 0x2
    Lava = 0x3
    Sparkles = 0x4
    ExplosionPop = 0x5
    ExplosionLava = 0x6
    LeafGreen = 0x7
    ExplosionSmoke = 0x8
    ExplosionSmall = 0x9
    SolarFlare = 0xA
    Splash = 0xB
    Bubble = 0xC
    SparklePurple = 0xD
    SparkleYellow = 0xE
    SparkleGreen = 0xF
    SparklePurple_0 = 0x10
    SparkleYellow_0 = 0x11
    SparkleGreen_0 = 0x12
    ExplosionLargeSmoke = 0x13
    ExplosionPink = 0x14
    PlankBrownHorizontal = 0x15
    PlankBirchHorizontal = 0x16
    PlankBrownVertical = 0x17
    RippleStar = 0x18
    RippleCircle = 0x19
    ExplosionSmallSmoke = 0x1A
    StaticStar = 0x1B
    StaticZ = 0x1C
    FlareWhite = 0x1D
    StaticRain = 0x1E
    ExplosionMediumSmoke = 0x1F
    MelonBouncing = 0x20
    MelonRolling = 0x21
    FlareRed = 0x22
    Sparks = 0x23
    Peanut = 0x24
    FlareStar = 0x25
    PeanutShell = 0x26
    ExplosionSmall_0 = 0x27
    ExplosionLargeSmoke_0 = 0x28
    LaserBlue = 0x29
    Pineapple = 0x2A
    Fireball = 0x2B
    Orange = 0x2C
    Grape = 0x2D
    GrapeSplat = 0x2E
    SparkleTNT = 0x2F
    ExplosionFire = 0x30
    FireballSmall = 0x31
    CoinDiddy = 0x32
    CoinChunky = 0x33
    CoinLanky = 0x34
    CoinDK = 0x35
    CoinTiny = 0x36
    BananaDK = 0x37
    Film = 0x38
    OrangeBouncing = 0x39
    Crystal = 0x3A
    GB = 0x3B
    Medal = 0x3C
    BananaDiddy = 0x3D
    BananaChunky = 0x3E
    BananaLanky = 0x3F
    BananaDK_0 = 0x40
    BananaTiny = 0x41
    ExplosionKrash = 0x42
    ExplosionWhite = 0x43
    Coconut = 0x44
    CoconutShell = 0x45
    MelonSpinning = 0x46
    Tooth = 0x47
    CrateAmmo = 0x48
    CoinRace = 0x49
    BlueprintLanky = 0x4A
    Cannonball = 0x4B
    Crystal_0 = 0x4C
    Feather = 0x4D
    Guitar = 0x4E
    Bongos = 0x4F
    Sax = 0x50
    Triangle = 0x51
    Trombone = 0x52
    NoteYellowDouble = 0x53
    NoteYellowSingle = 0x54
    NoteGreenSingle = 0x55
    NotePurpleDouble = 0x56
    NoteRedDouble = 0x57
    NoteRedSingle = 0x58
    NoteWhiteDouble = 0x59
    BlueprintDiddy = 0x5A
    BlueprintChunky = 0x5B
    BlueprintDK = 0x5C
    BlueprintTiny = 0x5D
    SparkleSpinning = 0x5E
    StaticRain_0 = 0x5F
    WaterTranslucent = 0x60
    unk61 = 0x61
    ScreenBlack = 0x62
    CloudWhite = 0x63
    LaserThin = 0x64
    BubbleBlue = 0x65
    CircleWhiteFaded = 0x66
    CircleWhite = 0x67
    ParticleGreen = 0x68
    SparkleBlue = 0x69
    ExplosionWhiteSmoke = 0x6A
    Joystick = 0x6B
    FireWall = 0x6C
    StaticRainBubble = 0x6D
    ButtonA = 0x6E
    ButtonB = 0x6F
    ButtonZ = 0x70
    ButtonCD = 0x71
    ButtonCU = 0x72
    ButtonCL = 0x73
    Acid = 0x74
    ExplosionAcid = 0x75
    RaceHoop = 0x76
    AcidGoop = 0x77
    unk78 = 0x78
    BrokenBridge = 0x79
    WhitePole = 0x7A
    BridgeChip = 0x7B
    BeamRivets = 0x7C
    BunchChunky = 0x7D
    BunchDiddy = 0x7E
    BunchLanky = 0x7F
    BunchDK = 0x80
    BunchTiny = 0x81
    BalloonChunky = 0x82
    BalloonDiddy = 0x83
    BalloonDK = 0x84
    BalloonLanky = 0x85
    BalloonTiny = 0x86
    ButtonR = 0x87
    ButtonL = 0x88
    Fairy = 0x89
    BossKey = 0x8A
    Crown = 0x8B
    CoinRareware = 0x8C
    CoinNintendo = 0x8D
    NoSymbol = 0x8E
    Headphones = 0x8F
    WaterOpaque = 0x90
    ButtonStart = 0x91
    QuestionMark = 0x92
    FaceCandy = 0x93
    FaceCranky = 0x94
    FaceSnide = 0x95
    FaceFunky = 0x96
    ArrowLeft = 0x97
    SparkleWhite = 0x98
    BoulderChunkBlack = 0x99
    BoulderChunkGreen = 0x9A
    WoodChip = 0x9B
    Snowflake = 0x9C
    StaticWater = 0x9D
    SpinningLeaf = 0x9E
    FlashingWater = 0x9F
    CoinRainbow = 0xA0
    ShockwaveParticle = 0xA1
    Implosion = 0xA2
    RarewareEmployeeFace = 0xA3
    Smoke = 0xA4
    StaticSmoke = 0xA5
    BarrelBottomChunk = 0xA6
    FaceScoff = 0xA7
    BunchMulti = 0xA8
    FaceDK = 0xA9
    FaceDiddy = 0xAA
    FaceLanky = 0xAB
    FaceTiny = 0xAC
    FaceChunky = 0xAD
    FairyTick = 0xAE
    Wrinkly = 0xAF

for file in json_files:
    data = None
    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)
    print(file.name.replace(".json", ".txt").split("/")[-1])
    with open(file.name.replace(".json", ".txt").split("/")[-1], "w") as fh:
        for text_line in data:
            segment_components = []
            last_component_was_icon = False
            for segment_index, segment in enumerate(text_line):
                for key, value in segment.items():
                    if key != "text":
                        print(f"NON TEXT KEY IN FILE {file}")
                        continue
                    if isinstance(value[0], int):
                        # Icon
                        last_component_was_icon = True
                        txt = f"[icon]{Icons(value[0]).name}[/icon]"
                        if len(segment_components) == 0:
                            segment_components.append(txt)
                        else:
                            segment_components[-1] += txt
                        continue
                    if last_component_was_icon:
                        segment_components[-1] += value[0]
                        for i, v in enumerate(value):
                            if i == 0:
                                continue
                            segment_components.append(v)
                    else:
                        value[0] = "[forcednewline]" + value[0]
                        segment_components.extend(value)
                    last_component_was_icon = False
            control_characters = {
                "\x01": "wobble",
                "\x02": "pop",
                "\x03": "spin",
            }
            control_state = {
                "\x01": False,
                "\x02": False,
                "\x03": False,
            }
            fnl = "[forcednewline]"
            if segment_components[0][:len(fnl)] == fnl:
                segment_components[0] = segment_components[0][len(fnl):]
            for component_index, component in enumerate(segment_components):
                new_str = ""
                for char in component:
                    if char in list(control_characters.keys()):
                        if control_state[char]:
                            new_str += f"[/{control_characters[char]}]"
                            control_state[char] = False
                        else:
                            new_str += f"[{control_characters[char]}]"
                            control_state[char] = True
                    elif char == "~":
                        new_str += "[kong]"
                    elif char == "@":
                        new_str += "[number]"
                    else:
                        new_str += char
                segment_components[component_index] = new_str
            fh.write("[newline]".join(segment_components))
            fh.write("\n")
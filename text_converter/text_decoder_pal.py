"""Decode text file into arrays of text items."""

import os
import zlib
import json
from enum import IntEnum, auto

main_pointer_table_offset = 0x1038D0
temp_file = "decodedtext.bin"

class TableNames(IntEnum):
    """Pointer Table Enum."""

    MusicMIDI = 0
    MapGeometry = auto()
    MapWalls = auto()
    MapFloors = auto()
    ModelTwoGeometry = auto()
    ActorGeometry = auto()
    Unknown6 = auto()
    TexturesUncompressed = auto()
    Cutscenes = auto()
    Setups = auto()
    InstanceScripts = auto()
    Animations = auto()
    Text = auto()
    Unknown13 = auto()
    TexturesHUD = auto()
    Paths = auto()
    Spawners = auto()
    DKTVInputs = auto()
    Triggers = auto()
    Unknown19 = auto()
    Unknown20 = auto()
    Autowalks = auto()
    Critters = auto()
    Exits = auto()
    RaceCheckpoints = auto()
    TexturesGeometry = auto()
    UncompressedFileSizes = auto()
    Unknown27 = auto()
    Unknown28 = auto()
    Unknown29 = auto()
    Unknown30 = auto()
    Unknown31 = auto()

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

class ROMPointerFile:
    """Class to store information about a ROM Pointer table file."""

    def __init__(self, rom: BinaryIO, table_index: int, file_index: int):
        """Initialize with given data."""
        rom.seek(main_pointer_table_offset + (table_index * 4))
        table_address = main_pointer_table_offset + int.from_bytes(rom.read(4), "big")
        rom.seek(table_address + (file_index * 4))
        self.start = main_pointer_table_offset + (int.from_bytes(rom.read(4), "big") & 0x7FFFFFFF)
        self.end = main_pointer_table_offset + (int.from_bytes(rom.read(4), "big") & 0x7FFFFFFF)
        self.size = self.end - self.start
        rom.seek(self.start)
        self.compressed = int.from_bytes(rom.read(2), "big") == 0x1F8B

    def grabFile(self, rom: BinaryIO) -> bytes:
        """Grab file bytes from ROM."""
        rom.seek(self.start)
        data = rom.read(self.size)
        if self.compressed:
            data = zlib.decompress(data, (15 + 32))
        return data

LANGUAGE_COUNT = 4
def grabText(file_index: int, language_index: int) -> list:
    """Pull text from ROM with a particular file index."""
    with open("dk64_pal.z64", "rb") as fh:
        text_file = ROMPointerFile(fh, TableNames.Text, file_index)
        fh.seek(text_file.start)
        with open(temp_file, "wb") as fg:
            if text_file.compressed:
                fg.write(zlib.decompress(fh.read(text_file.size), (15 + 32)))
            else:
                fg.write(fh.read(text_file.size))

    with open(temp_file, "rb") as fh:
        fh.seek(0)
        count = int.from_bytes(fh.read(1), "big")
        text = []
        text_data = []
        text_start = (count * 0xF) + 3
        data_start = 1
        for i in range(count):
            fh.seek(data_start)
            section_1_count = int.from_bytes(fh.read(1), "big")
            section_2_count = int.from_bytes(fh.read(1), "big")
            section_3_count = int.from_bytes(fh.read(1), "big")
            print(f"[DAT{i}]", hex(data_start))
            fh.seek(data_start + 5)
            start = int.from_bytes(fh.read(2), "big")
            size = int.from_bytes(fh.read(2), "big")
            block_start = 1
            blocks = []
            for k in range(section_1_count):
                fh.seek(data_start + block_start)
                sec2ct = int.from_bytes(fh.read(1), "big")
                offset = 0
                if (sec2ct & 4) != 0:
                    # print("Adding offset")
                    offset += 4
                text_blocks = []
                if (sec2ct & 1) == 0:
                    if (sec2ct & 2) != 0:
                        fh.seek(data_start + block_start + offset + 1)
                        sec3ct = int.from_bytes(fh.read(1), "big")
                        for j in range(sec3ct):
                            _block = block_start + 2 + offset + (4 * j) - 1
                            fh.seek(data_start + _block)
                            _pos = int.from_bytes(fh.read(2), "big")
                            fh.seek(data_start + _block)
                            _dat = int.from_bytes(fh.read(4), "big")
                            text_blocks.append({"type": "sprite", "position": _pos, "data": hex(_dat), "sprite": Icons((_dat >> 8) & 0xFF)})
                        old_block_start = block_start
                        block_start += (2 + offset + (4 * sec3ct) + 4)
                else:
                    for x in range(LANGUAGE_COUNT):
                        fh.seek(data_start + block_start + offset + 1)
                        sec3ct = int.from_bytes(fh.read(1), "big")
                        print("[SEC3]", hex(data_start + block_start + offset + 1), ">", sec3ct)
                        for j in range(sec3ct):
                            _block = block_start + 2 + offset + (8 * j) - 1
                            fh.seek(data_start + _block + 3)
                            _start = int.from_bytes(fh.read(2), "big")
                            fh.seek(data_start + _block + 5)
                            _size = int.from_bytes(fh.read(2), "big")
                            print("[TXTB]", hex(data_start + _block + 3), _start, _size)
                            text_blocks.append({"type": "normal", "start": _start, "size": _size, "dump": language_index == x})
                        old_block_start = block_start
                        block_start += (8 * sec3ct) + 1
                    block_start += 5 + offset
                blocks.append({"block_start": hex(old_block_start + data_start), "section2count": sec2ct, "section3count": sec3ct, "offset": offset, "text": text_blocks})
            fh.seek(data_start)
            if old_block_start < data_start:
                info = b""
            else:
                info = fh.read(old_block_start - data_start)
            text_data.append({"arr": info, "text": blocks, "section1count": section_1_count, "section2count": section_2_count, "section3count": section_3_count, "data_start": hex(data_start)})
            text_start += old_block_start - data_start
            data_start += block_start
        for item in text_data:
            text_block = []
            # print(item)
            for item2 in item["text"]:
                # print(item2)
                temp = []
                for item3 in item2["text"]:
                    if item3["type"] == "normal":
                        start = item3["start"] + data_start + 2
                        # print(hex(start))
                        end = start + item3["size"]
                        if item3["dump"]:
                            fh.seek(start)
                            print("[READ]", hex(start))
                            temp.append(fh.read(item3["size"]).decode("latin-1"))
                    elif item3["type"] == "sprite":
                        temp.append(item3["sprite"])
                        # print(fh.read(item3["size"]))
                text_block.append(temp)
            text.append(text_block)
    if os.path.exists(temp_file):
        os.remove(temp_file)
    formatted_text = []
    for t in text:
        y = []
        for x in t:
            y.append({"text": x})
        formatted_text.append(y)
    return formatted_text

text_file_names = [
    "Bonus Instructions",
    "Story Level Intro Text",
    "Kong Names",
    "Diddy",
    "Tiny",
    "Chunky",
    "Lanky",
    "Funky",
    "Cranky",
    "Candy",
    "Llama",
    "Snide",
    "DK TV Screen",
    "Dolby",
    "Beetle",
    "Vulture",
    "Squawks",
    "Factory Car Race",
    "Seal Race",
    "Misc & Microbuffer",
    "Rabbit",
    "Owl",
    "Worm",
    "Mermaid",
    "DK",
    "Training Grounds",
    "Bonus Encouragement Text",
    "K. Lumsy",
    "Seal Race 2",
    "B. Locker",
    "Fairy Queen",
    "Beanstalk",
    "Unused Lanky NPC",
    "Ice Tomato",
    "Castle Car Race",
    "Location and Level Names",
    "Pause Menu",
    "Main Menu",
    "Race Positions",
    "Move Names",
    "Fairy Queen Rareware Door",
    "Wrinkly",
    "Snide's Bonus Games",
]
for xi, x in enumerate(text_file_names):
    with open(f"../text_files/jsonstorage/[{xi}] - {x}.json", "w", encoding="utf-8") as file:
        json.dump(grabText(xi, 0), file, indent=4)
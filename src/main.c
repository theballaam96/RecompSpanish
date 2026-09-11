#include "modding.h"
#include "ultra64.h"
#include "enums.h"
#include "common_structs.h"
#include "font.h"

typedef struct {
    u8 file_start;
    u8 file_count;
    u8 height;
    u8 kerning_space;
    u8 kerning_character;
    u8 kerning_animation;
} Struct80754A34;
extern Struct80754A34 D_global_asm_80754A34[];
extern u8 *text_files[];
extern u16 text_file_sizes[];
extern u8 *fonttextures_1[];
extern u8 *fonttextures_6[];
extern u16 fontsizes_1[];
extern u16 fontsizes_6[];
extern CharStruct *D_global_asm_80754A18[7];
extern CharStruct font_1_characters[];
extern CharStruct font_6_characters[];
extern u8 fontstring_1[];
extern u8 fontstring_6[];
extern u8 fontstarts_1[];
extern u8 fontstarts_6[];
extern s8 fontydeltas_1[];
extern s8 fontydeltas_6[];
extern u8 *D_global_asm_807549FC[7];
u8 *_strchr(const u8 *str, s32 c);

RECOMP_PATCH s8 func_global_asm_806FB914(s16 arg0, u8 *arg1) {
    s8 ret;

    ret = 0;
    switch (arg0) {
        case 0:
            switch (*arg1) {
                case 0x2E:
                case 0x67:
                case 0x70:
                case 0x71:
                case 0x80:
                    ret = 2;
                    break;
                case 0x61:
                case 0x79:
                    ret = 1;
                    break;
            }
            *arg1 -= 0x21;
            break;
        case 1:
            *arg1 = _strchr(fontstring_1, *arg1) - fontstring_1;
            ret = fontydeltas_1[*arg1];
            break;
        case 6:
            *arg1 = _strchr(fontstring_6, *arg1) - fontstring_6;
            ret = fontydeltas_6[*arg1];
            break;
        case 2:
        {
            const char sp38[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.-?{}:=0123456789<>m)!@#$%^&cab";
            *arg1 = _strchr((const u8*)sp38, *arg1) - (u8*)sp38;
            break;
        }
        case 3:
        case 7:
        {
            const char sp28[] = "0123456789%/";
            *arg1 = _strchr((const u8*)sp28, *arg1) - (u8*)sp28;
            break;
        }
        case 4:
            if (*arg1 == 0x40) {
                *arg1 = 0x60;
            } else {
                *arg1 = *arg1 - 0x21;
            }
            break;
        case 5:
            *arg1 -= 0x21;
            break;
    }
    return ret;
}

extern void **D_global_asm_807FD7F0;
extern u8 *D_global_asm_807FD7F4;
void func_global_asm_80611690(void *arg0);
void *_malloc(s32);
void *func_global_asm_806FBB9C(s16 textureIndex);
RECOMP_PATCH void func_global_asm_806FBB58(void) {
    D_global_asm_807FD7F0 = _malloc(sizeof(s32) * 256);
    func_global_asm_80611690(D_global_asm_807FD7F4 = _malloc(sizeof(u8) * 256));
}

RECOMP_PATCH Gfx *func_global_asm_806FBEF0(Gfx *dl, u8 arg1, s16 arg2) {
    s16 textureIndex;

    textureIndex = (D_global_asm_80754A34[arg1].file_start + arg2) - 1;
    func_global_asm_806FBB9C(textureIndex);
    switch (arg1) {
        case 6:
            gDPLoadTextureBlock(dl++, (s32)D_global_asm_807FD7F0[textureIndex] + 0x80000000,
                G_IM_FMT_IA, G_IM_SIZ_8b, 256, 16, 0,
                G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMIRROR | G_TX_CLAMP,
                G_TX_NOMASK, G_TX_NOMASK,
                G_TX_NOLOD, G_TX_NOLOD);
            break;
        case 0:
            gDPSetTextureImage(dl++, G_IM_FMT_IA, G_IM_SIZ_16b, 1, (s32)D_global_asm_807FD7F0[textureIndex] + 0x80000000);\
            gDPSetTile(dl++, G_IM_FMT_IA, G_IM_SIZ_16b, 0, 0x0000, G_TX_LOADTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPLoadSync(dl++);\
            gDPLoadBlock(dl++, G_TX_LOADTILE, 0, 0, 2047, 64);\
            gDPPipeSync(dl++);\
            gDPSetTile(dl++, G_IM_FMT_IA, G_IM_SIZ_4b, 32, 0x0000, G_TX_RENDERTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPSetTileSize(dl++, G_TX_RENDERTILE, 0, 0, 0x07FC, 0x003C);\
            break;
        case 1:
            gDPLoadTextureBlock(dl++, (s32)D_global_asm_807FD7F0[textureIndex] + 0x80000000,
                G_IM_FMT_RGBA, G_IM_SIZ_16b, 80, 24, 0,
                G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMIRROR | G_TX_CLAMP,
                G_TX_NOMASK, G_TX_NOMASK,
                G_TX_NOLOD, G_TX_NOLOD);
            break;
        case 2:
            gDPSetTextureImage(dl++, G_IM_FMT_I, G_IM_SIZ_16b, 1, (s32)D_global_asm_807FD7F0[textureIndex] + 0x80000000);\
            gDPSetTile(dl++, G_IM_FMT_I, G_IM_SIZ_16b, 0, 0x0000, G_TX_LOADTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPLoadSync(dl++);\
            gDPLoadBlock(dl++, G_TX_LOADTILE, 0, 0, 1023, 64);\
            gDPPipeSync(dl++);\
            gDPSetTile(dl++, G_IM_FMT_I, G_IM_SIZ_4b, 32, 0x0000, G_TX_RENDERTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPSetTileSize(dl++, G_TX_RENDERTILE, 0, 0, 0x07FC, 0x001C);\
            break;
        case 3:
        case 7:
            gDPSetTextureImage(dl++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, (s32)D_global_asm_807FD7F0[textureIndex] + 0x80000000);\
            gDPSetTile(dl++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 0, 0x0000, G_TX_LOADTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPLoadSync(dl++);\
            gDPLoadBlock(dl++, G_TX_LOADTILE, 0, 0, 1023, 256);\
            gDPPipeSync(dl++);\
            gDPSetTile(dl++, G_IM_FMT_RGBA, G_IM_SIZ_16b, 8, 0x0000, G_TX_RENDERTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPSetTileSize(dl++, G_TX_RENDERTILE, 0, 0, 0x007C, 0x007C);\
            break;
        case 4:
            gDPSetTextureImage(dl++, G_IM_FMT_I, G_IM_SIZ_16b, 1, (s32)D_global_asm_807FD7F0[textureIndex] + 0x80000000);\
            gDPSetTile(dl++, G_IM_FMT_I, G_IM_SIZ_16b, 0, 0x0000, G_TX_LOADTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPLoadSync(dl++);\
            gDPLoadBlock(dl++, G_TX_LOADTILE, 0, 0, 2047, 32);\
            gDPPipeSync(dl++);\
            gDPSetTile(dl++, G_IM_FMT_I, G_IM_SIZ_4b, 64, 0x0000, G_TX_RENDERTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPSetTileSize(dl++, G_TX_RENDERTILE, 0, 0, 0x0FFC, 0x001C);\
            break;
        case 5:
            gDPSetTextureImage(dl++, G_IM_FMT_I, G_IM_SIZ_16b, 1, (s32)D_global_asm_807FD7F0[textureIndex] + 0x80000000);\
            gDPSetTile(dl++, G_IM_FMT_I, G_IM_SIZ_16b, 0, 0x0000, G_TX_LOADTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPLoadSync(dl++);\
            gDPLoadBlock(dl++, G_TX_LOADTILE, 0, 0, 2047, 32);\
            gDPPipeSync(dl++);\
            gDPSetTile(dl++, G_IM_FMT_I, G_IM_SIZ_4b, 64, 0x0000, G_TX_RENDERTILE, 0, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_CLAMP, G_TX_NOMASK, G_TX_NOLOD);\
            gDPSetTileSize(dl++, G_TX_RENDERTILE, 0, 0, 0x0FFC, 0x001C);\
            break;
    }
    return dl;
}



RECOMP_CALLBACK("*", recomp_on_asset_file_load_override)
void languageHackLoader(s32 tableIndex, s32 fileIndex, u8 **outputFile, s32 *file_size)
{
    u8 player_index;
    u16 font_1_start, font_6_start;

    if (tableIndex == 12) {
        *outputFile = (u8*)&text_files[fileIndex][0];
        *file_size = text_file_sizes[fileIndex];
    } else if (tableIndex == 14) {
        font_1_start = (256 - (FONT_1_COUNT + FONT_6_COUNT));
        font_6_start = (256 - (FONT_6_COUNT));
        if (fileIndex >= font_6_start) {
            *outputFile = (u8*)&fonttextures_6[fileIndex - font_6_start][0];
            *file_size = fontsizes_6[fileIndex - font_6_start];
        } else if (fileIndex >= font_1_start) {
            *outputFile = (u8*)&fonttextures_1[fileIndex - font_1_start][0];
            *file_size = fontsizes_1[fileIndex - font_1_start];
        }
    }
}

RECOMP_CALLBACK("*", recomp_on_init)
void languageHackInit(void)
{
    D_global_asm_80754A34[1].file_start = 256 - (FONT_1_COUNT + FONT_6_COUNT);
    D_global_asm_80754A34[1].file_count = FONT_1_COUNT;
    D_global_asm_80754A34[6].file_start = 256 - (FONT_6_COUNT);
    D_global_asm_80754A34[6].file_count = FONT_6_COUNT;
    D_global_asm_80754A34[6].height = 16; // Bug fix
    D_global_asm_80754A18[1] = font_1_characters;
    D_global_asm_80754A18[6] = font_6_characters;
    D_global_asm_807549FC[1] = fontstarts_1;
    D_global_asm_807549FC[6] = fontstarts_6;
}
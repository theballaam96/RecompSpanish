
# Porting this over to your own language

Here is a step by step guide on how to make your own language mod with this framework:
## Extracting Vanilla Text
1.  To do so, place your US (`dk64.z64`) or PAL (`dk64_pal.z64`) z64 ROM into `/text_converter`
2. Run either `text_decoder.py` or `text_decoder_pal.py` depending on what version your ROM is. 
> [!NOTE] 
> The PAL extractor will automatically extract the English text from ROM. If you wish to extract the other languages, change the 2nd arg of `grabText` in that file to 1 (French), 2 (German) or 3 (Spanish).
3. This will write a bunch of files in `/text_files/jsonstorage`. To convert these to the `.txt` files, go to `/text_files` and run `to_txt.py`

## Changing the text
1. To change the text, just overwrite the text files you wish to change. See the Text Syntax section for how these files are written
2. Once you are happy with the changes you've made, go to `/text_converter` and run `converter.py`. This will write the text files to a format that DK64 can understand better to `/src/text.c`
3. Run `make` and `./build.sh` or `./build.bat` (depending on your OS) to build your changes into the `.nrm`

## Adding new font characters
The font is stored in `/font` and will only currently modify the "white font" (what's seen in text bubbles, K Rool story intro text etc) and the "yellow font" (What's seen on the pause menu, level intro banners etc).
The white font is actually based on (or just heavily similar to) the `Tekton Bold` font. As such, if possible, try and add your new characters via what that character looks like with `Tekton Bold`. The yellow font unfortunately doesn't have an accompanying font type, so you'll have to get creative with this one.
1. To add a new font character, add the image of that character to the accompanying font directory (`/font/white` for the white font, `/font/yellow` for the yellow font). It must be the `.png` format, and the height must match what is expected for that font (16px for the white font, 24px for the yellow font). Name this file whatever you'd like
2. To match the font image you made to the character associated with it when you're typing it in a text file, go to the `config.json` file in the associated directory for your font, and add an entry for your letter. The entry is of format:
```
"file_name": "associated_character"
```
For example, if you were adding the German eszett character (`ß`), and you named the file `eszett.png`, your entry would look like:
```
"eszett": "ß"
```
3. Once you've made your desired changes, run `joiner.py`. This joins all your font characters together, writes them to `/src/font.c` and also writes several tables that need to be changed to account for changes to the font.

## Text Syntax
### Straight language ports
DK64 does several hidden things with it's text files to make text behave nicely. If you're doing a straight language port, I'd advise not messing with any tags in square brackets.
Do not mess with any words inside icon tags either in terms of converting the icon name to a different language (eg. `[icon]ButtonA[/icon]`). These icon names are just human-friendly names that feed to the converter so that it can convert those to the codes used for icons.
Each line of text in the `.txt` files is 1 entry in the text file (eg. 1 speech bubble). It is not advised to add any extra line breaks into your mod.
### More complex mods
However, if you **are** doing something other that than a straight language port, or want to know how the syntax works. All of these work in text bubbles, but not sure elsewhere:
- `[kong]` mentions the current kong's name
- `[number]` mentions a dynamic number written to by the game's code. The devs likely did this to make requirement changes quicker to make without having to mess with the text files. To change this value, change `D_global_asm_80750AC8`.
- `[wobble][/wobble]` makes any text inside it wobble
- `[pop][/pop]` makes any text do a pop effect as it appears
- `[/spin][/spin]` makes any text spin when it appears
- `[icon][/icon]` displays an icon in the text. To see all values, look at the `Icons` enum in `/text_converter/converter.py`
- `[newline]` splits the text into a new line. This might have been for memory reasons on the N64?
- `[forcednewline]` splits the text into a new line. For some reason the devs needed this too?


## Things to keep an eye on
1. DK64 really doesn't like super long words because it doesn't know how to properly break things up. If possible, try to limit yourself to 13 letters or less.
2. Whilst we have a fair bit of space to do additional characters, don't go incredibly overboard. Best to check that the total amount of png files in `/font/output` is less than 50.

# waifu-pics

It's a module you can use to get image/gif urls with ease

# How To Use

```py
from waifu_pics import Waifu

print(Waifu.waifu_pics(False, 'waifu'))
```

Using the code above will output a picture that is sfw and is in the 'waifu' category

There are 4 methods you can use : waifu_pics, waifu_im, hmtai, neko_bot

From the first 3 you can get both sfw and nsfw pictures

About the last one(neko_bot), you can only get nsfw pictures

```py
print(Waifu.waifu_pics(nsfw = False, category = 'waifu'))
print(Waifu.waifu_im(category = 'waifu'))
print(Waifu.hmtai(nsfw = False))
```
You can leave the nsfw arg empty to get sfw pictures

Also you can leave the category arg empty to get a random category

```py
print(Waifu.neko_bot(category = '4k')
```

The neko_bot method doesn't take a nsfw arg

# The Categories

`waifu_pics` :

nsfw : 

"waifu","neko","trap","blowjob"

sfw : "waifu","neko","shinobu","megumin","bully","cuddle","cry","hug","awoo","kiss","lick","pat","smug","bonk","yeet","blush","smile","wave","highfive","handhold","nom","bite","glomp","slap","kill","kick","happy","wink","poke","dance","cringe"


`waifu_im` :

nsfw : 

"ero","ass","hentai","milf","oral","paizuri","ecchi"

sfw :

"waifu","maid","marin-kitagawa","mori-calliope","raiden-shogun","oppai","selfies","uniform","kamisato-ayaka"


`hmtai` :

nsfw : "ass","anal","bdsm","classic","cum","creampie","manga","femdom","hentai","incest","masturbation","public","ero","orgy","elves","yuri","pantsu","pussy","glasses","cuckold","blowjob","boobjob","handjob","footjob","boobs","thighs","ahegao","uniform","gangbang","tentacles","gif","nsfwNeko","nsfwMobileWallpaper","zettaiRyouiki"

sfw : "wave","wink","tea","bonk","punch","poke","bully","pat","kiss","kick","blush","feed","smug","hug","cuddle","cry","cringe","slap","five","glomp","happy","hold","nom","smile","throw","lick","bite","dance","boop","sleep","like","kill","tickle","nosebleed","threaten","depression","wolf_arts","jahy_arts","neko_arts","coffee_arts","wallpaper","mobileWallpaper"


`neko_bot` :

nsfw : 

"hass","pgif","4k","hentai","hneko","hkitsune","anal","hanal","gonewild","ass","pussy","thigh","hthigh","tentacle","boobs","hboobs","yaoi","paizuri"

sfw : None



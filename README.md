# waifu-pics

It's a library you can use to get image/gif urls with ease

# How To Use

```py
from waifu_pics import Waifu

print(Waifu.waifu_pics(False, 'waifu'))
```

Using the code above will output a picture that is sfw and is in the 'waifu' category\n

There are 4 methods you can use : waifu_pics, waifu_im, hmtai, neko_bot\n
From the first 3 you can get both sfw and nsfw pictures\n
About the last one(neko_bot), you can only get nsfw pictures\n

```py
print(Waifu.waifu_pics(nsfw = False, category = 'waifu'))
print(Waifu.waifu_im(category = 'waifu'))
print(Waifu.waifu_pics(nsfw = False))
```
You can leave the nsfw arg empty to get sfw pictures
Also you can leave the category arg empty to get a random category



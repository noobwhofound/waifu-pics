import requests as req
from random import choice

class NotaValidCategory(Exception):
    """
    The category entered isn't a valid category
    """

class NotFound(Exception):
    """
    Couldn't find the item
    """

class Waifu:

    def waifu_pics(nsfw : bool = None, category : str = None):
        """
        Leave the nsfw arg empty to get sfw pictures and leave the category arg empty to get random pictures
        """
        if nsfw == None :
            nsfw = False
        if nsfw == True :
            nsfw = "nsfw"
            if category == None :
                category = choice(["waifu", "neko", "trap", "blowjob"])
            category = category.lower()
            if not category in ["waifu", "neko", "trap", "blowjob"]:
                raise NotaValidCategory
        elif nsfw == False :
            nsfw = "sfw"
            if category == None:
                category = choice(["waifu","neko","shinobu","megumin","bully","cuddle","cry","hug","awoo","kiss","lick","pat","smug","bonk","yeet","blush","smile","wave","highfive","handhold","nom","bite","glomp","slap","kill","kick","happy","wink","poke","dance","cringe"])
            category = category.lower()
            if not category in ["waifu","neko","shinobu","megumin","bully","cuddle","cry","hug","awoo","kiss","lick","pat","smug","bonk","yeet","blush","smile","wave","highfive","handhold","nom","bite","glomp","slap","kill","kick","happy","wink","poke","dance","cringe"] :
                raise NotaValidCategory
        res = req.get(f"https://api.waifu.pics/{nsfw}/{category}")
        if res.json()['url']:
            return res.json()['url']
        else :
            raise NotFound
    
    def waifu_im(nsfw : bool = None, category : str = None):
        """
        Leave the nsfw arg empty to get sfw pictures and leave the category arg empty to get random pictures
        """
        if nsfw == None :
            nsfw = False
        if nsfw == False :
            if category == None :
                category = choice(["waifu","maid","marin-kitagawa","mori-calliope","raiden-shogun","oppai","selfies","uniform","kamisato-ayaka"])
            category = category.lower()
            if not category in ["waifu","maid","marin-kitagawa","mori-calliope","raiden-shogun","oppai","selfies","uniform","kamisato-ayaka"]:
                raise NotaValidCategory
        elif nsfw == True :
            if category == None:
                category = choice(["ero","ass","hentai","milf","oral","paizuri","ecchi"])
            category = category.lower()
            if not category in ["ero","ass","hentai","milf","oral","paizuri","ecchi"]:
                raise NotaValidCategory
        params = {
            'included_tags': [f'{category}']
        }
        res = req.get("https://api.waifu.im/search", params=params)
        if res.json()['images'][0]['url']:
            return res.json()['images'][0]['url']
        else :
            raise NotFound
    
    def hmtai(nsfw : bool = None, category : str = None):
        """
        Leave the nsfw arg empty to get sfw pictures and leave the category arg empty to get random pictures
        """
        if nsfw == None :
            nsfw = False
        if nsfw == True :
            nsfw = "nsfw"
            if category == None :
                category = choice(["ass","anal","bdsm","classic","cum","creampie","manga","femdom","hentai","incest","masturbation","public","ero","orgy","elves","yuri","pantsu","pussy","glasses","cuckold","blowjob","boobjob","handjob","footjob","boobs","thighs","ahegao","uniform","gangbang","tentacles","gif","nsfwNeko","nsfwMobileWallpaper","zettaiRyouiki"])
            if not category in ["ass","anal","bdsm","classic","cum","creampie","manga","femdom","hentai","incest","masturbation","public","ero","orgy","elves","yuri","pantsu","pussy","glasses","cuckold","blowjob","boobjob","handjob","footjob","boobs","thighs","ahegao","uniform","gangbang","tentacles","gif","nsfwNeko","nsfwMobileWallpaper","zettaiRyouiki"]:
                raise NotaValidCategory
        elif nsfw == False :
            nsfw = "sfw"
            if category == None:
                category = choice(["wave","wink","tea","bonk","punch","poke","bully","pat","kiss","kick","blush","feed","smug","hug","cuddle","cry","cringe","slap","five","glomp","happy","hold","nom","smile","throw","lick","bite","dance","boop","sleep","like","kill","tickle","nosebleed","threaten","depression","wolf_arts","jahy_arts","neko_arts","coffee_arts","wallpaper","mobileWallpaper"])
            category = category.lower()
            if not category in ["wave","wink","tea","bonk","punch","poke","bully","pat","kiss","kick","blush","feed","smug","hug","cuddle","cry","cringe","slap","five","glomp","happy","hold","nom","smile","throw","lick","bite","dance","boop","sleep","like","kill","tickle","nosebleed","threaten","depression","wolf_arts","jahy_arts","neko_arts","coffee_arts","wallpaper","mobileWallpaper"] :
                raise NotaValidCategory
        res = req.get(f"https://hmtai.hatsunia.cfd/{nsfw}/{category}")
        if res.json()['url']:
            return res.json()['url']
        else :
            raise NotFound
    def neko_bot(category : str = None):
        """
        With this api you might get some 'real life' nsfw pictures
        ---
        Leave the category arg empty to get random pictures
        ---
        This is an only-nsfw api
        """
        if category == None :
            category = choice(["hass","pgif","4k","hentai","hneko","hkitsune","anal","hanal","gonewild","ass","pussy","thigh","hthigh","tentacle","boobs","hboobs","yaoi","paizuri"])
        category = category.lower()
        if not category in ["hass","pgif","4k","hentai","hneko","hkitsune","anal","hanal","gonewild","ass","pussy","thigh","hthigh","tentacle","boobs","hboobs","yaoi","paizuri"]:
            raise NotaValidCategory
        params = {
            'type' : f'{category}'
        }
        res = req.get("https://nekobot.xyz/api/image", params = params)
        if res.json()['message']:
            return res.json()['message']
        else :
            raise NotFound
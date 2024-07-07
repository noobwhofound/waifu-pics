import requests as req
from random import choice

class NotaValidCategory(Exception):
    """
    The category entered isn't a valid category
    """
    pass

class NotFound(Exception):
    """
    Couldn't find the item
    """
    pass

class Waifu:

    wp_nsfw_categories = ["waifu", "neko", "trap", "blowjob"]
    wp_sfw_categories = ["waifu","neko","shinobu","megumin","bully","cuddle","cry","hug","awoo","kiss","lick","pat","smug","bonk","yeet","blush","smile","wave","highfive","handhold","nom","bite","glomp","slap","kill","kick","happy","wink","poke","dance","cringe"]
    wp_url = "https://api.waifu.pics/"

    wim_nsfw_categories = ["ero","ass","hentai","milf","oral","paizuri","ecchi"]
    wim_sfw_categories = ["waifu","maid","marin-kitagawa","mori-calliope","raiden-shogun","oppai","selfies","uniform","kamisato-ayaka"]
    wim_url = "https://api.waifu.im/search"




    
    def __init__(self):
        pass

    
    def waifu_pics(self, nsfw : bool = None, category : str = None) -> str:
        """
        Leave the nsfw arg empty to get sfw pictures and leave the category arg empty to get random pictures
        """
        if nsfw == None :
            nsfw = False
        if nsfw == True :
            nsfw = "nsfw"
            if category == None :
                category = choice(self.wp_nsfw_categories)
            category = category.lower()
            if not category in self.wp_nsfw_categories:
                raise NotaValidCategory
        elif nsfw == False :
            nsfw = "sfw"
            if category == None:
                category = choice(self.wp.sfw.categories)
            category = category.lower()
            if not category in self.wp.sfw.categories:
                raise NotaValidCategory
        res = req.get(f"{self.wp_url}{nsfw}/{category}")
        if res.json()['url']:
            return res.json()['url']
        else :
            raise NotFound
    
    def waifu_im(self, nsfw : bool = None, category : str = None) -> str:
        """
        Leave the nsfw arg empty to get sfw pictures and leave the category arg empty to get random pictures
        """
        if nsfw == None :
            nsfw = False
        if nsfw == False :
            if category == None :
                category = choice(self.wim_sfw_categories)
            category = category.lower()
            if not category in self.wim_sfw_categories:
                raise NotaValidCategory
        elif nsfw == True :
            if category == None:
                category = choice(self.wim_nsfw_categories)
            category = category.lower()
            if not category in self.wim_nsfw_categories:
                raise NotaValidCategory
        params = {
            'included_tags': [f'{category}']
        }
        res = req.get(self.wim_url, params=params)
        if res.json()['images'][0]['url']:
            return res.json()['images'][0]['url']
        else :
            raise NotFound
    
    def hmtai(self, nsfw : bool = None, category : str = None) -> str:
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
    def neko_bot(self, category : str = None) -> str:
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

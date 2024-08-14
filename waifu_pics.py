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

    hm_nsfw_categories = ["ass","anal","bdsm","classic","cum","creampie","manga","femdom","hentai","incest","masturbation","public","ero","orgy","elves","yuri","pantsu","pussy","glasses","cuckold","blowjob","boobjob","handjob","footjob","boobs","thighs","ahegao","uniform","gangbang","tentacles","gif","nsfwNeko","nsfwMobileWallpaper","zettaiRyouiki"]
    hm_sfw_categories = ["wave","wink","tea","bonk","punch","poke","bully","pat","kiss","kick","blush","feed","smug","hug","cuddle","cry","cringe","slap","five","glomp","happy","hold","nom","smile","throw","lick","bite","dance","boop","sleep","like","kill","tickle","nosebleed","threaten","depression","wolf_arts","jahy_arts","neko_arts","coffee_arts","wallpaper","mobileWallpaper"]
    hm_url = "https://hmtai.hatsunia.cfd/"

    nb_nsfw_categories = ["hass","pgif","4k","hentai","hneko","hkitsune","anal","hanal","gonewild","ass","pussy","thigh","hthigh","tentacle","boobs","hboobs","yaoi","paizuri"]
    nb_url = "https://nekobot.xyz/api/image"
    
    def __init__(self):
        pass

    def make_req(self, url : str, params : dict = None):
        return req.get(url, params = params).json() if params else req.get(url).json()
    
    def waifu_pics(self, nsfw : bool = None, category : str = None) -> str:
        """
        Leave the nsfw arg empty to get sfw pictures and leave the category arg empty to get random pictures
        """
        nsfw = 'nsfw' if nsfw == True else 'sfw'

        if nsfw == 'nsfw':
            if category == None :
                category = choice(self.wp_nsfw_categories)
            else:
                category = category.lower()
                if not category in self.wp_nsfw_categories:
                    raise NotaValidCategory
                
        else:
            if category == None:
                category = choice(self.wp.sfw.categories)
            else :
                category = category.lower()
                if not category in self.wp.sfw.categories:
                    raise NotaValidCategory
                
        data = self.make_req(f"{self.wp_url}{nsfw}/{category}")['url']

        if data:
            return data
        else :
            raise NotFound
    
    def waifu_im(self, nsfw : bool = None, category : str = None) -> str:
        """
        Leave the nsfw arg empty to get sfw pictures and leave the category arg empty to get random pictures
        """
        nsfw = True if nsfw == True else False

        if nsfw == False :
            if category == None :
                category = choice(self.wim_sfw_categories)
            else :
                category = category.lower()
                if not category in self.wim_sfw_categories:
                    raise NotaValidCategory
                
        else:
            if category == None:
                category = choice(self.wim_nsfw_categories)
            else:
                category = category.lower()
                if not category in self.wim_nsfw_categories:
                    raise NotaValidCategory
            
        data = self.make_req(self.wim_url, params = {'included_tags': [f'{category}']})['images'][0]['url']
        if data:
            return data
        else :
            raise NotFound
    
    def hmtai(self, nsfw : bool = None, category : str = None) -> str:
        """
        Leave the nsfw arg empty to get sfw pictures and leave the category arg empty to get random pictures
        """
        nsfw = 'nsfw' if nsfw == True else 'sfw'

        if nsfw == 'nsfw' :
            if category == None :
                category = choice(self.hm_nsfw_categories)
            else :
                category = category.lower()
                if not category in self.hm_nsfw_categories:
                    raise NotaValidCategory
                
        else:
            if category == None:
                category = choice(self.hm_sfw_categories)
            else:
                category = category.lower()
                if not category in self.hm_sfw_categories:
                    raise NotaValidCategory
            
        data = self.make_req(f"{self.hm_url}{nsfw}/{category}")['url']
        if data:
            return data
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
            category = choice(self.nb_nsfw_categories )
        else :
            category = category.lower()
            if not category in self.nb_nsfw_categories :
                raise NotaValidCategory

        data = self.make_req(self.nb_url, params = {'type' : f'{category}'})['message']
        if data:
            return data
        else :
            raise NotFound

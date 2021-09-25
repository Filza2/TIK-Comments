try:
    from time import sleep 
    from requests import post
    from colorama import Fore
except Exception as b:exit(f"[!] Please Download The lib:\n{b}")
error=0
done=0
print(f"""
{Fore.RED}
 TIKTOK{Fore.RESET}
{Fore.LIGHTRED_EX}  ██████╗  ███╗   ███╗
{Fore.LIGHTRED_EX} ██╔════╝  ████╗ ████║
{Fore.LIGHTRED_EX} ██║       ██╔████╔██║
{Fore.LIGHTRED_EX} ██║       ██║╚██╔╝██║
{Fore.LIGHTRED_EX} ╚██████╗  ██║ ╚═╝ ██║
{Fore.LIGHTRED_EX}  ╚═════╝  ╚═╝     ╚═╝ {Fore.RESET}                                                          
</> {Fore.GREEN}@TweakPY - @vv1ck{Fore.RESET}""")
print("=====================================")
sessionid=input("[+] Enter Your seesion ID: ")
try:url=input("[+] Enter The Post url: ");postid=url.split('/video/')[1].split('?')[0]
except:postid=input("[+] Enter The Post ID: ")
tx=input("[+] Enter Your Text: ")
print("=====================================")
usr='none'
url=f'https://www.tiktok.com/api/comment/publish/?aid=1988&app_language=en&app_name=tiktok_web&aweme_id={postid}&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%29&cookie_enabled=true&device_id=7011872384592578050&device_platform=web_pc&focus_state=false&from_page=video&history_len=15&is_fullscreen=false&is_page_visible=true&os=linux&priority_region=SA&referer=https%3A%2F%2Fwww.tiktok.com%2F%40ra_28%3F&region=SA&root_referer=https%3A%2F%2Fwww.tiktok.com%2Flogin%2Fqrcode&screen_height=768&screen_width=1366&text={tx}&text_extra=%5B%5D&timezone_name=America%2FNew_York&verifyFp=verify_ktzvck05_L6NbGHJK_OJZs_4kn4_8A3o_6jcpKVxr2NmC&msToken=4r06GZptINBmTVlX_Kpu1q221Lce1MsC7tQurJPY9aN0CGh-kPoGNCIW2dvFes8tBlnHgSMKqVEHEaef_1b20Tl4Y9hvs7wLWKYtbG19PK-vDBCeYPmpVzCf5ADbFpQKkw==&X-Bogus=DFSzsIVL50xANHzRSFFPYzWdbTbM&_signature=_02B4Z6wo00001ZweOdAAAIDBtmfBRg1qKkWcHz1AAAZJa1'
head={
    'Host': 'www.tiktok.com',
    'Cookie': f'ttwid=1%7Cv65IlMNSVujsyD1ItjTAl9tzHfI1ZhNfmDHdR_MEVi8%7C1632579276%7C52e6c81ce43a29bffdc244066543e575e1df3a61fc3b650b0162c3d3210979e7; tt_webid_v2=7011872384592578050; tt_webid=7011872384592578050; tt_csrf_token=ye1uEMrpKKTVEOwPtrlsVDzR; csrf_session_id=5632ca3d21da42a696ad3ab3f2467ab4; R6kq3TV7=ADlFRx18AQAA8HDrzAE8FHH9DuqOyADa1QFm6kwSmAmTN2gLiF6jetoqB1Yw|1|0|f1a2e0c96c22d26a6585a8a4d9e08bb3265ecab9; passport_csrf_token_default=86d30db9b83f6aa408122cd61cadbbcc; passport_csrf_token=86d30db9b83f6aa408122cd61cadbbcc; cmpl_token=AgQQAPOvF-RMpbCWRisot104-y61-ymcP4A0YPy3QQ; sid_guard={sessionid}%7C1632578906%7C5184000%7CWed%2C+24-Nov-2021+14%3A08%3A26+GMT; uid_tt=36abe00256cdb3d7061447d5f805feba18506447025ce1fe570eaa124c9a6f37; uid_tt_ss=36abe00256cdb3d7061447d5f805feba18506447025ce1fe570eaa124c9a6f37; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; sid_ucp_v1=1.0.0-KGViZTdmMWY4MDdmMjAxMTdiMmM0MzRiMWU3OTM5ZDM4ZjUxZWE4OTUKIAiBiJaEypGq1GAQ2tq8igYYswsgDDD01aKFBjgHQPQHEAEaA3NnMSIgYjliZmRmMTEzYjhkYzQyNzI4NWIwYmViYjRmYzE5YjE; ssid_ucp_v1=1.0.0-KGViZTdmMWY4MDdmMjAxMTdiMmM0MzRiMWU3OTM5ZDM4ZjUxZWE4OTUKIAiBiJaEypGq1GAQ2tq8igYYswsgDDD01aKFBjgHQPQHEAEaA3NnMSIgYjliZmRmMTEzYjhkYzQyNzI4NWIwYmViYjRmYzE5YjE; store-idc=alisg; store-country-code=kw; odin_tt=1c3a2d10eefc45860c9e61e0533f0265b18471fe8cfc4eefc197045ee9b9e0a265b3e5558ee92229e957bacf2a91557c272be04b87ad96b50d68f037c4cf8886f52715d77b04b0c2ece0d9836a69d61d; passport_fe_beating_status=true; csrf_session_id=5632ca3d21da42a696ad3ab3f2467ab4; s_v_web_id=verify_ktzvck05_L6NbGHJK_OJZs_4kn4_8A3o_6jcpKVxr2NmC; msToken=4r06GZptINBmTVlX_Kpu1q221Lce1MsC7tQurJPY9aN0CGh-kPoGNCIW2dvFes8tBlnHgSMKqVEHEaef_1b20Tl4Y9hvs7wLWKYtbG19PK-vDBCeYPmpVzCf5ADbFpQKkw==; msToken=ZMtDQA7NBN70h1nfe6mnS_fQcmYTJG8HPjYVInJhYeRyDrITLV0nA86y5c6-BE6EqolQKv9OxE00limA2AD7pwwIssFkoFADAlqNUqAYZbW8kv8pFWbC0GWLFv50F4rPGmY=',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '0',
    'Tt-Csrf-Token': 'ye1uEMrpKKTVEOwPtrlsVDzR',
    'X-Secsdk-Csrf-Token': '00010000000146860da3e5491dafd2cfe4f06bb813ffc006919b10819772a15f4ff70bd155df16a81665e0eb975d',
    'Origin': 'https://www.tiktok.com',
    'Referer': f'https://www.tiktok.com/@{usr}/video/{postid}?is_from_webapp=v1&is_copy_url=1',
    'Te': 'trailers'}
while True:
    sleep(6.6)
    req=post(url,headers=head)
    if 'Comment sent successfully' in req.text:
        print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}')
        done+=1
    elif 'Login expired' in req.text:exit(f'[⚠] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱\nsession id [{sessionid}]')
    elif '{}' in req.text:exit(f'[🛑] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗮𝗻𝗻𝗲𝗱\nsession id [{sessionid}]')
    else:
        print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}')
        error+=1
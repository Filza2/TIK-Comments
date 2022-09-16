try:from time import sleep ;from requests import post;from colorama import Fore
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
error,done=0,0
print(f"""{Fore.LIGHTRED_EX} 
████████╗██╗██╗  ██╗      ██████╗███╗   ███╗
╚══██╔══╝██║██║ ██╔╝     ██╔════╝████╗ ████║
   ██║   ██║█████╔╝█████╗██║     ██╔████╔██║
   ██║   ██║██╔═██╗╚════╝██║     ██║╚██╔╝██║
   ██║   ██║██║  ██╗     ╚██████╗██║ ╚═╝ ██║
   ╚═╝   ╚═╝╚═╝  ╚═╝      ╚═════╝╚═╝     ╚═╝{Fore.RESET}                                                          
           By @TweakPY - @vv1ck""")
print("=====================================")
sessionid=input("[+] Enter Your seesion ID: ")
try:url=input("[+] Enter The Post url: ");postid=url.split('/video/')[1].split('?')[0]
except:postid=input("[+] Enter The Post ID: ")
tx=input("[+] Enter Your Text: ")
print("=====================================")
usr='none'
url=f'https://www.tiktok.com/api/comment/publish/?aid=1988&app_language=en&app_name=tiktok_web&aweme_id={postid}&browser_language=en&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%29&channel=tiktok_web&cookie_enabled=true&device_id=7122424033622476290&device_platform=web_pc&focus_state=true&from_page=video&history_len=6&is_fullscreen=false&is_page_visible=true&os=linux&priority_region=SA&referer=https%3A%2F%2Fwww.tiktok.com%2Far%2F&region=SA&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&text={tx}&text_extra=%5B%5D&tz_name=Asia%2FRiyadh&verifyFp=verify_l7chdt9a_7slNGyxb_mBhG_43Ss_8P7z_waU60HRLX7Az&webcast_language=ar&msToken=p1ktJG5g-94N5g9NIfUvF1WCBlHiVjBmsPaz5rUnJYmhZK_5jxDAoj16xwvwBOQylcy1hhi-sSLNJ9CpUaeEzOTcPfYIuadYg-dYJrLVwOhp_SeavvQSWg5zW53IqagGMM0=&X-Bogus=DFSzsIjLsRxANxYXSBG2H2ybrU-M&_signature=_02B4Z6wo00001Rt1ViAAAIDAGZHDibe5t5kbdFqAACXa6a'
head={
	'Host': 'www.tiktok.com',
    'Cookie': f'ttwid=1%7Cf1d9mI-3uCgb1W1ykT_ZvVGVVmxnggmGJ2TkBooEM1k%7C1661640067%7C93e913e8da2b23fa8191b53285b5c75aa85c086ce9915dcfcf80d0668716758a; _abck=22E1C240F157DDF6067B25DFB9B821C1~-1~YAAQ7eRhXmikQNOCAQAAFDVx4QiizRkCSprAq7q712xoDhOdIGoB3p8ffdIWuO8ciqKc4stHuZWZqXOqrd0VaZGSUeRt4T72pyYavUx+kPx3aXCUyfc9TLFo6J7NEegMRFQyODmb4Qp6TH1YyvVIdXDKepUmR1FI8Z4LKdcKXDn+XR1EPNTjKCa0Z+dJvZfK01DCJDCtXhv30THgiZ815GTVWhJTncs7Z9BN908AOsSRkEGGnKGpdXuKkf471IU/LtRAYkPanGRZIcNA/77R2UjN35YdZS+HNCC+De083/ZpAoU8ufjvjUiBbqp6ZFy88WWqHjMBnVVQAHpVrPvtEqmd21A0op/Gi5NpLTLiMMFVn8MM38ZqpfNBesRsOnL5oWqmIh0gpaWXyQ==~-1~-1~-1; tt_csrf_token=NLIPKjMI-nbSZThQ8j7GKCRM5WbYhfW8b164; ak_bmsc=71CE99E70024BE1AC44C55AF33FA6051~000000000000000000000000000000~YAAQ7eRhXmmkQNOCAQAAFDVx4RCLUgdkaFbVjgatFH4RJ6iK4IwxjMMPgHl5Mw214f976BhDbxe0KL9k8lJSkZq37V4nGLnntDMqqO3FnQN3rSUnIZkc4L3ida4mn2w5BiRRMkrp6ikhW+Ynz4BzYfMR1WwEcdfsm0PnLQYBRz2FQKg0SO/ciEfcDk8S3OBxSWrVRj3QSDxH2DVxI1xP18WnqSo9JGM57xhh0mGlaMmexqbA9XQlFChgetFjJjDf7LggTSGH6wHtIFz/GNktAeww1ccnEmh8YJ8DYrSmtkreU7fzT4pQvfL0rURtrN1Gm1S4MvMbpG0SUjey+Vl8pOr0frdKdsQ4QkJsvZ10mAKPgx2gU5p/gORCz9cei/XNXKfG+tgeeiYfSg==; bm_sz=29169B1A00AF93E69A99EC87548A5BF1~YAAQ7eRhXmukQNOCAQAAFDVx4RBO2aK1snwE0si7+A9NXsWK4AMqJdKnUloLzLyehNfjAFJHIvADi90SqkRoXIRFcGysiopcTLM2MNbYcqqTyzoObd/M/wkr4j4is8m4Ny7dA943oCm0XG2aB/9tZ04dch04l1FVuY0eR3F6Lk1OBcWkjjTDfG58bx0kf57HCOeIFu6l9uPzcDW5Amc1HysA187WozFvL+zx1T/h2GUYRQmm508tKmlErJKFflYSZIOsG0oACB7WcQBWbWPVXdxZYKFyVIyTUsDlN3FRlvnbPR8=~3488048~4535876; __tea_cache_tokens_1988='+str('{%22_type_%22:%22default%22%2C%22user_unique_id%22:%227122424033622476290%22%2C%22timestamp%22:1661639613182}')+f'; msToken=p1ktJG5g-94N5g9NIfUvF1WCBlHiVjBmsPaz5rUnJYmhZK_5jxDAoj16xwvwBOQylcy1hhi-sSLNJ9CpUaeEzOTcPfYIuadYg-dYJrLVwOhp_SeavvQSWg5zW53IqagGMM0=; passport_csrf_token=13ece5f7e525190b87f121f3036fc2fa; passport_csrf_token_default=13ece5f7e525190b87f121f3036fc2fa; s_v_web_id=verify_l7chdt9a_7slNGyxb_mBhG_43Ss_8P7z_waU60HRLX7Az; odin_tt=9aaac22a189bc99416140a82f2e6c99f4f9358a4589f7268a9411482610a50a2c1830cc9edc40068681f8999c6f56e7ffc5b7682898df346d30c63f79f69db11edea5ab139964182f9d779f8dc47089d; cmpl_token=AgQQAPO_F-RO0rM0c6QIM104-LZ337Ba_4A0YMULRQ; sid_guard={sessionid}%7C1661640060%7C5184000%7CWed%2C+26-Oct-2022+22%3A41%3A00+GMT; uid_tt=45ac0a8230548d27c192f810cca59123e7516d2cb30dfe412bf79aa3373a7b35; uid_tt_ss=45ac0a8230548d27c192f810cca59123e7516d2cb30dfe412bf79aa3373a7b35; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; sid_ucp_v1=1.0.0-KGQ5NTE4NmVjOTNmODFiNGRkOTc2MGMxYTVlOGI2ZWFlMGI2ZDQ2MjAKIAiBiIaAuKCnhWMQ_LqqmAYYswsgDDCuuqqYBjgEQOoHEAMaBm1hbGl2YSIgM2E4OWZjMDVmZmE5ZWIwMDE0NTU3ODM4ZTcwODE4ZTI; ssid_ucp_v1=1.0.0-KGQ5NTE4NmVjOTNmODFiNGRkOTc2MGMxYTVlOGI2ZWFlMGI2ZDQ2MjAKIAiBiIaAuKCnhWMQ_LqqmAYYswsgDDCuuqqYBjgEQOoHEAMaBm1hbGl2YSIgM2E4OWZjMDVmZmE5ZWIwMDE0NTU3ODM4ZTcwODE4ZTI; store-idc=alisg; store-country-code=sa; store-country-code-src=uid; tt-target-idc=alisg; bm_mi=8721266FFF830EE6914F5EFBF78CEF65~YAAQR+9hXrbABKuCAQAApT134RDfQ4baEb8bnNXS/KNNWNTIqOyJgaUD1EVE+lnn7C2rrGr/PgJTlDuPQygBY4upimsYU16+BQGoKfMd3WBxOxIpbf/5bE9YgCefPTzmOSo+Cvh/L4dM0VI8mDzyncQMzcgOSUrpGEupbBoJQPsP4/T3e9ZUu/M3QqsYCcuYJlORQ1fd0wOSIVZK0l4CL8qIAWoC6EwSjO/nPX+TWGNaB6xGz4jEmlFUnCypJoCx4wMTE0PFBHXN3Ml8RdQktHwFSgxjt3VCRTu/jYKt3sVhO9btadhpZGCWF/hdW2D5YQ==~1; bm_sv=438FE55ABACB17E0A6955CE09337EE7A~YAAQR+9hXqHBBKuCAQAAkXh44RBIb88TfyRwyS6/EB2/K8eJM7NlwctG+X5BycuYu6vB8EGtgxnec+cJIXX4iNBUyt+U1hwLvERxeeMAHOTSV30V2CGsX5lTEnpshrxpu5On1fXAq6Igdaz1xy/GiAr5cz9QWEnUbQY3tkhaQKeib0eKhQdkPfFJEnFg/CV5oaI52YsjzzqupFHeJbNoF5uh2FhYCBh4kBDJWQuMxhw8yhmhTWUQEwZg4Vp4ave9~1; passport_fe_beating_status=true; msToken=UUtCDGTkkqECDgVUANqxDOoSl7CRf4sVk8QoMZppgkBeHqhl6JRWYCaRcNc0ZbXqnLZZHbEUWJh82qwhGUMyPtssQ8K5PSiFzidzAmTcql3ZHOCHYplV; csrf_session_id=5d701bf19a877a2a4e1e3fa86f69af93',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
	'Accept': '*/*',
	'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': f'https://www.tiktok.com/@{usr}/video/{postid}?is_copy_url=1&is_from_webapp=v1',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Tt-Csrf-Token': 'NLIPKjMI-nbSZThQ8j7GKCRM5WbYhfW8b164',
	'X-Secsdk-Csrf-Token': '000100000001ed7ea0f4b3ee19c8ae2faae5f4674ff0b30a6577f1647aabffea34b953bb1118170f54f0b3f589f3',
	'Origin': 'https://www.tiktok.com',
	'Content-Length': '0',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'Te': 'trailers'}
print('\n')
while True:
	sleep(6.6)#Sleep - time between sending comments
	req=post(url,headers=head)
	if 'Comment sent successfully' in req.text:
		print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}',end='')
		done+=1
	elif 'You sent the same comment too often.' in req.text:
		print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}',end='')
		error+=1
	elif "You're commenting too fast. Take a break!" in req.text:
		print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}',end='')
		error+=1
	elif 'Login expired' in req.text:exit(f'[!] Your session ID has been expired\nsession id [{sessionid}]')
	elif '{}' in req.text:exit(f'[!] Your session ID has been banned\nsession id [{sessionid}]')
	else:
		print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}',end='')
		error+=1

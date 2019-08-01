import quopri
from urllib import parse

s = 'href%3D"https://post.pinterest=\r\n.com/f/a/WRi5L7G_wfTW1BovkyUGuw~~/AAAAAQA~/RgRe6WEYPwRXCXBpbnRlcmVzdEIKABwY=\r\n3AZdrwvFllIXdHVyZ2VvbmNocmlzM0BnbWFpbC5jb21YBAAAAAA~?target=3Dhttps%3A%2F%2=\r\nFwww.pinterest.com%2Fsecure%2Fautologin%2F%3Fod%3DFux7G1fLpQxdgu%252FAlq7%2=\r\n52FO0wnXhG3mrIvODBVUav9ko5yjUdnc84zWzwWN%252BPJyxYElh86K0WCnm9Th%252F6kUWW%=\r\n252FfcKmC7yJz0qo50Ss4EaaUahZGfo19MQS%252BIeP4Dlvz0hgCjvxIS4R%252BPMAF%252FG=\r\nl9BpWrQ%253D%253D%26user_id%3DNjEwMDk3MjE4MTc4OTE0MjA0%26next%3D%252Fpin%25=\r\n2F806707351985179613%252F%253Futm_campaign%253Dpopular_pins%2526e_t%253De5a=\r\nb90da0abf493b944b3c27261acfe3%2526utm_content%253D806707351985179613%2526ut=\r\nm_source%253D31%2526utm_term%253D1%2526utm_medium%253D2012'
print(len(s))


ret = parse.unquote_plus(quopri.decodestring(s).decode('utf-8'))
'href="https://post.pinterest.com/f/a/WRi5L7G_wfTW1BovkyUGuw~~/AAAAAQA~/RgRe6WEYPwRXCXBpbnRlcmVzdEIKABwY3AZdrwvFllIXdHVyZ2VvbmNocmlzM0BnbWFpbC5jb21YBAAAAAA~?target=https://www.pinterest.com/secure/autologin/?od=Fux7G1fLpQxdgu%2FAlq7%2FO0wnXhG3mrIvODBVUav9ko5yjUdnc84zWzwWN%2BPJyxYElh86K0WCnm9Th%2F6kUWW%2FfcKmC7yJz0qo50Ss4EaaUahZGfo19MQS%2BIeP4Dlvz0hgCjvxIS4R%2BPMAF%2FGl9BpWrQ%3D%3D&user_id=NjEwMDk3MjE4MTc4OTE0MjA0&next=%2Fpin%2F806707351985179613%2F%3Futm_campaign%3Dpopular_pins%26e_t%3De5ab90da0abf493b944b3c27261acfe3%26utm_content%3D806707351985179613%26utm_source%3D31%26utm_term%3D1%26utm_medium%3D2012'
print(ret)
print(len(ret))

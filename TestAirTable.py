import requests
import json

def json_nodes(start_node, level=0):
    resData = json.loads(start_node)
    for key, value in resData.items():
        if isinstance(value,list) & (str(value) in ('{')):
            for strValue in value:
                try:
                    json1 = json.dumps(strValue, ensure_ascii=False)
                    print(json1)
                    json_nodes(json1,level+1)
                except:
                  print("  "*level, "NODE:",key,value)
        else:
           print("  "*level, "NODE:",key,value)
r = requests.get("https://api.airtable.com/v0/applwTUoGpAs8aP9G/%E5%85%A8%E6%B0%91%E5%81%A5%E5%BA%B7%E4%BF%9D%E9%9A%AA%E5%B1%85%E5%AE%B6%E9%86%AB%E7%99%82%E7%85%A7%E8%AD%B7%E6%95%B4%E5%90%88%E8%A8%88%E7%95%AB%E6%94%B6%E6%A1%88%E7%94%B3%E8%AB%8B%E6%9B%B8?api_key=keyAVb8xDNRtSTyDP")
resData = json.loads(r.content.decode('utf8'))
json1 = json.dumps(resData['records'][0]['fields'], ensure_ascii=False)
print(json1)
json_nodes(json1,0)




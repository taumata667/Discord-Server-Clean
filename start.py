import requests, sys, json

def startBombing(token):
    check = requests.post("https://discord.com/api/v9/invites/1", headers = {"Content-Type":"application/json", "Authorization": token}, data={})
    if check.status_code == 401:
        sys.exit("Please enter a valid token!")
    print("Token verified.")
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds",  headers = {"Content-Type":"application/json", "Authorization": token})
    for i in json.loads(guilds.text):
        requests.delete("https://discord.com/api/v9/users/@me/guilds/{}".format(i['id']), headers = {"Content-Type":"application/json", "Authorization": token})
    print("Exited from servers successfully.")

if __name__ == "__main__":
    f = open("config.json")
    config = json.loads(f.read())
    f.close()
    if config["token"] == None or len(config["token"]) != 59:
        sys.exit("Please enter a valid token!")
    startBombing(config["token"])

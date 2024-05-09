import requests

def obtner_info(dueno, repo):
    
    url = f"https://api.github.com/repos/{dueno}/{repo}"
    response = requests.get(url)
    
    if response.status_code == 200:
        repo_info = response.json()
        return repo_info
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}



dueno = "DavidReveloLuna"
repo = "Machine-Learning"
repo_info = obtner_info(dueno, repo)



if "error" in repo_info:
    print(repo_info["error"])
else:
    print(f"Nombre: {repo_info['name']}")
    print(f"Descripcion: {repo_info['description']}")
    print(f"Lenguaje principal: {repo_info['language']}")
    print(f"URL: {repo_info['html_url']}")
    
    
with open("repo_info.txt", "w", encoding="utf-8") as file:
    file.write(str(repo_info))


import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

#Explore information about the repositories
repo_dicts =response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

#Examin the first repostory.
#repo_dict = repo_dicts[0]

print("\nSelected information about first repository")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
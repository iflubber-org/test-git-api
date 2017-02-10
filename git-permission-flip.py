import requests
import json
import sys

#user = sys.argv[1]
#password = sys.argv[2]
permission = sys.argv[1]
org = sys.argv[2]

#access = ('%s' % (user),'%s' % (password))
headers = {'Authorization': 'token 58f9c157310c2a43232c1c1e74597e596194364b'}
payload = {'permission': '%s' % (permission)}

# Fetch all the teams under the organization
r = requests.get('https://api.github.com/orgs/%s/teams' % (org), headers=headers)
teams = json.loads(r.text)
for team in teams:
	# For each team Fetch all repositories
	r = requests.get('https://api.github.com/teams/%s/repos' % (team[u'id']), headers = headers)
	repos = json.loads(r.text)
	for repo in repos:
		# For each repository Change the team permission
		r = requests.put('https://api.github.com/teams/%s/repos/%s/%s' % (team[u'id'], org, repo[u'name']), headers = headers, data = json.dumps(payload))
exit()

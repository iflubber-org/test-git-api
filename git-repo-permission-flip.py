import requests
import json
import sys

permission = sys.argv[1]
repo = sys.argv[2]
owner = sys.argv[3]

headers = {'Authorization': 'token 58f9c157310c2a43232c1c1e74597e596194364b'}
payload = {'permission': '%s' % (permission)}

# Fetch all the collaborators for the repository
r = requests.get('https://api.github.com/repos/%s/%s/collaborators' % (owner,repo), headers=headers)
collaborators = json.loads(r.text)
for collaborator in collaborators:
	# For each collaborator, flip the permission
	r = requests.delete('https://api.github.com/repos/%s/%s/collaborators/%s' % (owner,repo, collaborator[u'login']), headers = headers)
	print(r.status_code)
	r = requests.put('https://api.github.com/repos/%s/%s/collaborators/%s' % (owner,repo,collaborator[u'login']), headers = headers, data=json.dumps(payload))
	print(r.status_code)
exit()

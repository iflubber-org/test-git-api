import requests
import json
import sys

permission = sys.argv[1]
org = sys.argv[2]

headers = {'Authorization': 'token 58f9c157310c2a43232c1c1e74597e596194364b', 'Accept' : 'application/vnd.github.korra-preview'}
parameters = {'affiliation': 'direct'}
payload = {'permission': '%s' % (permission)}

# Fetch all the repos under the organization
r = requests.get('https://api.github.com/orgs/%s/repos' % (org), headers=headers)
repos = json.loads(r.text)
for repo in repos:
	headers = {'Authorization': 'token 58f9c157310c2a43232c1c1e74597e596194364b', 'Accept' : 'application/vnd.github.korra-preview'}
	# For each repo Fetch all collaborators
	r = requests.get('https://api.github.com/repos/%s/%s/collaborators' % (org, repo[u'name']), headers = headers, params = parameters)
	collaborators = json.loads(r.text)
	for collaborator in collaborators:
		# For each collaborator change the  permission
		r = requests.put('https://api.github.com/repos/%s/%s/collaborators/%s' % (org, repo[u'name'], collaborator[u'login']), headers = headers, data = json.dumps(payload))
	# For each repo Fetch all invitations
	headers = {'Authorization': 'token 58f9c157310c2a43232c1c1e74597e596194364b', 'Accept': 'application/vnd.github.swamp-thing-preview+json'}
	r = requests.get('https://api.github.com/repositories/%s/invitations' % (repo[u'id']), headers=headers)
	invitations = json.loads(r.text)
	for invitation in invitations:
		# For each invitations change the permission
		if(permission == "push"):
			inv_p = "write"
		elif(permission == "pull"):
			inv_p = "read"
		r = requests.patch('https://api.github.com/repositories/%s/invitations/%s' % (repo[u'id'], invitation[u'id']), headers = headers, data = json.dumps({'permissions': '%s' % (inv_p)}))
exit()

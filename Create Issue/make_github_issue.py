#Got the syntax from https://gist.github.com/JeffPaine/3145490
#Modified Code.Works fine. Tested on Python version 3.6.5

import json
import requests

#Note: Replace 'Change' with the required input as it wants

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)


USERNAME = 'Change'
PASSWORD = 'Change'

# The repository to add this issue to
REPO_OWNER = 'Change'
REPO_NAME = 'Change'

def make_github_issue(title, body=None, assignee=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Your url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.session()
    session.auth=(USERNAME, PASSWORD)
    # Create your issue
    issue = {'title': title,
             'body': body,
             'assignee': assignee,
             'labels': labels}
    # Add the issue to your repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue ', title)
    else:
        print ('Could not create Issue ', title)
        print ('Response:', r.content)

make_github_issue('issue name', 'Body of Issue','assignee_name' , ['bug'])
#pass your parameters(issue name, body of issue and other details) above.

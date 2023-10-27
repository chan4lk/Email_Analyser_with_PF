# Email_Analyser_with_PF
Email analyser with AI and prompt flow

### Set up  dev environment

####Create Environment

`conda create --name pf python=3.9`
`conda activate pf`

Clone the Repo
`git clone https://github.com/glbdhananjaya/Email_Analyser_with_PF.git`

install its requirements.
`pip install -r requirements.txt`

###Set up config.json
```json
{
    "authorization_url": "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize",
    "graph_api_endpoint": "https://graph.microsoft.com/v1.0/users/{user_id}/messages",
    "user_id": "xxxxxxxxxxxxxxx",
    "client_id": "xxxxxxxxxxxxxx",
    "client_secret": "xxxxxxxxxxxxx",
    "redirect_uri": "http://localhost",
    "tenant_id": "xxxxxxxxxxxxxxxx",
    "access_token": "xxxxxxxxxxxxxxxxxxx"
}
```



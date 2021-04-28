## Instagram Clone

This project is an example for instagrame clone using **Flask** in **Python**

<p align="center">
  <img src="/app/static/images/favico/favicon-512x512.png" width=300 height=300 alt="Instagram Clone"/>
</p>

---
## Todo
1. Add Fulltext Search using `flask_whooshalchemy`
**Error :** `/venv/lib/python3.8/site-packages/flask_whooshalchemy.py`
`NameError: name 'unicode' is not defined`
---
### Before running
before running project there are some `env` variable you need to set


|  |  | 
| ---- | --- |
| MAIL_USERNAME | < Your E-Mail >  |   
| MAIL_PASSWORD | < Your E-Mail Password > |

Other than this you need to run a command in terminal

```BASH
flask db upgrade
```
This command should create a `Database/database.db` file in igclone folder

### Run App
To Run app you can simply type
```
flask run
```
and this will run this flask app at `localhost:5000` 

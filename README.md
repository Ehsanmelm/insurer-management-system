# insurer-management-system

### Admin
- Admin account can be created using createsuperuser command.
- After login, admin can view/update/delete insurer
- Can view/add/update/delete policy category 
- Can view/add/update/delete policy
- Can approve policy, applied by insurer
- Can answer customer question

### Insurer
- Create account 
- After login, can view all policy that are added by admin.
- If customer likes any policy, then they can apply for it.
- When customer will apply for any policy, it will go into pending status, admin can approve it.
- Customer can check status of his policy under history section
- Customer can ask question from admin.

- ---

## HOW TO RUN THIS PROJECT
- Open Terminal and Execute Following Commands :
```
python -m pip install -r requirements.txt
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/

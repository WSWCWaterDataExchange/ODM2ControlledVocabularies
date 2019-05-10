# WaDE Controlled Vocabularies

The source code for a Python/Django web application and REST API for managing the Water Data Exchange program (WaDE) Controlled Vocabularies. WaDE is part of the Western States Water Council programs.
 

The deployed online moderated registry at http://vocabulary.westernstateswater.org/ aims to promote consistent use of terminology (i.e., Controlled Vocabularies) to describe attributes of the Water Data Exchange(WaDE) project across the seventeen Western US States while they still retain the use of their native terms. The use of these controlled vocabularies allow interoperable data query across states and regional analysis. Click at the tables below to view their vocabularies. You may suggest edits to the existing vocabularies or suggest new ones to be added. Scroll to the bottom for more info on how to the registry works. 

## Deploy the app into a linux Ubuntu Server  
 
**Prerequisites**    
* Ubuntu Linux Server to host the app. Amazon AWS or Azure provide them.   
* [WinSCP](https://winscp.net/eng/index.php) to move the Excel Input file from Windowns into the Linux Server   
* [PuTTY](https://www.putty.org/) to execute linux commands from your windows   

 
**a. Install Basic packages/updates on the server**   
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install python-pip
sudo apt install ansible
```
**b. Clone the GitHub repo into the server**   
```
git clone https://WamdamProject/WaMDaM_ControlledVocabularies.git   
```

**C. Run ansible playbooks**   
```cd WaMDaM_ControlledVocabularies/ansible/```  

```ansible-playbook deploy.yml```  

*** D. Make sure three docker containers are up (wamdam1,wamdam1_db) **  
```
docker ps 
```

**F. Populate the DB**  
Use WinSCP to transfer the Excel file from your machien to the AWS server.  
```
sudo mv WaMDaM_CVs_Nov2018.xlsx spreadsheets
docker exec wamdam1 python manage.py reset_d
docker exec wamdam1 python manage.py populate_db /spreadsheets/WaMDaM_CVs_Nov2018.xlsx
```


**G. Uninstall and redeploy the app   
First stop the docker containers and remove after that  

```
docker stop wamdam1
docker stop wamdam1_db
docker rm wamdam1
docker rm wamdam1_db
```
Then deploy the app  
ansible-playbook deploy.yml  



### Licensing  
WaDE and materials in this GitHub repository are disturbed under a BSD 3-Clause [LICENSE](/LICENSE). 


### Credit 
The design of this registry is adapted from the source code of the ODM2 ControlledVocabularies available on GitHub @ github.com/ODM2/ODM2ControlledVocabularies. Thanks to Dr. Jeff Horsburgh and the ODM2 team for promoting #OpenScience by publishing their source code.


The adapted source code is available on GitHub @ https://github.com/WSWCWaterDataExchange/WaDEControlledVocabulary and includes detailed instructions on the changes made to the original repository and how to deploy, access, and populate the repository. The configuration and deployment of the original repository have been significantly changed to be much simplified and automated using Ansible and Docker. 


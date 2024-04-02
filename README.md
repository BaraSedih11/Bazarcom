<div align=center>
   
  ![Bazar com](https://github.com/BaraSedih11/Bazar.com/assets/98843912/8eabeccd-49dc-49c8-b5c7-2a78cdec461d)

   ![GitHub repo size](https://img.shields.io/github/repo-size/BaraSedih11/bazar.com) ![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/BaraSedih11/bazar.com) [![Python Version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)
[![Pip Version](https://img.shields.io/badge/pip-21.0-orange)](https://pypi.org/project/pip/21.0/)
 ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/BaraSedih11/bazar.com/main)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](https://github.com/BaraSedih/bazar.com/releases/tag/v1.0.0)
[![Contributors](https://img.shields.io/github/contributors/BaraSedih11/bazar.com)](https://github.com/BaraSedih11/bazar.com/graphs/contributors)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/BaraSedih11/bazar.com)
  
</div>
Welcome to Bazar.com! This repository contains the source code for a simple e-commerce website built with Flask and SQLite.

## About Bazar.com

Bazar.com is an online marketplace where users can browse and purchase a variety of products conveniently. Whether you're looking for electronics, fashion items, home decor, or more, Bazar.com has something for everyone.

## Features

- Get all books.
- Get book by ID.
- Get books by topic
- Purchase a book

## Technologies Used

- Python (Flask)
- SQLite
- Docker

## Getting Started

To get started with Bazar.com, follow these steps:

<ol>
   
   <li>Clone this repository to your local machine.</li>
   <li>To run the project using vscode terminal:
      <ul>
         <li>Install the required dependencies by running:</li>
         
   
   ```bash
   pip install -r requirements.txt
   ```
   
   <li>Uncomment the code for creating the database (from line 49 to 60):</li>
         
   ``` python
   with app.app_context():
       db.drop_all()
       db.create_all()
       book1 = Book(title='How to get a good grade in DOS in 40 minutes a day', topic="distributed_systems", price=10.99, quantity=100)
       book2 = Book(title='RPCs for Noobs', topic="distributed_systems", price=15.00, quantity=50)
       book3 = Book(title='Xen and the Art of Surviving Undergraduate School', topic="undergraduate_school", price=5.00, quantity=30)
       book4 = Book(title='Cooking for the Impatient Undergrad', topic="undergraduate_school", price=10.00, quantity=70)
       db.session.add(book1)
       db.session.add(book2)
       db.session.add(book3)
       db.session.add(book4)
       db.session.commit()
   ```
         
   <li>Start the catalog server:</li>
     
   ```bash
   python catalog/catalog.py
   ```
         
   Now the catalog server running on `http://0.0.0.0:5000`
         
   * If you need to run it another time you sould comment the code for database (from line 49 to 60) because it will recreate the database with the initial data.
   
   <li>Uncomment the code for creating the database (from line 49 to 51):</li>
   <li>Start the order server:</li>
   
   ``` bash
   python order/order.py
   ```
         
   Now the order server running on `http://0.0.0.0:6000`
         
   * If you need to run it another time you sould comment the code for database (from line 49 to 51) because it will recreate the database with the initial data.
         
   <li>Start the gateway server:</li>
     
   ```bash
   python start gateway/gateway.py
   ```

   Now the order server running on `http://0.0.0.0:5050`
      </ul>
   </li>

   <li> To run the project using docker to separate each service/server into separate docker container (Recomended):
      <ul>
         <li>Open powershell on your windows</li>
         <li>Heads towards your project (copy the path from vscode) then enter this command on powershell:</li>
        
   ``` bash
   cd 'path/to/project'
   ```
   
   <li>Now we need to build images for each one of the servers(make sure that docker server is running on your device):</li>
   
   * Build catalog image
   ```bash
   cd catalog
   docker build -t catalog_service .
   ```
   
   * Build order image
   ```bash
   cd ..
   cd order
   docker build -t order_service .
   ```
   
   * Build gateway image:
   ```bash
   cd ..
   cd gateway
   docker build -t gateway_service
   ```
   
   <li>Now you need to run each image on a separate powershell window:</li>
     
   ```bash
   docker run -it -p 5000:5000 catalog_service
   ```
   
   ```bash
   docker run -it -p 6000:6000 order_service
   ```
   
   ```bash
   docker run -it -p 5050:5050 gateway_service
   ```

   * Now you can send any request via the gateway and it will works well.
      </ul>
   </li>
</ol>

# Documentations
We've made postman documentation [here](https://documenter.getpostman.com/view/33323023/2sA35Ba439)

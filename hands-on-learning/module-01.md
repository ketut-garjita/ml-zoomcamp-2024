## Setting up the Environment
_Source_ : **https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/06-environment.md**

### Linux
- VMWare
- Linux Mint 21 (Ubuntu)
- Install Anaconda
  ```
  $ wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh
  ```
- Craeate envronment for course
  ```
  conda create -n ml-zoomcamp python=3.11
  ```
- Activate environment
  ```
  conda activate ml-zoomcamp
  ```
- Installing libraries
  ```
  conda install numpy pandas scikit-learn seaborn jupyter
  ```
  Later in the course you will also need to install XGBoost and Tensorflow, but we can skip this part for now.

### Cloud (AWS)
- [Creating an AWS account](https://mlbookcamp.com/article/aws)
- [Renting an ec2 instance](https://mlbookcamp.com/article/aws-ec2)

  <img width="140" alt="image" src="https://github.com/user-attachments/assets/7fbde986-a0b3-4500-b182-65d508b3126a">

  <img width="301" alt="image" src="https://github.com/user-attachments/assets/5d303557-207f-4a0e-8353-ddd4b972fe51">

  ![image](https://github.com/user-attachments/assets/c8fc2841-9845-4a50-9ad4-d627c3863c1d)

  
  <img width="674" alt="image" src="https://github.com/user-attachments/assets/695b90cc-d677-45f1-a92b-8e2575731ee7">
  


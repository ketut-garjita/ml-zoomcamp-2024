## Setting up the Environment
**https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/06-environment.md**

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
  
  

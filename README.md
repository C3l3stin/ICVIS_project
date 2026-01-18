# ICVIS_project
Here is the project of the Computer Vision course dealing with car plate recognition


## Setup Instructions
To set up the environment for this project, please follow the instructions below.
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/C3l3stin/ICVIS_project.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd ICVIS_project
    ```
3. **Install Required Libraries**:
    ```bash 
    pip install -r requirements.txt
    ```
4. **Download the dataset**: 
   Please download the dataset from [Kaggle - Car Number Plate Detection](https://www.kaggle.com/datasets/andrewmvd/car-number-plate-detection) and place it in the `data` directory.
   If the previous link doesn't work (the author may have deleted it), here is a wetransfer link to download the small dataset we used for the training of our model : [available until January 21st.](https://we.tl/t-lcmyvWkmNj) With this small dataset, please avoid to run the 4th cell, which aims to create it. 
5. **Run the Notebooks**: 
   Don't run the `yolov1_kaggle_run.ipynb` notebook : it is basically the version of our notebook `yolov1.ipynb`. We ran on kaggle with the gpu boost to load the hyperparameter tuning and training of our model. If you want to run the model without training it, you can download it and place it into a folder named `models` into your `notebooks` directory : [available until January 21st.](https://we.tl/t-bqUG4H7Eie) We also did a google colab version, with a pretrained model : `colab_yolo_v12ipynb`.


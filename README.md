# Fashion Multi-Label Attribute Classifier

This project uses a deep learning model to classify fashion product images into four attributes:
- **Color** of the product
- **Product Type** (e.g., T-shirt, Shoes, etc.)
- **Season** (e.g., Summer, Winter)
- **Gender** (Men, Women, Unisex)

The model is integrated into a simple web app using Flask, allowing users to upload images and receive predictions through a browser interface.

---

## How to Run the Project

### 1. Download the Complete Project Folder

The project (including the trained model and web app files) is too large for GitHub.  
Download the complete folder from the link below:

 **[Download Project Folder from Google Drive](https://drive.google.com/drive/folders/1ETmpZWLQIq4AJuJwXRj6VuH5vxRxwqQR?usp=sharing)**

Once downloaded, unzip the folder and open it.

---

### 2. Install Required Libraries:

Open Anaconda Prompt and run the following command
```bash
pip install -r requirements.txt
```
### 3. Run the Web Application:
After installing the dependencies run
``` bash
cd <Path of unzipped assignment folder>
```
and then run
```bash
python app.py
```
### 4. Upload an Image and Get Predictions
* Upload one of the sample fashion images (e.g., Amazon product screenshots provided in the folder).
* Click the Predict button.
* The model will return predictions for Color, Product Type, Season, and Gender.
 



# English - Hindi OCR Tool

This is a web-based OCR application that can extract text from images containing both Hindi and English text. It also allows for keyword search functionality, highlighting the specified keywords in the uploaded images.

## Requirements

- Python 3.x
- Streamlit
- Pillow
- pytesseract
- Tesseract OCR installed on your machine

## Setup Instructions

Follow the steps below to set up and run the project locally.

### 1. Fork the Repository

Fork this repository to your GitHub account by clicking the **Fork** button in the upper right corner of the GitHub page.

### 2. Clone Your Forked Repository

Clone the forked repository to your local machine and navigate into the project directory:

```bash
git clone https://github.com/your-username/ocr_project.git cd ocr_project
```

Replace `yourusername` with your actual GitHub username.


### 3. Create a Virtual Environment

Set up a virtual environment to manage the project dependencies:

```bash
python -m venv ocr_project
```

Activate the virtual environment:

- On macOS/Linux:

```bash
source ocr_project/bin/activate
```

- On Windows:

```bash
ocr_project\Scripts\activate
```

### 4. Install Dependencies

Install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install:

- `streamlit`: For building the web application.
- `Pillow`: For handling image uploads and processing.
- `pytesseract`: For performing OCR.

### 5. Install Tesseract OCR

Follow the instructions for your OS:

- **Windows:** [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki/Installation)
- **macOS:** You can install Tesseract using Homebrew:
  ```bash
  brew install tesseract
  ```
- **Linux:** You can install Tesseract using apt:
  ```bash
  sudo apt install tesseract-ocr
  ```

## Running the Application

1. Make sure your virtual environment is activated.
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open your web browser and navigate to `http://localhost:8501`.

## Features

- **Upload an Image**: Allows you to upload image files (JPG, PNG).
- **Extract Text**: Uses OCR to extract text in Hindi and English from the uploaded image.
- **Keyword Search**: Enter a keyword to search for its occurrences in the extracted text, with highlighted matches.

## Notes

- Ensure Tesseract is properly installed and added to your system's PATH for OCR functionality.
- For best results, provide clear images with visible text.

## Directory Structure

```
ocr_project/
│
├── app.py              # Main script for the Streamlit web application
├── ocr_utils.py        # Utility functions for OCR processing
├── requirements.txt    # Dependencies required for the project
└── README.md           # Instructions on how to run and deploy the project
```

- `app.py`: Contains the web application code for uploading images, performing OCR, and searching for keywords.
- `ocr_utils.py`: Contains functions for loading the OCR model and performing text extraction.
- `requirements.txt`: Lists all the libraries needed for the project.
- `README.md`: This instruction file.

## Deployment

To deploy this project, you can use Streamlit Cloud or Hugging Face Spaces.

### Deploying to Streamlit Cloud

1. Push the code to your GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Sign in with your GitHub account.
4. Select **Deploy an app** and connect your repository.
5. Choose the repository and branch that contains `app.py`.
6. Click **Deploy**.

Once deployed, the app will be accessible via a live URL provided by Streamlit Cloud.

### Deploying to Hugging Face Spaces

1. Create a Hugging Face account and a new Space.
2. Push your code to the Hugging Face repository.
3. Add the `requirements.txt` file to ensure all dependencies are installed.
4. Your application will automatically deploy on Hugging Face Spaces, and a live URL will be provided.

## Example Usage

1. **Upload Image**: Click the **Browse files** button to upload an image containing text in Hindi and/or English.
2. **Extract Text**: The application will use the OCR model to extract text from the image and display it on the screen.
3. **Keyword Search**: Enter a keyword in the search box to find its occurrences in the extracted text. The app will indicate whether the keyword was found or not.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
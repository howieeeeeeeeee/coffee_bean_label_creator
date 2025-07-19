# Coffee Bean Label Generator

## Project Goal & Overview

Welcome to my Coffee Bean Label Generator! This application is specifically designed for my home coffee roasting business, aiming to help me quickly and easily create beautiful, custom labels for my freshly roasted coffee beans.

Through this tool, users (which is me!) can input detailed information about a coffee bean, such as its origin, name, processing method, roast level, flavor notes, and even the roasting date. The backend server then composites this information onto a predefined label template and provides a downloadable PNG image.

## Key Features

*   **Custom Label Generation**: Dynamically generates unique coffee labels based on input bean information.
*   **Instant Preview**: Preview the generated label before downloading to ensure content and layout are as expected.
*   **Multiple Download Options**:
    *   Directly download the generated PNG label.
    *   Download the PNG label rotated by 90 degrees, useful for different packaging needs.
*   **Dynamic Origin Display**: Based on the selected origin, the label displays the corresponding Chinese origin name and a map icon.
*   **Responsive Web Design (RWD)**: The interface automatically adjusts to different screen sizes, providing a good user experience on both desktop and mobile.
*   **Multilingual Support**: The web interface is localized to Traditional Chinese for ease of use.

## Technologies Used

*   **Backend**:
    *   Python 3
    *   [Flask](https://flask.palletsprojects.com/): A lightweight web framework.
    *   [Pillow (PIL Fork)](https://python-pillow.org/): A powerful image processing library for label composition.
    *   [Gunicorn](https://gunicorn.org/): A Python WSGI HTTP Server for production deployment.
*   **Frontend**:
    *   HTML5
    *   CSS3 (Responsive Design)
    *   JavaScript
*   **Dependency Management**:
    *   [Pipenv](https://pipenv.pypa.io/en/latest/): Used for managing project Python dependencies and virtual environments.
*   **Deployment**:
    *   [Render](https://render.com/): Automated deployment using a `render.yaml` configuration file.

## Local Setup & Running

Please follow these steps to set up and run the application on your local machine:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/howieeeeeeeeee/coffee_bean_label_creator.git
    cd coffee_bean_label_creator
    ```

2.  **Prepare Image and Font Assets**:
    *   Place your blank label background image, named `template.png`, in the `static/` directory.
    *   Place your font files (e.g., `SourceHanSerifTW-Bold.otf`) in the `static/fonts/` directory.
    *   Place your origin map icons (e.g., `肯亞.png`, `衣索比亞.png`) in the `static/images/origins/` directory.
    *   **Important**: Ensure that the font file paths and image filenames in `app.py` match your actual file placements.

3.  **Install Dependencies**:
    Use Pipenv to install all necessary Python dependencies. This will create a virtual environment and install `Flask`, `Pillow`, `gunicorn`, etc.
    ```bash
    pipenv install --deploy --system
    ```

4.  **Run the Application**:
    Start the Flask development server. The application will run on `http://127.0.0.1:5001`.
    ```bash
    pipenv run python app.py
    ```

5.  **Access the Application**:
    Open `http://127.0.0.1:5001` in your web browser.

## Deployment to Render

This project is configured with a `render.yaml` file for easy deployment to the Render platform.

1.  **Create a Render Account**: If you don't have one, sign up at [Render.com](https://render.com/).
2.  **Connect Your Git Repository**:
    *   After logging into Render, click "New" -> "Web Service".
    *   Select your Git provider (e.g., GitHub) and connect your `coffee_bean_label_creator` repository.
3.  **Configure the Web Service**:
    *   Render will automatically detect the `render.yaml` file and pre-fill most settings.
    *   Ensure the **Root Directory** is set to the root of your repository.
    *   The **Build Command** should automatically be set to `pipenv install --deploy --system`.
    *   The **Start Command** should automatically be set to `gunicorn app:app`.
    *   Select the **Python 3** environment.
    *   Choose an appropriate **Instance Type**.
4.  **Create Web Service**: Click "Create Web Service" to start the deployment.

Render will automatically pull your code, install dependencies, and start the application. Once deployed, you'll get a public URL to access your Coffee Label Generator from anywhere!
# Inference Script

This script runs inference on an image using a specified model.

## Setup

1. **Create a virtual environment:**

    ```sh
    python -m venv roboflow
    ```

2. **Activate the virtual environment:**

    On macOS and Linux:
    ```sh
    source roboflow/bin/activate
    ```

    On Windows:
    ```sh
    .\venv\Scripts\activate
    ```

3. **Install the required package:**

    ```sh
    pip install inference
    ```

4. **Create a [.env](http://_vscodecontentref_/0) file with your Roboflow API key:**

    ```sh
    echo "ROBOFLOW_API_KEY=your_api_key_here" > .env
    ```

## Usage

Run the script with the path to the image file:

```sh
python testrobo.py /path/to/your/image.png
```

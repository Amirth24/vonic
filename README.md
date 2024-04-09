# Vonic: Video Captioning and Summarization Application

Vonic is a Python-based application built using Streamlit, designed to provide video captioning and summarization functionalities. It utilizes cutting-edge natural language processing models from Hugging Face and Google Generative AI to generate accurate captions and summaries for uploaded videos. With Vonic, users can easily obtain textual representations of video content, enabling better accessibility, searchability, and understanding.

## Features

- **Video Captioning**: Automatically generates captions for uploaded videos using Hugging Face's `openai/whisper-tiny.en` model.
- **Summarization**: Summarizes the generated captions using Google's Gemini, providing concise textual summaries of video content.
- **Downloadable Captions**: Allows users to download the generated captions in text format for future reference or integration into other applications.
- **User-Friendly Interface**: Streamlit provides an intuitive and interactive interface for easy navigation and usage of the application.
- **Customizable and Extendable**: Users can further customize and extend the application according to their specific needs and requirements.

## Installation

To run Vonic locally, follow these steps:

1. Clone the repository:

   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```
   cd vonic
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Export Google API Key:

   ```
   export GOOGLE_API_KEY=<your_google_api_key>
   ```

   Replace `<your_google_api_key>` with your actual Google Generative AI API Key obtained for the summarization task.

5. Run the application:

   ```
   streamlit run main.py
   ```

   The Streamlit server will start, and you can access the application by navigating to the URL provided in the terminal.

## Usage

1. Upload a Video: Click on the "Upload Video" button to select and upload a video file.
2. View Captions: Once the video is uploaded, captions will be automatically generated and displayed alongside the video.
3. Download Captions: Optionally, you can download the generated captions by clicking on the "Download Captions" button.
4. Summarize Captions: The application will summarize the generated captions using Google's Gemini API, providing concise summaries of the video content.
5. Explore Options: Feel free to explore additional options or features provided by the application interface.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- Streamlit
- Hugging Face Transformers
- Google Generative AI API Client

You can install these dependencies using pip and the `requirements.txt` file provided in the repository.

## Contributing

Contributions to Vonic are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [amirth300324@gmail.com](mailto:amirth300324@gmail.com).

Enjoy using Vonic for your video captioning and summarization needs!

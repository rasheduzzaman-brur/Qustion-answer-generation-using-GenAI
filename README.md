# Question-answer-generation-using-GenAI

## Bangla Data Question Generation with Gemini AI

### Overview

This project utilizes Google's GenerativeAI (Gemini Pro) to generate questions and answers from Bangla  data. By leveraging AI, this tool automates the process of creating questions and corresponding answers based on provided headings and descriptions of Bangladeshi  data.

### Requirements

- Python 3.x
- `dotenv` library
- `pandas` library
- `google.generativeai` library
- A Google API key for accessing Gemini Pro

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/bangla--question-generation.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Google API key by creating a `.env` file in the project root directory and adding your API key:

    ```makefile
    GOOGLE_API_KEY=your_google_api_key
    ```

### Usage

1. Place your data in a CSV file with columns for headings and descriptions.
2. Update the file path in the script to point to your CSV file.
3. Run the script:

    ```bash
    python generate_questions.py
    ```

4. The script will iterate through the provided Bangla  data, generate questions and answers using Gemini AI, and save the results in the output directory.

### Safety Settings

To ensure appropriate content generation, the script uses predefined safety settings to filter out harmful or inappropriate content.

### Output

Generated questions and answers are saved in individual text files in the output directory, with each file named `response_{index}.txt`.

### Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License.


# py-downloader 🚀

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Multi-threading](https://img.shields.io/badge/Multi--Threading-0078D7?style=for-the-badge&logo=threads&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

**py-downloader** is a Python-based command-line tool designed to download files from the web quickly and efficiently. It supports **multi-threading** for faster downloads and includes a **progress bar** to track download status. Whether you're downloading a single file or multiple files, **py-downloader** makes the process seamless and user-friendly.

---

## Features ✨

- **Multi-threading**: Download files faster using multiple threads.
- **Progress Bar**: Visualize download progress in real-time.
- **Lightweight**: Minimal dependencies and easy to use.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Resumable Downloads**: Supports resuming interrupted downloads.
- **Customizable**: Set the number of threads and output directory.
- **User-Friendly CLI**: Simple and intuitive command-line interface.

---

## Installation 🛠️

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/maziyar-redox/py-downloader.git
   cd py-downloader
   ```

2. **Install dependencies:**

    ```bash
   pip install -r requirements.txt
   ```

3. **Run the downloader:**

    ```bash
   python main.py --url <URL> --output <OUTPUT_DIRECTORY> --threads <NUM_THREADS>
   ```

## Usage 🖥️

### Basic Usage

**Download a single file:**

    ```bash
    python main.py --url https://example.com/file.zip --output ./downloads
    ```

### Advanced Usage

* **Download with multiple threads:**

    ```bash
    python main.py --url https://example.com/file.zip --output ./downloads --threads 8
    ```

* **Download multiple files:**

    ```bash
    python main.py --url https://example.com/file1.zip --url https://example.com/file2.zip --output ./downloads
    ```

* **Resume a failed download:**

    ```bash
    python main.py --url https://example.com/file.zip --output ./downloads --resume
    ```

### Command-Line Options

| Option         | Description | Default Value |
| -------------- | ----------------------------------------- | ----------------- |
| `--url`        | URL of the file to download               | Required          |
| `--output`     | Output directory for downloaded files     | Current directory |
| `--threads`    | Number of threads to use for downloading  | 4                 |
| `--resume`     | Resume a previously interrupted download  | False             |
| `--help`       | Show help message and exit                | N/A               |

## Example Workflow 🛠️

1. **Download a large file with 8 threads:**

   ```bash
   python main.py --url https://example.com/large-file.iso --output ./downloads --threads 8
   ```

2. **Download multiple files:**

    ```bash
   python main.py --url https://example.com/file1.zip --url https://example.com/file2.zip --output ./downloads
   ```

3. **Resume a failed download:**

    ```bash
   python main.py --url https://example.com/large-file.iso --output ./downloads --resume
   ```

## How It Works 🧠

* **Multi-threading:** The downloader splits the file into chunks and downloads each chunk simultaneously using multiple threads.

* **Progress Bar:** The `tqdm` library is used to display a real-time progress bar.

* **Resumable Downloads:** The downloader saves the state of each download, allowing you to resume interrupted downloads.

## Contributing 🤝

Contributions are welcome! Here’s how you can contribute:

1. Fork the repository.

2. Create a new branch (`git checkout -b feature/YourFeatureName`).

3. Commit your changes (`git commit -m 'Add some feature'`).

4. Push to the branch (`git push origin feature/YourFeatureName`).

5. Open a pull request.

Please ensure your code follows PEP 8 guidelines and includes appropriate documentation.

## License 📜

This project is licensed under the MIT License. See the [LICENCE](https://github.com/maziyar-redox/py-downloader/blob/master/LICENSE) file for details.

## Acknowledgments 🙏

* **Python:** For being an amazing programming language.

* **tqdm:** For providing a beautiful progress bar.

* **Requests:** For simplifying HTTP requests.

## Contact 📧

For questions, feedback, or suggestions, feel free to reach out:

* **Email:** [r6.acc.051@gmail.com](mailto:r6.acc.051@gmail.com)

* **GitHub:** [maziyar-redox](https://github.com/maziyar-redox)

Happy Downloading! 🎉
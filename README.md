#Quick, Write!

## Description

Quick, Write! is a neural network trained OCR model inspired by Google's Quick, Draw! With a given word, the neural network will try to guess the word you drew, so, take the challenge, how good is your hand writing on a mouse. Note, the application is not mobile compatable as of yet. Thi project is still in development. 

## How to run the program

The web app is still in development, but the program can also be run locally by following these steps. Please ensure you have pip installed on your machine. If you do not, please follow the instructions [here](https://pip.pypa.io/en/stable/installing/).

1. Clone this repository to your local machine:

```bash
git clone https://github.com/RajPandya737/Quick_Write.git
```

2. Change to the project directory:

```bash
cd Quick_Write
```

3. The project utilizes many libraries. Ensure you have all of them downloaded by running

```bash
pip install -r requirements.txt
```

4. Run the program, please read the usage part of this file before continuing:

```bash
python quickwrite/app.py
```

## Usage

If you are running it locally, make your way to http://localhost:8000 and play the game!

## Project Structure
The project consists of the following files inside of the Anisync Folder folder:

1. `app.py`: The main Python script.
2. `config.py`: Contains all constants used in the program.
3. `scan_text.py`: Performs the OCR
4. `scanned_image.py`: ScannedImage class used to manipulate the image for better OCR results
5. `static/css`: Contains CSS for each of the respective HTML files. The CSS is minified.
6. `static/images`: Contains all images used in the project.
7. `static/js`: Contains all the Javascript used in the project.
8. `static/drawing`: Contains the user drawing.
9. `templates`: Contains all HTML files used in the project.


## Credits
- **Google**: Idea is based on [Google's Quickdraw](https://quickdraw.withgoogle.com/)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

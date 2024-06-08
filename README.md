# Forest Fire Prediction

This project uses machine learning to predict the Fire Weather Index (FWI) based on various weather conditions and fire indices.

## Introduction

Forest fires are a significant environmental concern, and predicting them accurately can help in taking preventive measures. This project aims to predict the Fire Weather Index (FWI) using a Ridge regression model based on various weather parameters.

## Dataset

The dataset contains the following features:

1. **Date**: (DD/MM/YYYY) Day, month ('June' to 'September'), year (2012)
2. **Temp**: Temperature at noon (in Celsius degrees)
3. **RH**: Relative Humidity (in %)
4. **Ws**: Wind speed (in km/h)
5. **Rain**: Total rain (in mm)
6. **FFMC**: Fine Fuel Moisture Code index from the FWI system
7. **DMC**: Duff Moisture Code index from the FWI system
8. **DC**: Drought Code index from the FWI system
9. **ISI**: Initial Spread Index from the FWI system
10. **BUI**: Buildup Index from the FWI system
11. **FWI**: Fire Weather Index
12. **Classes**: Two classes - Fire and Not Fire
13. **Region**: Binary indicator for the region

## Features

The model uses the following features for prediction:
- Temperature
- Relative Humidity
- Wind Speed
- Rain
- FFMC
- DMC
- ISI
- Classes
- Region

## Installation

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/kindo-tk/forest_fire.git
    ```
2. **Navigate to project directory:**

    ```sh
    cd .\forest_fire\
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv .venv
    ```

3. **Activate the virtual environment:**

   ```sh
   .venv\Scripts\activate
   ```

5. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

6. **Run the Flask application:**

    ```sh
    python app.py
    ```

## Usage

1. Navigate to http://127.0.0.1:5000/ in your web browser.
2. Enter the required input parameters in the form.
3. Click on the **Predict** button to get the FWI prediction.

## Results

The model will output the predicted Fire Weather Index (FWI) based on the input parameters.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 
For any inquiries or feedback, please contact:

- <a href="https://www.linkedin.com/in/tufan-kundu-577945221/">Tufan Kundu (LinkedIn)</a>
- Email: tufan.kundu11@gmail.com
<hr>
<br>
<img src="https://github.com/kindo-tk/images/blob/main/forest_fire/homepage.png">
<img src = "https://github.com/kindo-tk/images/blob/main/forest_fire/result.png">

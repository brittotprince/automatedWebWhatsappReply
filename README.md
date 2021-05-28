<h1 align ="center"> Automated Web Whatsapp Reply </h1>

## Send out to whatsapp message to all missed call numbers

### Set up
* run 
    ```python
    python -m pip install selenium
    ```
* Download and unzip [chrome driver](https://chromedriver.chromium.org/) to same folder(if you're using different webdriver, please update the path)

### Steps to follow
* Get the required timeframe's call log as .csv file
* Put the CSV in same folder as source code
    * The expected Column names in CSV is
        * Phone numbers -> `Phone`
            * Eg: `+919400419216`
        * Call status -> `Type`
            * Eg: `Missed`
* Edit the message and run the program
* A 30s timeout is given in order to complete whatsapp web QR code scan
* 🎉Tada🎉 -> You can see the message being send out to the required nembers.


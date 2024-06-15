# Cookie Clicker Bot

This project is a simple bot that automates the clicking of the cookie in the popular game [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/). The bot uses Selenium WebDriver to interact with the web page.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python installed on your machine. If not, download and install it from [python.org](https://www.python.org/).
- You have Google Chrome installed on your machine.
- You have ChromeDriver installed. You can download it from [chromedriver.chromium.org](https://chromedriver.chromium.org/).

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/cookie-clicker-bot.git
    cd cookie-clicker-bot
    ```

2. Install the required Python packages:

    ```bash
    pip install selenium
    ```

3. Ensure that the ChromeDriver executable is in your PATH, or provide the path to the `webdriver.Chrome` constructor in the script.

## Usage

1. Open a terminal and navigate to the project directory.

2. Run the script:

    ```bash
    python cookie_clicker_bot.py
    ```

The bot will open the Cookie Clicker game in a new Chrome window, accept the cookies policy, switch the language to English, and start clicking the big cookie indefinitely.

- **Imports**: The script starts by importing the necessary modules from the Selenium package and the `time` module.

- **Chrome Options**: `chrome_options` is configured to ensure the browser does not close immediately after the script finishes.

- **Driver Initialization**: A new Chrome browser window is opened with `webdriver.Chrome()`.

- **Navigate to the Game**: The bot navigates to the Cookie Clicker game URL.

- **Wait for Page Load**: The script pauses for 3 seconds to ensure the page loads completely.

- **Accept Cookies**: The bot finds and clicks the "Accept Cookies" button.

- **Change Language**: The bot changes the language to English by locating the appropriate elements and clicking them.

- **Wait for Language Change**: Another pause to ensure the language change takes effect.

- **Find and Click Cookie**: The bot finds the big cookie by its ID and enters an infinite loop to keep clicking it.

- **Quit Driver**: This line (`driver.quit()`) will not be executed due to the infinite loop. It's there for good practice if you decide to add a breaking condition to the loop.
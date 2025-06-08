# Unit Testing using Gradle

This repository contains a base Java project enhanced with unit tests written using Gradle.

---

## 1 Team Members

This assignment was completed by the following team:

*   **Sagi Einav** ([sagieinav](https://github.com/sagieinav))
*   **Keren** ([GitHub Username 2] - Link to GitHub profile)


---

## 2 Project Structure

This project is based on a provided template repository. The key elements relevant to this assignment are:

*   `README.md`: This file, providing information about the project and how to run the tests.
*   `src/main/java/[package-path]/App.java`: Contains the core application code with functions to be tested.
*   `src/test/java/[package-path]/AppTest.java`: Contains the unit tests written for the functions in `App.java`.
*   `build.gradle`: The Gradle build file defining the project structure and dependencies.
*   `gradlew` / `gradlew.bat`: The Gradle wrapper scripts for running commands without a global Gradle installation.

---

## 3 Tests Overview

Each team member chose and wrote unit tests for 3 different functions from the `App.java` file. The tests are located in `src/test/java/[package-path]/AppTest.java`.

Below is a table detailing which member wrote tests for which functions, along with a brief description of the function or the tests' purpose.

| Function Name       | Author     | Description of Function/Tests |
| :------------------ | :--------- | :---------------------------- |
| `[Function Name 1]` | Sagi Einav |                               |
| `[Function Name 2]` | Sagi Einav |                               |
| `[Function Name 3]` | Sagi Einav |                               |
| `[Function Name 4]` | Keren      |                               |
| `[Function Name 5]` | Keren      |                               |
| `[Function Name 6]` | Keren      |                               |

---

## 4 Getting Started

To get this project set up and run the tests, follow these steps:

### 4.1 Prerequisites

*   A Unix-like operating system (Linux, macOS, or Windows with WSL).
*   `git` command-line tool installed.
*   **Java Development Kit (JDK)** installed (compatible version for the project).
*   (Optional but recommended) Gradle is not strictly necessary if using the wrapper (`gradlew`).

### 4.2 Cloning the Base Repository and Setting Up Your Repo

1.  **Create a new, empty Private Repository on GitHub.** Name it appropriately for this assignment (e.g., `assignment2-gradle-testing`). Do **NOT** initialize it with a README or license.
2.  Open your terminal.
3.  Create a new directory for the project and navigate into it:
    ```bash
    mkdir assignment2-gradle-testing
    cd assignment2-gradle-testing
    ```
4.  Clone the instructor's base project into the current directory:
    ```bash
    git clone https://github.com/TomCo2210/25B-10142-Gradle_UnitTesting_Assignment.git .
    ```
    *(The `.` at the end clones into the current, empty directory)*
5.  Remove the original remote origin (which points to the instructor's repo):
    ```bash
    git remote remove origin
    ```
6.  Add your newly created private repository as the new origin:
    ```bash
    git remote add origin https://github.com/your-username/your-repo.git
    ```
    *(Replace `https://github.com/your-username/your-repo.git` with the clone URL of the **private** repository you created in step 1).*
7.  Push the initial code to your new private repository:
    ```bash
    git push -u origin main # or master, depending on your repo's default branch name
    ```
    You will likely need to use a Personal Access Token (PAT) instead of your password when prompted for authentication.

### 4.3 Running the Tests

Once the project is cloned and set up, you can run all the unit tests using the Gradle wrapper.

1.  Ensure you are in the root directory of the project (the one containing `build.gradle` and `gradlew`).
2.  Run the Gradle `test` task:
    *   On Linux/macOS:
        ```bash
        ./gradlew test
        ```
    *   On Windows (using Command Prompt or PowerShell):
        ```bash
        gradlew test
        ```

The output in the terminal will show the progress and results of the tests (whether they passed or failed).

Detailed test reports (including which specific assertions passed/failed) are typically generated in HTML format. You can find these reports after running the tests in:

```
build/reports/tests/test/index.html
```

Open this `index.html` file in your web browser to view a detailed summary of the test execution.

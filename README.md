# obsidian-cs-knowledge-base
   
A public repository containing my personal Obsidian vault, focused on Computer Science education notes and materials.
## 1 Purpose
   
This repository serves as a public archive and knowledge base of my Computer Science education notes. It's shared to potentially benefit friends, other students or individuals interested in these topics.
## 2 Contents
**DISCLAIMER:** Most of the contents in this vault are written in Hebrew.
   
This repository contains the structure and content of my Obsidian vault, specifically related to Computer Science studies:
   
   -   📄 **Obsidian Notes:** Comprehensive notes, summaries, concepts, and materials compiled during my Computer Science education. The notes are organized by `Semester > Course Name > ...`. Courses currently included are:
       -   **Semester 1:**
           -   Computer Science Intro (Python)
           -   Calculus 1
           -   Linear Algebra 1
           -   Discrete Math
       -   **Semester 2:**
           -   Java OOP
           -   Comp Architecture
           -   Calculus 2
           -   Probability Intro
           -   Development Tools
   
*(This list will be updated as new courses are added).*
   
   -   📚 **Raw Materials/Documents:** Includes some original documents and materials provided by the college or lecturers.
> **Note on External Materials**
  These materials are included solely for personal reference and study purposes as part of my educational notes within this knowledge base. Their inclusion here does not grant any rights to reproduce, distribute, or publicly display them. Redistribution or public sharing of these specific external materials beyond cloning this repository for personal use may be subject to copyright restrictions from the original creators.
   
   
   -   ⚙️ **Obsidian Settings:** My personalized application settings stored in the `.obsidian` folder, including editor preferences, hotkeys, and appearance settings.
   
   -   🔌 **Obsidian Plugins:** All installed community plugins located within the `.obsidian/plugins` directory. These plugins enhance the functionality of the vault.
   
   -   🎨 **Obsidian CSS:** Custom CSS snippets used for styling the vault, located in the `.obsidian/snippets` directory or within the theme folder.
   
## 3 Getting Started
   
Make sure you have the following software installed:
   
   *   **Git:** Required to clone the repository.
       *   [Install Git](https://git-scm.com/downloads)
   *   **Obsidian:** The knowledge base is designed for use with Obsidian.
       *   [Install Obsidian](https://obsidian.md/download)
   
**You can use this vault in two primary ways**, depending on whether you want to regularly receive the latest updates from this repository.
   - **Option 1:** Clone and Sync with Updates (keep getting my updates)
   - **Option 2:** Forking the repository (clone and continue on your own)
For instructions on how to set-up and use this vault for your specific needs, please refer to one of the two sections below.
   
### 3.1 Option 1: Clone and Sync with Updates (Recommended for Collaboration)
   
This option is best if you want to **make your own additions and modifications to the vault while also being able to easily pull the latest notes and updates that I add**. This method treats this repository as an "upstream" source for shared notes.

##### Setting Up
1.  **Clone the repository:**
	Open your terminal or command prompt and run:
	   `git clone <your_forked_repo_url> <destination-folder>`
	   `cd <destination-folder>`
	Replace `<destination-folder>` with your desired path.
	
2.  **Add the original repository as an 'upstream' remote:**
	This step only needs to be done once after cloning. It sets up a reference to pull my updates.
	`git remote add upstream https://github.com/sagieinav/obsidian-cs-knowledge-base.git`
   
3.  **Open the Vault in Obsidian:**
	Launch Obsidian, click "Open folder as vault", and select the `<destination-folder>`. You may need to enable community plugins.
   
4.  **Make your own notes and modifications:**
	Use the vault in Obsidian as you normally would, adding or changing notes.

##### Using and Getting Latest Updates
Perform these steps every time you wanna fetch my latest updates and merge them with your current vault.
*BE EXTRA CAUTIOUS WHEN PERFOMING THESE STEPS, TO AVOID POTENTIAL DATA LOSS.*
   
5.  **Commit your changes:**
	Save your changes to your local Git history.
       `git add . # Stages all changes in the vault`
       `git commit -m "Add my personal notes and adjustments" # Use a descriptive message`
	*Always commit your local changes before pulling updates from upstream to avoid losing work and simplify conflict resolution.*
   
6.  **Get the latest updates from the original repository:**
	 When there are updates, fetch them:
       `git fetch upstream`
   
7.  **Merge the updates into your vault:**
    Integrate my fetched updates into your local branch.
       `git merge upstream/main # Assuming 'main' is the default branch name`

 *   If Git reports **merge conflicts**, you'll need to manually edit the affected files to resolve them, then stage (`git add <conflicted_file>`), and complete the merge (`git merge --continue`).
   
   
   By following steps 5 through 7 periodically, you can keep your personalized vault updated with the latest shared notes while preserving your own modifications.
   
### 3.2 Option 2: Forking the Repository (For a Personal Starting Point)
   
This option is suitable **if you simply want a copy of the vault** as a starting point for your *own* personal vault and **do not** intend to regularly sync with my future updates.
   
1.  **Fork the repository:** Go to `https://github.com/sagieinav/obsidian-cs-knowledge-base.git` on GitHub and click the "Fork" button. This creates a complete copy under your own GitHub account.
   
2.  **Clone *your* forked repository:** Clone the repository from *your* GitHub account URL.
       ```
       git clone <your_forked_repo_url> <destination-folder>
       cd <destination-folder>
       ```
       Replace `<your_forked_repo_url>` with the URL of *your* forked repository.
   
3.  **Open the Vault in Obsidian:**
       Launch Obsidian, click "Open folder as vault", and select the `<destination-folder>`. You may need to enable community plugins.
   
4.  **Use it as your personal vault:** You can now freely add, modify, and delete notes. Since this is your independent copy, you can commit and push changes to *your* remote repository (`origin` by default) without affecting my original one.
   
   **Note:** If you use this method, your fork is independent. Future updates I make to the original repository will **not** automatically appear in your forked copy. This method is simpler if you just want the content as a one-time download and starting point.

## 4 Vault Usage: Tips & Tricks
Here are some tips for using this vault and maximizing workflow: {to be added}
### 4.1 Most Useful Hotkeys
**Note:** The hotkeys in this section are written for MacOS keyboard layout, but they work the same for Windows, with the corresponding keys (⌘ = Ctrl, ⌥ = Alt, etc...)

These are some of the most useful and must-know hotkeys. You can see all hotkeys inside the app (Settings > Hotkeys)

- Open Command Palette: ⌘ + P
- Pin/unpin current tab: ⌥ + P
- Toggle edit/view mode: ⌘ + E
- Export to PDF: ⌘ + Shift + E
- Text formatting: same as any other app. ⌘ + B for **bold**, ⌘ + H for ==highlight==, etc...
- 
## 5 Contribution
   
   This repository is primarily maintained for my personal use and as a public archive. Therefore, Contributions in the form of Pull Requests are generally not expected.
   
   However, if you find errors, broken links, or have suggestions for improvement, feel free to open an issue on the GitHub repository.
## 6 License
   
   This project, specifically the notes and configuration files created by the repository owner, is licensed under the **MIT License**.
   
   You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the content covered by this license, provided you include the original copyright and permission notice.
   
   See the [LICENSE](LICENSE) file for the full text.
   
   **Note on External Materials:** As mentioned in the Contents section, some materials included are from external sources (e.g., college lecturers). These materials are included for personal educational context only and are not covered by the MIT License for redistribution. Please respect the original copyrights of these external materials.

---
   
   *This repository contains personal education notes and is shared publicly under the MIT License, with the understanding that some included external materials are subject to their original copyrights.*
# Task CLI

A command-line application for managing tasks. This application allows users to store, list, and search tasks, with each task containing an ID, title, and short description. Tasks are saved in a JSON file for persistence.

## Features

- Add new tasks with a title and description.
- List all existing tasks.
- Search for tasks by title or description.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd task-cli
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:

```
python src/cli.py
```

### Commands

- **Add a Task**
  ```
  python src/cli.py add "Task Title" "Task Description"
  ```

- **List Tasks**
  ```
  python src/cli.py list
  ```

- **Search Tasks**
  ```
  python src/cli.py search "search term"
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
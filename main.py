import os
import extensions  # Import the extensions module for file type definitions


class DownloadOrganizer:
    def __init__(self, downloads_folder):
        """
        Initializes the DownloadOrganizer with the path to the downloads folder.

        Parameters:
            downloads_folder (str): The path to the downloads folder to organize.
        """
        self.downloads_folder = downloads_folder
        # Create necessary folders and store their paths
        self.folder_paths = self.create_folders()

    def create_folders(self):
        """
        Creates folders for different file types if they do not already exist.

        Folders created:
            - Music
            - Images
            - Videos
            - Miscellaneous

        Returns:
            dict: A dictionary with folder names as keys and folder paths as values.
        """
        # Dictionary of folder names and their descriptions
        folders = {
            'Music': 'Music',
            'Images': 'Images',
            'Miscellaneous': 'Miscellaneous',
            'Videos': 'Videos'
        }

        # Create folder paths dynamically based on the downloads folder
        folder_paths = {name: os.path.join(self.downloads_folder, folder) for name, folder in folders.items()}

        # Loop through the folder paths and create directories if they do not exist
        for folder, path in folder_paths.items():
            if not os.path.exists(path):
                os.makedirs(path)  # Create the directory
                print(f"A {folder} folder has been created.")
            else:
                print(f"The {folder} folder already exists.")

        return folder_paths

    def move_files(self, current_path, folder_name, file):
        """
        Moves a file from its current location to the appropriate folder based on file type.

        Parameters:
            current_path (str): The current path of the file.
            folder_name (str): The name of the folder to move the file to.
            file (str): The name of the file to be moved.
        """
        # Construct the new file path in the specified folder
        new_path = os.path.join(self.folder_paths[folder_name], file)

        # Move the file from current_path to new_path
        os.replace(current_path, new_path)
        print(f"Moved a file to the {folder_name}.")

    def find_files(self):
        """
        Scans the downloads folder for files and organizes them into respective folders
        based on their file extensions.
        """
        # Iterate through all files in the downloads folder
        for file in os.listdir(self.downloads_folder):
            # Construct the full file path
            file_path = os.path.join(self.downloads_folder, file)

            # Skip hidden files and directories
            if not file.startswith('.') and not os.path.isdir(file_path):
                # Determine the type of file based on its extension and move it to the correct folder
                if file.endswith(extensions.music_ext):
                    print(f"A music file has been found: {file}")
                    self.move_files(file_path, "Music", file)
                elif file.endswith(extensions.video_ext):
                    print(f"A video file has been found: {file}")
                    self.move_files(file_path, "Videos", file)
                elif file.endswith(extensions.image_ext):
                    print(f"An image file has been found: {file}")
                    self.move_files(file_path, "Images", file)
                else:
                    print(f"A miscellaneous file has been found: {file}")
                    self.move_files(file_path, "Miscellaneous", file)


# Usage Example
downloads_folder = '/Users/raioneru/Downloads'  # Define the path to the downloads folder
organizer = DownloadOrganizer(downloads_folder)  # Create an instance of the DownloadOrganizer
organizer.find_files()  # Start the process of finding and organizing files

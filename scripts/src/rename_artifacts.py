import pandas as pd
import subprocess
import json
import os

def load_toc(file_path:str) -> pd.DataFrame:
    toc = pd.read_csv(file_path)
    return toc

def get_directory_artifacts(directory_path:str) -> list:
    artifacts = os.listdir(directory_path)
    return artifacts

def is_md_file(artifact_path:str) -> bool:
    extension = artifact_path.split('.')[-1:]
    return extension[0] == 'md'

def remove_auto_generated_id(artifact_path:str, is_directory:bool) -> None:
    # Since we want to remove the last, auto generated, part of the name of artifacts we need to split by the white espaces, remove the last one (which
    # is the trash we want to remove) and joint the path again. If a file, however, we need to add back the extension. Furthermore, if not an md file or dir,
    # there is no trash to remove

    if (not is_directory and not is_md_file(artifact_path)):
        return

    parsed_name = artifact_path.split(' ')[:-1]
    parsed_name = ''.join(parsed_name)
    
    if not is_directory:
        extension = artifact_path.split('.')[-1:][0]
        parsed_name = parsed_name + '.' + extension

    print('SRC:', artifact_path)
    # print(os.path.isfile(artifact_path))
    # exit(1)

    # os.rename(artifact_path, parsed_name)
    subprocess.run(['mv', '{path}'.format(path=artifact_path), '"{path}"'.format(path=parsed_name)])

def is_dot_file(file_name:str) -> bool:
    return file_name[0] == '.'

def remove_auto_generated_id_from_artifacts(parent_directory: str, recursive: bool = False) -> None:
    artifacts = get_directory_artifacts(parent_directory)
    
    for artifact_path in artifacts:
        
        # Since there might me dot files due to pandoc and git, skip if encountered
        if is_dot_file(artifact_path):
            continue

        # Since we might have multiple nasted directories with the auto-generated id, check if the user wants it to recursively clean all files and dir
        artifact_path = os.path.join(parent_directory, artifact_path)
        is_directory = os.path.isdir(artifact_path)

        if  is_directory and recursive:
            remove_auto_generated_id_from_artifacts(artifact_path, recursive)

        remove_auto_generated_id(artifact_path, is_directory)

if __name__ == '__main__':

    # TOC_PATH = '/Users/pedrocruz/Documents/Develop/notion_backup/EM/EM306 - Estática 1800016dc2a34f39a0fff77b4c78bcdb/Tópicos d9630f1672154eb1ac4456a681109ada.csv'
    # NOTES_PATH = '/Users/pedrocruz/Documents/Develop/notion_backup/EM/EM306 - Estática 1800016dc2a34f39a0fff77b4c78bcdb/Tópicos d9630f1672154eb1ac4456a681109ada'


    NOTES_PATH = '/Users/pedrocruz/Desktop/notes'
    remove_auto_generated_id_from_artifacts(NOTES_PATH, recursive=True)

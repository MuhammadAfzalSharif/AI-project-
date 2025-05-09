
import os.path

from utils.converter import Converter
from utils.printer import Printer

class FileManager:

    # class attribute
    world: list = []

    #Check if a file exist
    def __file_exist(file_name:str) -> bool:
        return os.path.isfile(file_name)

    #Read the information from a plain text file by generating a list of strings
    #with each row of the file
    def __read(file_name) -> None:

        if FileManager.__file_exist(file_name):           
            with open(file_name, "r") as file:
                __class__.world = file.readlines()
                file.close()
                Printer.showMessage(f"File read successfully!")
                
        else:
            Printer.showMessage(f"The file {file_name} does not exist!")
        
        

    #Return the value of property world
    def getOutput() -> list:
        return __class__.world

    def uploadFile(file_name) -> None:
        FileManager.__read(file_name)
        Converter.removeCharacterInEachRow(__class__.world,'\n')
        Converter.transEachRowInListOfIntegers(__class__.world)
 

       
      
     
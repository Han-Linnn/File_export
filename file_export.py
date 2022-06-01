#!/usr/bin/env python3
import os

def file_export()->str:
	os.system("cp /data/train.csv ../data")
	os.system("cp /data/test.csv ../data")
	return 'data files have been automatically moved to file system'
	
if __name__ == "__main__":
    command = sys.argv[1]

    functions = {
        "file_export": file_export,
    }
    
    output = functions[command]()
    print(yaml.dump({"output": output}))
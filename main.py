import os
import zipfile

def zipFiles(path):
    projectPath = os.path.abspath(path)
    print("Project path: " + projectPath)
    for folder in os.listdir(projectPath):
        #print(folder)
        zipf = zipfile.ZipFile('{0}.zip'.format(os.path.join(projectPath, folder)), 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(os.path.join(projectPath, folder)):
            for filename in files:
                zipf.write(os.path.abspath(os.path.join(root, filename)), arcname=filename)
        zipf.close()

if __name__== "__main__":
    zipf = zipFiles("test-files")
import os

from pykwalify.core import Core
import yaml


schemaFile = "schema.yaml"

def main():
    for root, _, files in os.walk("../data"):
        for f in files:
            filename = os.path.join(root, f)
            checkFile(filename)


def checkFile(filename):
    with open(filename, 'r') as file:
        contents = yaml.load_all(file)
        for i, doc in enumerate(contents):
            c = Core(source_data=doc, schema_files=[schemaFile])
            
            print("{} ({})".format(filename, i))
            c.validate(raise_exception=False)


if __name__== "__main__":
    main()
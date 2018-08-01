import os

def producer(top_dir):
    print(top_dir)
    files = os.listdir(top_dir)
    for f in files:
        filepath = os.path.join(top_dir, f)
        if os.path.isdir(filepath):
            producer(filepath)

def main():
    producer('testdata')

if __name__ == "__main__":
    main()

import os

SENTENCE = "I have said no two million times this week and you still ask. Effective immediately, I am saying no to this job too."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")

if __name__ == "__main__":
    main()

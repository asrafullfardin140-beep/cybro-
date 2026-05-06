import sys

def main():
    try:
        with open("old_portfolio.txt", "r") as f:
            old_portfolio_html = f.read()
    except FileNotFoundError:
        print("old_portfolio.txt not found!")
        return

    with open("index.html", "r") as f:
        lines = f.readlines()

    start_idx = -1
    end_idx = -1

    for i, line in enumerate(lines):
        if "<!-- ═══════════════════ FEATURED PROJECTS (BENTO BOX)" in line:
            start_idx = i
        if start_idx != -1 and "</section>" in line:
            # We want to make sure it's the end of the section
            # Looking at the code we put in, the first </section> after start_idx is the end of the bento box.
            end_idx = i
            break

    if start_idx != -1 and end_idx != -1:
        new_lines = lines[:start_idx] + [old_portfolio_html + "\n"] + lines[end_idx+1:]
        with open("index.html", "w") as f:
            f.writelines(new_lines)
        print("Reverted index.html successfully.")
    else:
        print(f"FAILED to find boundaries. Start: {start_idx}, End: {end_idx}")

if __name__ == "__main__":
    main()

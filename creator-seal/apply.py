# Swaps the creator seal block in an HTML file for the combined
# Mohave Technology Group plus Pajamastan seal, or adds it before </body>.
import sys

block = open(sys.argv[1]).read().strip("\n")
path = sys.argv[2]
page = open(path).read()

mark = page.find("CREATOR SEAL")
if mark != -1 and "END CREATOR SEAL" in page:
    start = page.rfind("<!--", 0, mark)
    start = page.rfind("\n", 0, start) + 1
    end_mark = page.find("END CREATOR SEAL", mark)
    end = page.find("\n", end_mark)
    end = len(page) if end == -1 else end
    page = page[:start] + block + page[end:]
    print("swapped", path)
else:
    at = page.lower().rfind("</body>")
    if at == -1:
        print("skipped, no body tag", path)
        sys.exit(0)
    page = page[:at] + block + "\n" + page[at:]
    print("added", path)

open(path, "w").write(page)

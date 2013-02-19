"""
Builds the version of typeahead.js that's in vendor/typeahead.js and
packages it as a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "0.8.0"


def cp(src):
    cmd = [
        "cp -R vendor/typeahead.js/%s typeaheadjs/static/typeaheadjs/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "build": "grunt build",
        "version": DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./jquery/static/jquery"], shell=True)
    subprocess.call(
            ["cd vendor/typeahead.js && %(build)s" % args],
            shell=True)
    cp("dist/*")
    cp("LICENSE")

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()

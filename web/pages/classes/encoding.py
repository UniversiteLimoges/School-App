# Encoding solution
def encodingUTF8():
    import sys
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
    print("Content-type: text/html; charset=utf-8\n")
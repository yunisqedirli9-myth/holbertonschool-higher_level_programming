#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Modulun içindəki bütün adları alırıq
    names = dir(hidden_4)
    
    # Adları əlifba sırası ilə düzürük və filtrləyirik
    for name in sorted(names):
        if not name.startswith("__"):
            print("{}".format(name))

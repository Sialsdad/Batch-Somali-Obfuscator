from random import randint
import random, codecs, string, os, time

try:
    from pystyle import *
except:
    os.system("python -m pip install pystyle")
    from pystyle import *

try:
    from tqdm import tqdm
except:
    os.system("python -m pip install tqdm")
    from tqdm import tqdm

try:
    import colorama
except ImportError:
    os.system("python -m pip install colorama")
    import colorama
colorama.deinit()

__author__ = 'K.Dot#0001'

code = r"""
@echo off
set "n=a" && set "o=b" && set "p=c" && set "q=d" && set "r=e" && set "s=f" && set "t=g" && set "u=h" && set "v=i" && set "w=j" && set "x=k" && set "y=l" && set "z=m" && set "a=n" && set "b=o" && set "c=p" && set "d=q" && set "e=r" && set "f=s" && set "g=t" && set "h=u" && set "i=v" && set "j=w" && set "k=x" && set "l=y" && set "m=z" && set "N1=A" && set "O1=B" && set "P1=C" && set "Q1=D" && set "R1=E" && set "S1=F" && set "T1=G" && set "U1=H" && set "V1=I" && set "W1=J" && set "X1=K" && set "Y1=L" && set "Z1=M" && set "A1=N" && set "B1=O" && set "C1=P" && set "D1=Q" && set "E1=R" && set "F1=S" && set "G1=T" && set "H1=U" && set "I1=V" && set "J1=W" && set "K1=X" && set "L1=Y" && set "M1=Z"
chcp 65001 > nul
"""
if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31':
    os._exit(0)
banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#4044\n\n
""")

options = """
[1] Level 1 (Recommended to use AFTER 2)
[2] Level 2
[3] Level 3
[clean] cleans the code to try and fix any common errors
[all] does 1, 2, 3 and clean
[fud] makes it undetectable by everything on virustotal
[ultimate] The Ultimate batch obfuscation (nowhere near done... but beta out now.)\n
"""


class Main:
    def __init__(self):
        print(Colorate.Vertical(Colors.yellow_to_red, banner, 2))
        self.carrot = False
        self.label = False
        self.file = Write.Input("File to obfuscate -> ", Colors.rainbow, interval=0.05)
        if os.path.exists(self.file):
            print(Colorate.Vertical(Colors.yellow_to_red, options, 2))
            self.level = Write.Input("What level of Obfuscation do you want? -> ", Colors.rainbow, interval=0.05)
            if self.level == "1":
                self.level1()
            elif self.level == "2":
                self.level2()
            elif self.level == "3":
                self.level3()
            elif self.level == "clean":
                self.clean()
            elif self.level == "all":
                self.all()
            elif self.level == "fud":
                self.fud()
            elif self.level == "ultimate":
                self.ultimate()
            else:
                print("Invalid option")
                time.sleep(3)
                Main()
        else:
            print(Colors.red + "That file does not exist!" + Colors.reset)
            time.sleep(3)
            Main()
            
    def make_random_string(self):
        length = randint(5, 8)
        return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZḆḞԍǏƘԸɌȚЦѠƳȤѧćễļṃŉᵲừŵź☠☢☣卐") for i in range(length))
            
    def level1(self):
        carrot = False
        var = False
        BYPASS = False
        try:
            os.remove(f"{self.file}.level1.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.level1.bat", "a+", encoding="utf-8") as f:
            f.write(code)
            for line in tqdm(data, desc="Obfuscating", unit=" lines", colour="green", ascii=True):
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if BYPASS == True:
                        if char == "}":
                            BYPASS = False
                            pass
                        else:
                            f.write(char)
                    else:
                        if char == "{":
                            BYPASS = True
                            pass
                        elif char == ">":
                            f.write(char)
                        elif char == "^":
                            f.write(char)
                            carrot = True
                        elif carrot == True:
                            f.write(char)
                            carrot = False
                        else:
                            if char == "%":
                                var = not var
                                f.write(char)

                            elif var == True:
                                f.write(char)

                            elif "\n" in char:
                                f.write(char)

                            else:
                                random = self.make_random_string()
                                if char in string.ascii_letters:
                                    if char.islower():
                                        coded0 = codecs.encode(char, 'rot_13')
                                        coded = coded0.replace(coded0, f"%{coded0}%")
                                        f.write(f"{coded}%{random}%")
                                    else:
                                        coded0 = codecs.encode(char, 'rot_13').upper()
                                        coded = coded0.replace(coded0, f'%{coded0}1%')
                                        f.write(f"{coded}%{random}%")
                                else:
                                    f.write(f"{char}%{random}%")
                                
    def level2(self):
        characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        random_order = ''.join(random.sample(characters, len(characters)))
        carrot = False
        var = False
        BYPASS = False
        try:
            os.remove(f"{self.file}.level2.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.level2.bat", "a+", encoding="utf-8") as f:
            f.write(f"set KDOT={random_order}\nchcp 65001 > nul\n")
            for line in tqdm(data, desc="Obfuscating", unit=" lines", colour="green", ascii=True):
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if BYPASS == True:
                        if char == "}":
                            BYPASS = False
                            pass
                        else:
                            f.write(char)
                    else:
                        if char == "{":
                            BYPASS = True
                            pass
                        elif char == ">":
                            f.write(char)
                        elif char == "^":
                            f.write(char)
                            carrot = True
                        elif carrot == True:
                            f.write(char)
                            carrot = False
                        else:
                            if char == "%":
                                var = not var
                                f.write(char)

                            elif var == True:
                                f.write(char)

                            elif "\n" in char:
                                f.write(char)

                            else:
                                if char in string.ascii_letters:
                                    var = f"%KDOT:~{random_order.index(char)},1%"
                                    f.write(var)
                                else:
                                    f.write(char)
                                
    def level3(self):
        out_hex = []

        #lowkey overkill lmao
        out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
        with open(f'{self.file}','rb') as f:
                penis = f.read()

        out_hex.extend(['{:02X}'.format(b) for b in penis])

        with open(f'{self.file}.level3.bat', 'wb') as f:
            for i in out_hex:
                f.write(bytes.fromhex(i))
                
    def clean(self):
        with open(self.file, 'r', encoding="utf-8") as f:
            contents = f.read()
        with open(f'{self.file}.cleaned.bat', 'a+', encoding="utf-8") as f:
            contents.replace("%~f0%", "%~f0")
            contents.replace("%~dp0%", "%~dp0")
            contents.replace("%~dpn0%", "%~dpn0")
            contents.replace("%~dpnx0", "%~dpnx0")
            f.write(contents)
            
    def all(self):
        names = []
        self.level2()
        self.file = f"{self.file}.level2.bat"
        names.append(self.file)
        self.level1()
        self.file = f"{self.file}.level1.bat"
        names.append(self.file)
        self.clean()
        self.file = f"{self.file}.cleaned.bat"
        names.append(self.file)
        self.level3()
        os.rename(f"{self.file}.level3.bat", "FINAL.bat")
        for name in names:
            os.remove(name)
        print("FINAL.bat is the finished product!")
        time.sleep(5)
        os._exit(0)
        
    def fud(self):
        carrot = False
        var = False
        BYPASS = False
        try:
            os.remove(f"{self.file}.fud.bat")
        except:
            pass
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.fud.bat", "a+", encoding="utf-8") as f:
            f.write("::Made by K.Dot\n")
            for line in tqdm(data, desc="Obfuscating", unit=" lines", colour="green", ascii=True):
                if line.startswith(":") and not line.startswith("::"):
                    f.write(line)
                    continue
                for char in line:
                    if BYPASS == True:
                        if char == "}":
                            BYPASS = False
                            pass
                        else:
                            f.write(char)
                    else:
                        if char == "{":
                            BYPASS = True
                            pass
                        elif char == ">":
                            f.write(char)
                        elif char == "^":
                            f.write(char)
                            carrot = True
                        elif carrot == True:
                            f.write(char)
                            carrot = False
                        else:
                            if char == "%":
                                var = not var
                                f.write(char)

                            elif var == True:
                                f.write(char)

                            elif "\n" in char:
                                f.write(char)

                            else:
                                random = self.make_random_string()
                                f.write(f"{char}%{random}%")
                            
    def ultimate(self) -> None:
        #ultimate mode
        BYPASS = False
        with open(self.file, "r", encoding="utf-8") as f:
            data = f.readlines()
        with open(f"{self.file}.ultimate.bat", "a+", encoding="utf-8") as f:
            f.write("::Made by K.Dot\n")
            f.write(code)
            characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            random_order = ''.join(random.sample(characters, len(characters)))
            f.write(f"set KDOT={random_order}\n")
            for line in tqdm(data, desc="Obfuscating", unit=" lines", colour="green", ascii=True):
                random_bool = random.choice([True, False])
                if line.startswith("{"):
                    BYPASS = True
                    for char in line:
                        if char == "}":
                            BYPASS = False
                            pass
                        else:
                            if len(char) == 1:
                                pass
                            else:
                                f.write(char)
                elif line.startswith("::"):
                    f.write(line)
                    continue
                elif line.startswith(":"):
                    f.write(line)
                    continue
                else:
                    if random_bool == True:
                        f.write(";")
                    for word in line.split():
                        if word.startswith("%"):
                            f.write(word + " ")
                            continue
                        else:
                            for char in word:
                                if char == '\n':
                                    f.write('\n')
                                    continue
                                elif char == ' ':
                                    f.write(' ')
                                    continue
                                else:
                                    random_obf = [self.ran1(char), self.ran2(char, random_order), self.ran3(char), self.ran4(char)]
                                    f.write(f"{random.choice(random_obf)}")
                            f.write(' ')
                    f.write('\n')

    def ran1(self, char):
        random = self.make_random_string()
        if char in string.ascii_letters:
            if char.islower():
                coded0 = codecs.encode(char, 'rot_13')
                coded = coded0.replace(coded0, f"%{coded0}%")
                return f"{coded}%{random}%"
            else:
                coded0 = codecs.encode(char, 'rot_13').upper()
                coded = coded0.replace(coded0, f'%{coded0}1%')
                return f"{coded}%{random}%"
        else:
            return f"{char}%{random}%"
        
    def ran2(self, char, random_order):
        public = r"C:\Users\Public"
        weird = r"C:\Program Files (x86)\Common Files"
        if char in public:
            return f"%public:~{public.index(char)},1%"
        elif char in weird:
            return f"%CommonProgramFiles(x86):~{weird.index(char)},1%"
        else:
            if char in string.ascii_letters:
                var = f"%KDOT:~{random_order.index(char)},1%"
                return var
            else:
                return char
    
    def ran3(self, char):
        if char in string.ascii_letters:
            escape = '^'
            return f"{escape}{char}"
        else:
            return char
        
    def ran4(self, char):
        return char
    
    def true_statement(self, line):
        true_statements = ["if exist C:\Windows\System32 ( {} )", "if not 0 neq 0 ( {} )"]
        random_statement = random.choice(true_statements)
        return random_statement.format(line)
    
    def obliterate(self):
        #The best obfuscation method involving encoding
        #I ain't nowhere near done with this yet :skull:
        #(it does work tho stg | and its op asf)
        pass

if __name__ == "__main__":
    Main()
    print("Done!")
    more = Write.Input("Do you want to obfuscate another file? (y/n): ", Colors.rainbow, interval=0.05)
    if more.lower() == "y":
        os.system("cls")
        Main()
    else:
        time.sleep(3)
        os._exit(0)

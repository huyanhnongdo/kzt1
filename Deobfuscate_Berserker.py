import os, sys, re
import subprocess
  
def write(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()


if __name__ == "__main__":

    obf_file1 = 1# obfuscated file

    with open(input("Input File Enc(Để chung vs tool): ")) as code:
        data = code.read()
        
        s1 = re.search("if self.(.+?) in open", data).group(1)
        s1s = s1.replace("15", "12")
        s2 = re.findall("{(.+?)}", data)

        source = (
            data.replace(s1, s1s)
            .replace("{" + s2[0] + "}", "print")
            .replace(",{" + s2[1] + "}()", "")
        )
        write('tmpfile.py', source)
        
        print("Chờ Đợi!")
        try:
            os.system(f"python tmpfile.py > decbyhuykazuto.py")
        except:
            exit('Sorry, Tool này k hợp vs bạn=)))')
        print(f"Xog lưu file decbyhuykazuto.py !") # show real code in terminal
        os.remove("tmpfile.py")

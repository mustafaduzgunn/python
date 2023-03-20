import pyfiglet
from termcolor import colored #pip install termcolor

def create_banner():
    # Yeni bir Figlet font nesnesi oluşturun
    custom_font = pyfiglet.Figlet(font="cosmic")
    
    # Yazı örneğini oluşturun
    ascii_banner = custom_font.renderText("MDUZGUN")
    
    # Yazı örneğini ekrana yazdırın
    print(colored((ascii_banner),color="light_yellow"))

create_banner()
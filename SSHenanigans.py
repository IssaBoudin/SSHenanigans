import random
import base64
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk
from colorama import Fore, Style, init

# Initialize colorama for cross-platform support
init(autoreset=True)

# Base64-encoded images
happy_cat_base64 = """
/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhMTExMWFhUVGBgXFRgXGBgVFxgXGBYXGBoYFhgYHiggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGxAQGy0lICUtLS0tLS0tLy0tLS0tLS0tLS0tLS0tLS0tLS0tLSstLS0tLS0tLS0tLS0tLS0tLSstL//AABEIAKgBKwMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABAUDBgcCAQj/xABAEAABAwIDBAcGAwYGAwEAAAABAAIRAyEEBTESQVFhBiJxgZGh8BMyscHR4QcU8RUjQlJikjNTcoKywiSisxb/xAAZAQEAAwEBAAAAAAAAAAAAAAAAAgMEAQX/xAAjEQEBAQADAAICAgMBAAAAAAAAAQIDESESMSJBBFETQpEU/9oADAMBAAIRAxEAPwDhqIiAiIgIiICIiAiLJhwC5oNxI+KCdSyLEPYHsovc0iQQ0nyVe9hBIIII1BsR2rp2GxlVruq4gDQbo4RuUvH5dSxrf3zRtfw1WgB44TGo5G3CFm/9HX3Gn/B39VyRFbZ7kFbCuIe2WT1Xj3XfQ8iqqFollncZ7LL1XxERdcEREBERAREQEREBF9XxAX2FIwOCqVnBlNhc7gPiTuHNdB6O9AaQh2Jd7R3+W0lrB2u953dHeob5M5+088etfTm0JC78cgwQYW/lqQBt1W7J8dSuG51gvYV6tL+RxAPETY+ELmOSavTu+O5naEiIrFYiIgIiICIiAiIgIiICIiAiIgLJQeA5pOgIJ7isaIOoPozcAcVLy+oQdJ5THhZfcnipQpvj3mNP/qF9B2TosVy2yrQU2VmljgDNnU3izm8BOhGognRc56U9E3UNqrRl1Ee8NX0v9Y4f1eK6RgMYwi4EjefpvVhUa1/uiHge6bhzd4aTqOR+yrzrXHe8/wDE9Zm51r/rgThtCRqNR8/XzWFdH6R9DGvmrg2w8SX0Dv47HZBBb4LQMXhyx0EESJANjHA8wQR3Ldjkzudxi3x3F6qOvpC90qLnTAnepbMsqOJIGhPxU+0ekBFavyCsAOpuleDkdf8Ayyudw6qtXtm/sXqth3MMOaR2hfaDZnkCfI/ZdcYVkpsm50HqBzSlSLiABr68F6qOmANBYc+fafogxuMq5yDo3VxJB9yneXkTpqGj+Iq66P8AQhzgypiJa0wRT0e69gf5QR64dFwWEAAAAsIDW2a0cBy7Fm5efrzH208XB/tr6QMrymlh2bFNmyNTvc48XcezRSalQi+m7n3kaKbUZHvNjsGvYXXhRnUtrd5qjOe/a0XXTA3Enj3zE9pK5b06H/nV/wDZ/wDNi6z+Xjf65Lj3Syvt4zEEfzlv9vV+Sv4Z+TPzX8VQiItLMIiICIiAiIgIiICIiAiIgIiICIiDrv4cVBWwrQdWSw91x5EKdmeE2StO/CfHFuJdS3VGzHNvDnBPguq5jg9sTFxqs+p1bGnN8lajhMPLrODTuvH3VsXVKYG3YbnC7fDUd0FeW4GlPXD/APZ9IlXFJrQyGte4RrBMd8lw8IVVyummt5pjXNLagseI0McecfJQ8+yanjaftCAKzLyP4xaZ56HxV5XykPuTDCbwdDOuiwezDHADS9+yx8ll1dYveWiTO51VDg+j1GnTlwvAjwuqfFVw0lrOq2/ityxLIDtrj6IWh5sYqndvVv8AH5Nat+Srm485n4sgx7gde1ZmZmY19eoVBXrHQL7RrkiNOC2fpk/a7/Nh3vNBHODxSgyk93+GGy0i1tyqqL5HNXHR6h7R/h8RPwUd6+ObU8Z+VWGM6N0/ZvLANotgeuER4lZeifRJlBvt6zdupEsabhu8OPOQfBbK7DGI9aqXQpyI36cdPncLz5/J5L43X+PifkiYVpcdp2p9X+ivMNhnRYEDlae8rHleXlhJImN/qys6rnb9lo8XfH6K/ix4p3fVPiqEHQd1/MrG2gFOqULrLhcIXHkNVfIq1UR1DZaCTG86aC517F+eMXW23vf/ADOc7xJPzXcfxPzP8vhHwOtV/dM5bQO0bf0g+K4QrOKfdUct+oIiK5SIiICIiAiIgIiICIiAiIgIiICIiCdkuYHD16VZutN4d2jeO8SO9fpWg4VGMq0zLXgOB5ESCvy6F3/8OMUG5dRcA8jQgnaAItb+mx7NFVy+fkt4/fEzN8FIJFiqTDmptdV1xoCTJ7D8lsmJrB0uG/0VAxVIBsjTcbWKp1Z9tOf6qNjMwc4bLgb20i8b7myr6NI2IJggm+o3wewyPFZW7cwZIO8+r339iztokAC+pvu9aqjdn7W5n9MWOpksEX4eGngW+C0fGYAvc8/yifL9fBdLxVGKDnaQJJ5xr5LWMJQ26NVxF3Ntw+yrmrPyTsl8rnmYUNmSO5RGgwtlr5aXzG746rDTyd2gjj677LZnlz16y74td+IOX4YuAEawPFbh0Vy1zHX3nyB+699F8r9o9gI0InuJ+Nls2Xhv5g0og3PCZtbwWbk5bq2RoxxzMlq8w+E6ote3wUfEZfBBBj9Z+EK1bDbc/XrmvryCez0B5eS5Jkt0x0gSOfq8BfBRKzYVmyZP8V+7jy+yk4mBoLnQfMrRnqRVe+0XD4Ym3BSfZEdVthvWWjUAgeK8dJMx/L4arVptDnMYXAEwLDeeClbPpXXD/wAZc19pi24dp6tBvW4e0fBPg3ZHiufLPjcU6rUfUeZe9xc48S4yVgWjM6nTLq93sREUnBERAREQEREBERAREQEREBERAREQAus/hBnkUamGcfdcXNHJwEjxBK5MrXo1mDqNdpbvsVXy57z4nx2TXrv2LpCJGh4bj8lCq1wBBIkc9e0aqooZo4NlxifD4LXcxz8h1iF593q+R6Ocz7raTAM6Sb8FshpUzTAkAEXJLYtzlc1yTPYeXVQXN/lmB38VsgzDBVT+8wu1wa+o97f7J2fELnU7/Ivf+rbTgxUw7mNc2SCLEEHw9XVJ+yzQw5bq4D4bvNYaGWYCpGzR/K1D7tTDuNMg8wDDhycO5Rck6QPbUqYbEuBA2tiqYG2AY6wGjgF25zZ1L4jLqXuqbLS3rW4+O7sU1lFnfE93onwXgUGh7tniZ7DcfNWmGoMaGvJmyy6nvjXL4ndFMAQC4Dt7dVY4TJHfmfakQ0CJnXuWD9u0sJhuqC+oSYYwSSdY5CN6wYDJa+LaK2Lxj2Md1hToE02gHc5/vOO60LRx46nbLvVtrZnYXrE7jv8AkN4WPF4cN2eHrn5KsoZLgsOZGJr7W4mtUqDwdIUmtjaRaS2o55F2g6eACamZ9VzN1ftKdT2veEr48gEgA6S53yn6BUFDpJtW2S0g79Pur3DYwPH6pnl6vVTvH52w1KDiIFr3VH+JebUcPl1ZjjL6o9mwRMuPHgALq1zHNwzqgeVvNcR/EbO6mIrBrnHYbcN3A6Sr+K/Lk8UcvmGnoiLewiIiAiIgIiICIiAiIgIiICIiAiIgIiICkYOpDgYFjvn5KOvoQdArZqCwbBsRqBN+F9FT0mF77tB/u/6lYMjG23ZhxHHQTwkn6LZcLg2U+sQ2ee0752WLWZit2NfOMtHBN2RLC3mCDPZI+a9OcGiATO7QnxG9Rv2sGOuxrhwLTH/OVcUKlKpsj2NRkkWDakf3OdEeCquLfVk3J4z5dQcRtvqbIiYmI/qHEaLHmmVCmDWJa+YLCDv1nn91tzsPS2NmphRsxAeww4A6mZsR23Uv/wDNMqYZ2y+ZaQ07MFtrW3qv46+Xiz5569c0wWOnZbvNz2q3GK1EnT4LVsDR9jiHNqOIewmxAgidQr+lg34uuynQdLxBfI6rRzI+CleLPfTs5NSdrGjkRxDW1S4McN8wHN+XBSMRTxNNrQ0h9NguAbgaTPzPmtuzfo4GYem32gbBEuLZ8AvGW5dhgA1jKhmRvLZBuXTYd6quNd9O/wCTPXcaZTxgqDUzaRu8yJ7lsOTYGRftvb6qG7KW0qriXAiTFp42JNpVth6zTAHlY/OVH4/27dzrxSdIGezPb3R8IXrJMY4W1PIlXGaYRr2zA011+AlaxUpmk4xYcvVks7dl8fOleYezpVHT1t0GLniuLYiqXOJcZJ36re+lubFwIDr8/uFoL9V6X8bHWfXnfydd66jyiItLMIiICIiAiIgIiICIiAiIgIiICIiAvoC+Ig9CPVl7bWjQN7xtf8pCxIgtsrxzxUBLnG+8rZ8wxVTi7Z3LTcJRMgkgDnv7Bv8Agt+wjNugI95tp3x/1Wbmz7208Ov0o6rHOuerzcdRxA1Pcp2BdTYNo02O2dXu22tnWxLrkcBTJWCpg7kmT814q4ckcOHLsXMWJbldEyTpKwNaWugbwQSCP9MWHOw5K/Z0qGzA2Z7dm/ZEXXA31alEmCQdZ4uO/nAnvuvNPNqxsHmTYdp4c1ZOPr6V/Pv7bh06rNNQVmmC4w4ag2kOHA8Vsn4YZk1jdtzpcRGzoABx4n6LkONqVNtwqTtNJaQdxFiPJZsvxlam792XSQSQJNgJJgcge5P8c+0py+dfp+nsVnNOoACwHhtaSsbcy6pO0xojRo/7X+C4ThekWIGyS4GdxExNte8KRSzvFYjZhxbJhpFg13YPeBkTrFzxBhrEtSlsjomNxRdLjsuIOpAa7sa9tjrvPcoVDGkOuSBNpJ8joe0LJSwz20htgCoReBYns07v0VXReQ61p112T2g/dZubMni7htbnh8dtMI1t6O/xWqdJCKTS6CJ5694Vzg3kNNoPL1ZaR05zAA7PLj8IsVVxY7qze5I0TOcaXuN1VrJXfJKxr1pOp08vV7vYiIuuCIiAiIgIiICIiAiIgIiICIiAiIgIiIC9MdG7xXlEGRlQzzK3fotiAww920XC7R7rQdJjU8zpZaTSgXO7QcT9FYZbmDw4NabuPZfifNQ3O4njXVb/AInC3nUcVEfR5KZlL4ZDiXA7zrMDRZsSG7zfgqJOl1ta7i8G2oIcFRYvLDQqMNyDdh5tvHwWz1xeymZdmGzDTETP6KyaR6U1es3EVDUrYXYL9XAOMm2rRHoqVhatKk5zaWHdtPBptqX0eIJa0iRabLb6T2PjaA1mwvrYDdc71fUaNEt6wbEWJ5DzXPU+5I5tknRepiHuFLqU2dUveJl0yYA3xC6HlHR6jhgD774947rRYDTReMRnlFjRTohrW/06TvMBYaWYhxuY9bk8RttWeKaHttqO5QBgNoyRB3/X1yUmm9pPvQe2FgzDN20w4RJ0MatMfxDcCDroqN47va3Gup0xY/FNp0nAOh38PZ8wuQZ/inOeQ+HCZBtI5j1fwK2rNsS5xkPmZjtETHbIP+5aXmzHbwp8GeqjzXxVvbHq3cvK+kr4tbIIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiD04qXlWFdUqANChLb+idHZBdE9yhvXUTxnup2LxfstkbwI3wsX7RPMzoUzChtXhRGSbHUafZZ5WmxndidwXj2h5816p03bpWWnhnON1LtHplw2YVNxsrH87Uew7ROtliZhdICsMFRkQRZcunZlHw7ZEaFe6tZzYgkj1u9aKxGAi+7ivZwROgVN2tmFO7GvMTdZ6dRzxvMCATcgcJ4K4oZPNzHavdTBtaIEKu6qyZjUsVSFxEHXvH2J8lU4nC7XPmtlzOiQdPsqupT5K3j0r5M9tSx+XFtwFXFpGq3+jRYbGF5xHR9jhOz64LTOXr7Zbxf00BFbZnlT2E2sqtzCFbLL9KrLPt5REXXBERAREQEREBERAREQEREBERAREQEREHpq3jo0wmmbXjXl4rSsM0lwA1XTclwzm0RO/1uVPNfF3FPUR1MbvmF9o4czMd8Ka9gmLrNToyd/rislrVHrCZftKzZlgA0TBgjf5fBWLKJdxXe3OmAYFoGi+twQKtKeFiB4r0cNChanEXDYDasSY8FOdhWt3eCz06JhRsSdwKja7J3UWvVAmAqmo86m3w7+CsKx2TJF+1RX0y+8R2b+1Q7WdKnHstPn9wqWs3h8PmtlqYIkXv4/JUmaMcBAAtyv4qzFV6ivpuvz9aK6whkadypKLYIv5K+y93Yee/4q6q4x4zAhwNr+K0zPcnM9UQO9dGIMb47h+qrcywoeNPD7pndlc1majk1WkWm4WNbJnuVuBJGi11zYWzOpqdses/GvKIikiIiICIiAiIgIiICIiAiIgIiICIiCdlH+IPrA7yur4doNJmze25EWfm+2jh+nn2Mm0W8vupGDwZOum7ciLNYvlXOHwtvIfZWTKAECP0REEikJMKZ+UtzC+Io2eHfrFiGkCygugSdT5oiqq6IrqYfMi3Ky+UcMBvtzX1FDtPp4xFIAdU+Eny3KhxtHUGTOvoL6itzEFczARuPx+SkUAWmG6fD6IislQsWMkbwZWOtTOtu3VfEXUVHm+XB4Mjw+y0HNsKGmwMdiIr+G+quaTpVkL4iLUyCIiAiIg//2Q==
"""
sad_cat_base64 = """
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
"""

def decode_image(base64_string):
    """Decode a Base64 image and return a PIL Image."""
    image_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(image_data))

def show_image(base64_string, title):
    """Display an image decoded from Base64."""
    root = tk.Tk()
    root.title(title)

    img = decode_image(base64_string)
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
    root.mainloop()

def generate_local_port_forwarding():
    local_port = random.randint(1000, 9999)
    remote_port = random.randint(1000, 9999)
    remote_ip = f"10.10.{random.randint(1, 255)}.{random.randint(1, 255)}"
    return ("Local Port Forwarding", 
            f"{Fore.CYAN}You want to access a service running on {remote_ip}:{remote_port} but it is only accessible locally. "
            f"Write an SSH command to forward your local port {local_port} to the remote service.{Style.RESET_ALL}",
            {
                "REMOTE_IP": remote_ip,
                "LOCAL_PORT": str(local_port),
                "REMOTE_PORT": str(remote_port)
            })

def generate_reverse_port_forwarding():
    remote_port = random.randint(1000, 9999)
    local_port = random.randint(1000, 9999)
    remote_ip = f"10.10.{random.randint(1, 255)}.{random.randint(1, 255)}"
    return ("Reverse Port Forwarding", 
            f"{Fore.CYAN}You want to make a service running locally on your machine on port {local_port} "
            f"accessible on the remote server's port {remote_port} on {remote_ip}. "
            f"Write an SSH command to accomplish this.{Style.RESET_ALL}",
            {
                "REMOTE_IP": remote_ip,
                "LOCAL_PORT": str(local_port),
                "REMOTE_PORT": str(remote_port)
            })

def generate_dynamic_port_forwarding():
    local_port = random.randint(1000, 9999)
    remote_ip = f"10.10.{random.randint(1, 255)}.{random.randint(1, 255)}"
    return ("Dynamic Port Forwarding", 
            f"{Fore.CYAN}You want to set up a dynamic SOCKS proxy on your local port {local_port} to route traffic through the SSH server {remote_ip}. "
            f"Write an SSH command to accomplish this.{Style.RESET_ALL}",
            {
                "REMOTE_IP": remote_ip,
                "LOCAL_PORT": str(local_port)
            })

def generate_multiple_services():
    remote_ip = f"10.10.{random.randint(1, 255)}.{random.randint(1, 255)}"
    local_port1 = random.randint(1000, 9999)
    remote_port1 = random.randint(1000, 9999)
    local_port2 = random.randint(1000, 9999)
    remote_port2 = random.randint(1000, 9999)
    return ("Multiple Services", 
            f"{Style.RESET_ALL}The remote machine ({remote_ip}) is hosting:{Style.RESET_ALL}\n"
            f"{Fore.CYAN}A web server on localhost:{remote_port1}.\n"
            f"An SSH service on localhost:{remote_port2}.{Style.RESET_ALL}\n"
            f"{Style.RESET_ALL}Write an SSH command to forward:{Style.RESET_ALL}\n"
            f"{Fore.CYAN}Your local port {local_port1} to the remote web server.\n"
            f"Your local port {local_port2} to the remote SSH service.{Style.RESET_ALL}",
            {
                "REMOTE_IP": remote_ip,
                "LOCAL_PORT1": str(local_port1),
                "REMOTE_PORT1": str(remote_port1),
                "LOCAL_PORT2": str(local_port2),
                "REMOTE_PORT2": str(remote_port2)
            })

def generate_chained_port_forwarding():
    bastion_ip = f"10.10.{random.randint(1, 255)}.{random.randint(1, 255)}"
    target_ip = f"10.10.{random.randint(1, 255)}.{random.randint(1, 255)}"
    local_port = random.randint(1000, 9999)
    remote_port = random.randint(1000, 9999)
    return ("Chained Port Forwarding", 
            f"{Fore.CYAN}You can only reach the target machine ({target_ip}) through a bastion host ({bastion_ip}). "
            f"Write an SSH command to forward your local port {local_port} to {target_ip}:{remote_port} through the bastion host.{Style.RESET_ALL}",
            {
                "BASTION_IP": bastion_ip,
                "TARGET_IP": target_ip,
                "LOCAL_PORT": str(local_port),
                "REMOTE_PORT": str(remote_port)
            })

def check_answer(question_type, question_variables, user_input):
    correct_answer = ""

    if question_type == "Local Port Forwarding":
        correct_answer = "ssh user@REMOTE_IP -L LOCAL_PORT:localhost:REMOTE_PORT"
    elif question_type == "Reverse Port Forwarding":
        correct_answer = "ssh user@REMOTE_IP -R REMOTE_PORT:localhost:LOCAL_PORT"
    elif question_type == "Dynamic Port Forwarding":
        correct_answer = "ssh user@REMOTE_IP -D LOCAL_PORT"
    elif question_type == "Multiple Services":
        correct_answer = ("ssh user@REMOTE_IP -L LOCAL_PORT1:localhost:REMOTE_PORT1 "
                          "-L LOCAL_PORT2:localhost:REMOTE_PORT2")
    elif question_type == "Chained Port Forwarding":
        correct_answer = "ssh -J user@BASTION_IP user@TARGET_IP -L LOCAL_PORT:localhost:REMOTE_PORT"
    else:
        return False, "Unsupported question type."

    for placeholder, value in question_variables.items():
        correct_answer = correct_answer.replace(placeholder, value)

    return correct_answer.strip() == user_input.strip(), correct_answer

def generate_random_question(last_two_types):
    """Randomly select and generate a question, avoiding the last two types."""
    question_generators = {
        "Local Port Forwarding": generate_local_port_forwarding,
        "Reverse Port Forwarding": generate_reverse_port_forwarding,
        "Dynamic Port Forwarding": generate_dynamic_port_forwarding,
        "Multiple Services": generate_multiple_services,
        "Chained Port Forwarding": generate_chained_port_forwarding
    }

    available_types = [q for q in question_generators if q not in last_two_types]
    selected_type = random.choice(available_types)
    return question_generators[selected_type](), selected_type

def main():
    print(f"{Fore.MAGENTA}Welcome to the Port Forwarding Practice Script! 🚀{Style.RESET_ALL}\n")
    last_two_types = []
    points = 0  # Initialize points

    while True:
        # Display points before the question
        print(f"{Fore.CYAN}Your current points: {points}{Style.RESET_ALL}\n")

        # Generate a random question
        (question_type, question, variables), selected_type = generate_random_question(last_two_types)
        last_two_types.append(selected_type)
        if len(last_two_types) > 2:
            last_two_types.pop(0)

        print(f"{Fore.YELLOW}[Question Type: {question_type}]{Style.RESET_ALL}")
        print(question)

        user_input = input(f"\n{Fore.BLUE}Enter your SSH command: {Style.RESET_ALL}")
        result = check_answer(question_type, variables, user_input)

        if result[0]:  # Correct answer
            points += 25
            print(f"\n{Fore.GREEN}✅ Correct! Well done.{Style.RESET_ALL}")
            print(f"{Fore.CYAN}You earned 25 points!{Style.RESET_ALL}\n")
            show_image(happy_cat_base64, "Happy Cat")
        else:  # Incorrect answer
            points -= 25
            correct_answer = result[1]
            print(f"\n{Fore.RED}❌ Incorrect.{Style.RESET_ALL} The correct answer is: {Fore.GREEN}{correct_answer}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}You lost 25 points.{Style.RESET_ALL}\n")
            show_image(sad_cat_base64, "Sad Cat")

        # Display updated points after each question
        print(f"{Fore.CYAN}Your updated points: {points}{Style.RESET_ALL}\n")

        # Prompt user to continue or exit
        input(f"{Fore.CYAN}Press Enter to generate another question or Ctrl+C to exit...{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()

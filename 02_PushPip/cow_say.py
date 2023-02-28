import argparse
import cowsay

def parse():
    modes = ["b", "d", "g", "p", "s", "t", "w", "y"]
    parser = argparse.ArgumentParser()
    parser.add_argument("message", nargs='?', default="hello", help="text")
    parser.add_argument("-f", "--cowfile", default="default", help="cowfile")
    parser.add_argument("-e", "--eye_string", default="00", help="cows eyes")
    parser.add_argument("-T", "--tongue_string", default="  ", help="cows tongue")
    parser.add_argument("-W", "--width", type=int, default=40, help="Text width")

    parser.add_argument("-n", action="store_true")
    parser.add_argument("-l", action="store_true")

    for mode in modes:
        parser.add_argument(f'-{mode}', action="store_true")
    arguments = parser.parse_args().__dict__
    return arguments, modes
def main():
    arguments, modes = parse()
    if arguments["l"]:
        print(cowsay.list_cows())
    else:
        preset = "".join(mode for mode in modes if arguments[mode])
        if "/" in arguments["cowfile"]:
            print(cowsay.cowsay(message=arguments["message"], cowfile=arguments["cowfile"], preset=preset,
                                eyes=arguments["eye_string"],
                                tongue=arguments["tongue_string"], width=arguments["width"], wrap_text=arguments["n"]))
        else:
            print(cowsay.cowsay(message=arguments["message"], cow=arguments["cowfile"], preset=preset,
                                eyes=arguments["eye_string"],
                                tongue=arguments["tongue_string"], width=arguments["width"], wrap_text=arguments["n"]))

if __name__ == '__main__':
    main()
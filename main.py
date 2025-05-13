from window import Window

def main():
    print("Hello, World!")

if __name__ == "__main__":
    app = Window(800, 600)
    app.wait_for_close()
    main()  
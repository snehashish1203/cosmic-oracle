from time import sleep
from cosmic_oracle.engine import generate_answer
from cosmic_oracle import ui
def main():
    ui.show_banner()
    
    while True:
        user_res = ui.question_panel()
        if user_res == 0:
            break
        ui.loader()
        choice = generate_answer(user_res)

        ui.printer("\n[bold]Revealing prophecy...[/bold]")
        sleep(0.5)
        
        ui.animated_prophecy_panel(choice)

        select = ui.menu()

        if select == 0:
            ui.printer("\n[bold red]The Oracle returns to silence...[/bold red]")
            break


if __name__ == "__main__":
    main()


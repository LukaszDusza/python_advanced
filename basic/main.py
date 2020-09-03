import player_provider

def main():
    name = input("Podaj imię gracza:\n")
    email = input("Podaj email gracza:\n")
    player = player_provider.create_player(name, email)
    print("Zarejestrowano gracza o imieniu " + player.get_name())
    print("Gracz ten ma póki co: " + str(player.get_points()) + " punktów")
    player_provider.show_all_players()

# wskazujemy poczatek programu:
if __name__ == "__main__":
    main()

    # praca domowa: na podstawie pliku kalkulator dodaj menu do aplikacji 
    # 1. dodaj gracza 
    # 2. skasuj gracza 
    # 3. rozpocznij grę
    # 4. wyjdz z gry
import random

#Definimos las opciones disponibles para el juego
option = ("Piedra", "Papel", "Tijera")

#Contadores de vitorias
computer_wins = 0
user_wins = 0

#Contador de rondas jugadas
rounds = 1

while True:

  #Imprimimos el número de rondas actual
  print('*' * 10)
  print('ROUNDS: ', rounds)
  print('*' * 10)
  print('\n')

  #Imprimos el marcador actual
  print(f'El marcador va Usuario {user_wins} vs Computer {computer_wins}\n')

  #Usuario escoge una opción 
  user_option = input("Piedra, Papel, Tijera: ")
  user_option = user_option.capitalize()

  #Incrementamos el contador de rondas
  rounds += 1
  
  #Si el usuario ingresa una opción no válida, continuamos con la siguiente ronda
  if not user_option in option:
    print(f'La opción {user_option} no hace parte del juego.\n')
    continue

  #La computadora escoge una opción aleatoria (Randomizada sin seed)
  computer_option = random.choice(option)

  #Imprimimos la opción escogida por la computadora
  print(f'\nLa computadora escogió {computer_option}\n')

  #Comparamos las opciones escogidas y determinamos el ganador de la ronda
  if user_option == computer_option:
    print("¡Hay un empate!\n")

  #Conficiones del juego
  elif user_option == 'Piedra':
    if computer_option == 'Tijera':
      print('Piedra grana a Tijera')
      print('¡Usuario gana!')
      user_wins += 1

    else:
      print('Papel gana a Piedra')
      print('¡Computer gana!')
      computer_wins += 1

  elif user_option == 'Papel':
    if computer_option == 'Piedra':
      print('Papel gana a Piedra')
      print('¡Gana el User!')
      user_wins += 1

    else:
      print('Tijera gana a Papel')
      print('¡Computer gana!')
      computer_wins += 1

  elif user_option == 'Tijera':
    if computer_option == 'Papel':
      print('Tijera gana a Papel')
      print('¡Gana el user!')
      user_wins += 1

    else:
      print('Piedra gana a Tijera')
      print('¡Computer gana!')
      computer_wins += 1

  #Verificamos si alguno de los jugadores ha ganado dos rondas
  if computer_wins == 2:
    print('\n¡El ganador definitivo es la computadora!')
    break

  if user_wins == 2:
    print('\n¡El ganador definitivo es el usuario!')
    break
    
  
  
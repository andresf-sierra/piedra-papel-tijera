# Documentación del Juego

# Juego: Piedra, Papel o Tijera

Este es un juego de Piedra, Papel o Tijera desarrollado para poner en práctica mis habilidades básicas en Python.

## Instrucciones

1. El jugador elige una opción: Piedra, Papel o Tijera.
2. La computadora elige una opción al azar.
3. Se determina el ganador según las reglas del juego.
4. El primer jugador en ganar dos veces seguidas es el ganador definitivo.

## Explicación del código

Aquí hay una explicación de cada parte del código:

- **`import random`** importa el módulo **`random`** para generar opciones aleatorias para la computadora.
- **`option = ("Piedra", "Papel", "Tijera")`** define las opciones posibles para el juego.
- `computer_wins = 0` y `user_wins = 0` inicializan los contadores de victorias de la computadora y del usuario en 0, respectivamente.
    - `rounds = 1` inicializa la primera ronda del juego

El siguiente bloque de código inicia un bucle while que se ejecutará hasta que se alcance una condición de finalización:

```python
while True:
```

El siguiente bloque de código imprime la ronda actual y el marcador:

```python
print('*' * 10)
  print('ROUNDS: ', rounds)
  print('*' * 10)
  print('\n')

  print(f'El marcador va Usuario {user_wins} vs Computer {computer_wins}\n')
```

Luego, el usuario ingresa su opción y se capitaliza la primera letra de la opción:

```python
user_option = input("Piedra, Papel, Tijera: ")
user_option = user_option.capitalize()
```

Después se incrementa el número de rondas:

```python
rounds += 1
```

Si la opción del usuario no está en la lista **`option`**, se imprime un mensaje de error y se continua con la siguiente ronda:

```python
if not user_option in option:
    print(f'La opción {user_option} no hace parte del juego.\n')
    continue
```

A continuación, se genera aleatoriamente una opción para la computadora:

```python
computer_option = random.choice(option)
```

Se imprime la opción de la computadora:

```python
print(f'\nLa computadora escogió {computer_option}\n')
```

Luego, se comparan las opciones del usuario y de la computadora para determinar el ganador:

```python
if user_option == computer_option:
    print("¡Hay un empate!\n")
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
```

Si la computadora o el usuario alcanzan dos victorias, se imprime un mensaje de que han ganado y el juego termina:

```python
if computer_wins == 2:
    print('\n¡El ganador definitivo es la computadora!')
    break
  if user_wins == 2:
    print('\n¡El ganador definitivo es el usuario!')
    break
```
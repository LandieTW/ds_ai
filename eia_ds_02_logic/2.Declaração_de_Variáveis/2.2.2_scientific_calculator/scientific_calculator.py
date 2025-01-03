"""
Para construir uma calculadora científica, você pode implementar as seguintes funcionalidades:

### Funcionalidades Básicas:
3. **Funções Exponenciais e Logarítmicas**:
   - Exponenciação (`x^y`)
   - Raiz quadrada (`sqrt(x)`)
   - Logaritmo natural (`ln(x)`)
   - Logaritmo de base 10 (`log(x)`)

4. **Funções Matemáticas Adicionais**:
   - Fatorial (`x!`)
   - Valor absoluto (`abs(x)`)
   - Valor de π (`pi`)

### Funcionalidades Avançadas:
5. **Funções Trigonométricas em graus ou radianos**:
   - Definir unidade para os ângulos (graus ou radianos)

6. **Funções de Manipulação de Matrizes** (se desejado):
   - Determinante
   - Transposta

7. **Funções Estatísticas**:
   - Média
   - Desvio padrão
   - Variância

8. **Conversões**:
   - Conversão de ângulos (graus, radianos, gradians)
   - Conversão de unidades (por exemplo, Celsius para Fahrenheit)

9. **Funções de Cálculo Avançado**:
   - Integração numérica (método de integração de Simpson, por exemplo)
   - Derivação numérica (método de diferenças finitas)

10. **Memória**:
    - Armazenar e recuperar resultados (memória de operação)

### Extras:
11. **Interface Gráfica (GUI)** (opcional):
    - Usar bibliotecas como Tkinter ou PyQt para uma interface visual amigável.
    
12. **Histórico de Cálculos**:
    - Armazenar e exibir os cálculos anteriores.

Essa lista pode ser adaptada conforme você queira expandir ou simplificar a calculadora. Para começar, seria interessante implementar as funções mais básicas e ir incrementando aos poucos.
"""

# CONSTANTS

modes = (
    {1: 'COMP', 2: 'SD', 3: 'REG'},
    {1: 'Deg', 2: 'Rad', 3: 'Gra'},
    {1: 'Fix', 2: 'Sci', 3: 'Norm'},
    'Disp'
)
count = -1

# LIBS

import math
import os

# METHODS

def counter():
    global count
    print(count)
    if count == 2:
        count = -1
    else:
        count += 1

def fat(n: int):
    fat_n = 1
    for i in range(n):
        fat_n = fat_n * (fat_n - i)
    return fat_n

def comb(n_1, n_2):
    return fat(n_1) / (fat(n_2) * (fat(n_1 - n_2)))

def perm(n_1, n_2):
    return fat(n_1) / fat(n_1 - n_2)

# CLASS

class Sci_Cal:

    mod = ''  # Depois tenho que ver o que cada modo faz e ajustar o código

    last_result = None

    A = None
    B = None
    C = None
    D = None
    E = None
    F = None

    shift = False
    alpha = False

    def __init__(self):
        pass

    def shift_button():
        if Sci_Cal.shift:
            Sci_Cal.shift = False
        else:
            Sci_Cal.shift = True
    
    def alpha_button():
        if Sci_Cal.alpha:
            Sci_Cal.alpha = False
        else:
            Sci_Cal.alpha = True

    def mode():
        try:
            if Sci_Cal.alpha:
                os.system('clear')
                Sci_Cal.last_result = None
            else:
                x = ''
                while x == '':
                    counter()
                    x = int(input(f"Select calculator mode: {modes[count]}"))
                Sci_Cal.mod = modes[count][x]
        except Exception:
            print(Exception)
    
    def fat_n(*val: int) -> float:
        try:
            if val:
                if Sci_Cal.shift:
                    Sci_Cal.last_result = fat(val)
                else:
                    Sci_Cal.last_result = 1 / val
            else:
                if Sci_Cal.shift:
                    Sci_Cal.last_result = fat(Sci_Cal.last_result)
                else:
                    Sci_Cal.last_result = 1 / Sci_Cal.last_result
            return Sci_Cal.last_result
        except Exception:
            print(Exception)
    
    def comb_perm(n_1: int, n_2: int) -> float:
        try:
            if Sci_Cal.shift:
                Sci_Cal.last_result = perm(n_1, n_2)
            else:
                Sci_Cal.last_result = comb(n_1, n_2)
            return Sci_Cal.last_result
        except Exception:
            print(Exception)
    
    def pol_rec():
        ''

    def sum_n(n_1: float | int, *n_2: float | int) -> float:
        try:
            if n_2:
                Sci_Cal.last_result = n_1 + n_2
            else:
                Sci_Cal.last_result += n_1
            return Sci_Cal.last_result
        except Exception:
            print(Exception)
    
    def sub_n(n_1: float | int, *n_2: float | int) -> float:
        try:
            if n_2:
                Sci_Cal.last_result = n_1 - n_2
            else:
                Sci_Cal.last_result -= n_1
            return Sci_Cal.last_result
        except Exception:
            print(Exception)
    
    def mul_n(n_1: float | int, *n_2: float | int) -> float:
        try:
            if n_2:
                Sci_Cal.last_result = n_1 * n_2
            else:
                Sci_Cal.last_result = Sci_Cal.last_result * n_1
            return Sci_Cal.last_result
        except Exception:
            print(Exception)
    
    def div_n(n_1: float | int, *n_2: float | int) -> float:
        try:
            if n_2:
                Sci_Cal.last_result = n_1 / n_2
            else:
                Sci_Cal.last_result = Sci_Cal.last_result / n_1
            return Sci_Cal.last_result
        except Exception:
            print(Exception)
    
    def sin_n(*rad: float | int) -> None | float:
        try:
            if rad:
                if Sci_Cal.alpha:
                    print("Alpha is on.")
                    Sci_Cal.D = rad
                    return None
                else:
                    if Sci_Cal.shift:
                        print("Shift is on.")
                        Sci_Cal.last_result = math.asin(rad)
                    else:
                        Sci_Cal.last_result = math.sin(rad)
            else:
                if Sci_Cal.shift:
                    print("Shift is on.")
                    Sci_Cal.last_result = math.asin(Sci_Cal.last_result)
                else:
                    Sci_Cal.last_result = math.sin(Sci_Cal.last_result)
            return Sci_Cal.last_result
        except Exception:
            print(Exception)

    def cos_n(*rad: float | int) -> None | float:
        try:
            if rad:
                if Sci_Cal.alpha:
                    print("Alpha is on.")
                    Sci_Cal.D = rad
                    return None
                else:
                    if Sci_Cal.shift:
                        print("Shift is on.")
                        Sci_Cal.last_result = math.acos(rad)
                    else:
                        Sci_Cal.last_result = math.cos(rad)
            else:
                if Sci_Cal.shift:
                    print("Shift is on.")
                    Sci_Cal.last_result = math.acos(Sci_Cal.last_result)
                else:
                    Sci_Cal.last_result = math.cos(Sci_Cal.last_result)
            return Sci_Cal.last_result
        except Exception:
            print(Exception)

    def tan_n(*rad: float | int) -> None | float:
        try:
            if rad:
                if Sci_Cal.alpha:
                    print("Alpha is on.")
                    Sci_Cal.D = rad
                    return None
                else:
                    if Sci_Cal.shift:
                        print("Shift is on.")
                        Sci_Cal.last_result = math.atan(rad)
                    else:
                        Sci_Cal.last_result = math.tan(rad)
            else:
                if Sci_Cal.shift:
                    print("Shift is on.")
                    Sci_Cal.last_result = math.atan(Sci_Cal.last_result)
                else:
                    Sci_Cal.last_result = math.tan(Sci_Cal.last_result)
            return Sci_Cal.last_result
        except Exception:
            print(Exception)

    def ln_n(*val: float | int) -> None | float:
        try:
            if val:
                if Sci_Cal.alpha:
                    print("Alpha is on.")
                    Sci_Cal.last_result = math.e
                    return None
                else:
                    if Sci_Cal.shift:
                        print("Shift is on.")
                        Sci_Cal.last_result = math.exp(val)
                    else:
                        Sci_Cal.last_result = math.log(val, math.e)
            else:
                if Sci_Cal.shift:
                    print("Shift is on.")
                    Sci_Cal.last_result = math.exp(Sci_Cal.last_result)
                else:
                    Sci_Cal.last_result = math.log(Sci_Cal.last_result, math.e)
            return Sci_Cal.last_result
        except Exception:
            print(Exception)
            
    def log_n(*val: float | int) -> None | float:
        try:
            if val:
                if Sci_Cal.shift:
                    print("Shift is on.")
                    Sci_Cal.last_result = 10 ** val
                else:
                    Sci_Cal.last_result = math.log10(val)
            else:
                if Sci_Cal.shift:
                    print("Shift is on.")
                    Sci_Cal.last_result = 10 ** Sci_Cal.last_result
                else:
                    Sci_Cal.last_result = math.log10(Sci_Cal.last_result)
            return Sci_Cal.last_result
        except Exception:
            print(Exception)

    def pot_n(n_1: float | int, *n_2: float | int) -> float:
        try:
            if n_2:
                if Sci_Cal.shift:
                    print("Shift is on.")
                    Sci_Cal.last_result = n_2 ** (1 / n_1)
                else:
                    Sci_Cal.last_result = n_2 ** n_1
            else:
                if Sci_Cal.shift:
                    print("Shift is on.")
                    Sci_Cal.last_result = Sci_Cal.last_result ** (1 / n_1)
                else:
                    Sci_Cal.last_result = Sci_Cal.last_result ** n_1
            return Sci_Cal.last_result
        except Exception:
            print(Exception)
    
    def squ_n(*val: float | int) -> float:
        try:
            if val:
                Sci_Cal.last_result = val ** 2
            else:
                Sci_Cal.last_result = Sci_Cal.last_result ** 2
            return Sci_Cal.last_result
        except Exception:
            print(Exception)



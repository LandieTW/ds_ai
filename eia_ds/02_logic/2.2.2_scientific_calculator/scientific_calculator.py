"""
Para construir uma calculadora científica, você pode implementar as seguintes funcionalidades:

### Funcionalidades Básicas:
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
    {1: 'Disp'}
)
count = 0

# LIBS

import math
import os
from fractions import Fraction

# METHODS

def counter(count: int) -> None:
    global count_modes
    if count == 2:
        count = 0
    else:
        count += 1

def fat(n: int):
    fat_n = 1
    for i in range(n):
        fat_n = fat_n * (fat_n - i)
    return fat_n

def comb(n_1: int, n_2: int) -> float:
    return fat(n_1) / (fat(n_2) * (fat(n_1 - n_2)))

def perm(n_1: int, n_2: int) -> float:
    return fat(n_1) / fat(n_1 - n_2)

def rec(r: float | int, teta: float | int) -> tuple[float, float]:
    return ((r / math.cos(teta)), (r / math.sen(teta)))

def pol(x: float | int, y: float | int) -> tuple[float, float]:
    return (math.sqrt(x**2 + y**2), math.atan(y / x))

# CLASS

class Sci_Cal:

    mod = ''  # Depois tenho que ver o que cada modo faz e ajustar o código

    fracao_mod = 'd/c'

    last_result = None

    coord_1 = None
    coord_2 = None

    angle_d = None
    angle_m = None
    angle_s = None

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
        global count
        try:
            if Sci_Cal.alpha:
                os.system('clear')
                Sci_Cal.last_result = None
            else:
                x = ''
                while x == '':
                    x = int(input(f"Select calculator mode: {modes[count]}"))
                    if x == '':
                        counter(count)
                Sci_Cal.mod = modes[count][x]
                count = 0
            print(f"Mode selected: {Sci_Cal.mod}")
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
    
    def pol_rec(x: float | int, y: float | int) -> None:
        try:
            if Sci_Cal.shift:
                Sci_Cal.coord_1, Sci_Cal.coord_2 = rec(x, y)
            else:
                Sci_Cal.coord_1, Sci_Cal.coord_2 = pol(x, y)
            print((Sci_Cal.coord_1, Sci_Cal.coord_2))
        except Exception:
            print(Exception)
    
    def cub_n(*val: float | int) -> float:
        try:
            if val:
                if Sci_Cal.shift:
                    Sci_Cal.last_result = math.pow(val, 1/3)
                else:
                    Sci_Cal.last_result = math.pow(val, 3)
            else:
                if Sci_Cal.shift:
                    Sci_Cal.last_result = math.pow(Sci_Cal.last_result, 1/3)
                else:
                    Sci_Cal.last_result = math.pow(Sci_Cal.last_result, 3)
            return Sci_Cal.last_result
        except Exception:
            print(Exception)

    def fracao_m_d(n_1: float | int, *n_2: float | int) -> float:
        try:
            if Sci_Cal.shift:
                Sci_Cal.fracao_mod = 'd/c'
            else:
                Sci_Cal.fracao_mod = 'a_b/c'
            if n_2:
                Sci_Cal.last_result = n_1 / n_2
            else:
                Sci_Cal.last_result = Sci_Cal.last_result / n_1
            if Sci_Cal.fracao_mod == 'a_b/c':
                int_result = Sci_Cal.last_result // 1
                rac_result = Sci_Cal.last_result - int_result
                frac = Fraction(rac_result)
                print(f"{int_result}+{frac}")
            return Sci_Cal.last_result
        except Exception:
            print(Exception)

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
    
    def raiz_quadrada(*val: float | int) -> float:
        try:
            if val:
                Sci_Cal.last_result = math.sqrt(val)
            else:
                Sci_Cal.last_result = math.sqrt(Sci_Cal.last_result)
            return Sci_Cal.last_result
        except Exception:
            print(Exception)

    def negative(*val: float | int) -> float:
        try:
            if val:
                if Sci_Cal.alpha:
                    Sci_Cal.A = val
                    return Sci_Cal.A
                else:
                    Sci_Cal.last_result = - val
            else:
                if Sci_Cal.alpha:
                    Sci_Cal.A = Sci_Cal.last_result
                    return Sci_Cal.A
                else:
                    Sci_Cal.last_result = - Sci_Cal.last_result
            return Sci_Cal.last_result
        except Exception:
            print(Exception)

    def degrees(val) -> float:
        try:
            ''
        except Exception:
            print(Exception)

from system import System

def main():

  sys = System()

  while True:
    print("")
    print("1: (F1) Gerar o tapete A")
    print("2: (F2) Mostrar o estado dos tapetes, pilhas e robô")
    print("3: (F3) Processar peças")
    print("4: (F4) Mostrar totais")
    print("5: ---- Terminar programa")

    _input =  input("> ")
    if len(_input) == 1 and any(map(lambda i: str(i) == _input, [1,2,3,4,5])):
      if   _input == "1":
        while True:
          num = input("> Quantas peças de cada tipo (> 0): ")
          try:
            num = int(num)
            if num > 0: break
          except Exception as e: pass
          print("Números inteiros > 0, por favor.")
        sys.gen_queue_a(num)
        print(sys.queue_a)
      elif _input == "2":
        pass
      elif _input == "3":
        while True:
          num = input("> Quantas peças (> 0): ")
          try:
            num = int(num)
            if num > 0: break
          except Exception as e: pass
          print("Números inteiros > 0, por favor.")
        sys.process(num)
      elif _input == "4":
        print("Peças recolhidas:       %d" % sys.robot.touched_count)
        print("Embalagens no tapete B: %d" % sys.robot.package_count)
      elif _input == "5":
        break
      else:
        print("1, 2, 3, 4, ou 5 por favor.")

main()

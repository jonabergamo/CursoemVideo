from time import sleep
# cores:|  reset  | amarelo   |    azul   |   verde   |   roxo     | vermelho |
cores = ['\033[0m', '\033[33m', '\033[34m', '\033[32m', '\033[35m', '\033[31m']
# codigo:  | 0 |       | 1 |        | 2 |     | 3 |       | 4 |         | 5 |

print('\nCONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS!!')
print('''                      (
      __________        )\n\
     /         /\______{,}
     \_________\/''')
n = 10
v = 0
for c in range(10, -1, -1):
    print('[{}'.format(cores[v]), n,'{}]'.format(cores[0]))
    n -= 1
    if v < 6:
        v += 1
    elif v == 6:
        v = 0
    sleep(1)

print('''                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\ /.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\.   '
      *            *..*         :
        *
        *''')



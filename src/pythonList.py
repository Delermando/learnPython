list = {}
list['da'] = 'da'
list['de'] = 'de'
#list ar key sensitive
list['De'] = 'de'

#################Delete list############
#delete unic item
del list['de']

#delete a item from your value
list.remove('da')

#delete the last item
list.pop()
#this delete the last item, and return that

#clear array
list.clear()

###############Acessing elements#################
#array per position
list2 = ['da', 'de', 'di', 'do', 'du']

#indice positive, comeca do primeiro para o ultimo
list2[2]
#'di'

#indice negative, comeca do ultimo para o primeiro
list2[-3]
#'di'

list2[-1]
#'du'

############slice lists###########
#positive, pega do primeiro ate o terceiro item
list2[:3]
#'da','de', 'di'

#negative, temos 5 itens -2, igual 3 pega do terceiro ao primeiro
list2[:-2]
#'da','de', 'di'

#number position
# vai do 0 ate o 2
list2[:2]
#'da','de'


#vai do 2 ao ultimo
list2[2:]
#'di', 'do', 'du' 

#range
list2[2:4]
#'di','do'


###########Expandindo lista###############

#adiciona um item na ultima posicao
list2.append('dade')

#insere em uma posicao especifica
list2.insert(2, 'delermando')
#insere na segunda posicao a string 'delermando'

#somar uma lista a atual
array = ['teste1', 'teste2', 'teste3']
list2.extend(array)

############Search in list's###########
list2.index('dade')
#6

#################list operators#########################
list = ['a', 'b', 'c', 'd', 'e']
list = list + ['f', 'g']
#or
list =+ ['f', 'g']
list
#'a', 'b', 'c', 'd', 'e', 'f','g'

list = ['a','b'] * 2
#vai pegar o itens e adicionar a list repetidamente o numero de vezes especificado
list 
#'a','b','a','b'

#concat list
li = [1,2] + [1,2] + [1,2]

####################Mapping list #############################
li = [1,2,3,4,5]
li =  [element * 20 for element in li]
li
#[400, 800, 1200, 1600, 2000]

##################List objets#####################
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

params.keys()
#['pwd', 'database', 'uid', 'server']

params.values()
#['secret', 'master', 'sa', 'mpilgrim']

params.items()
#[('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]

########################interact list########################
#k is keys
#v is values

[k for k, v in params.items()]
#nesta interacao por usar params.itens, cada value e um array dentro de params
#entao intera k e igual a lista e arrays e para cada k, pegue a sua key

[v for k, v in params.items()]
#neste exemplo para cada k pega o seu value

["%s < - > %s" % (k, v) for k, v in params.items()]
#neste exemplo, para cada k pegue o seu value, e chave e concatena na string "%s < - > %s"
#['pwd < - > secret', 'database < - > master', 'uid < - > sa', 'server < - > mpilgrim']


########################join list########################
#join is a function that disponibilize a list in a string, separated by a string that you inform
";".join(["%s=%s" % (k, v) for k, v in params.items()])
#'pwd=secret;database=master;uid=sa;server=mpilgrim'

".".join(["%s=%s" % (k, v) for k, v in params.items()])
#'pwd=secret.database=master.uid=sa.server=mpilgrim'

".".join(v for k, v in params.items())
#'secret.master.sa.mpilgrim'

li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
print ";".join(li)
#'server=mpilgrim;uid=sa;database=master;pwd=secret'

#########################split ########################3
#convert a string in a array using a delimiter
string = 'delermando, deler, del, d'
string.split(',')
#['delermando', ' deler', ' del', ' d']

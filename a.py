from transitions.extensions import GraphMachine
from IPython.display import Image, display, display_png
class Basic(object): pass
states = ['init','text','start','song','res','sticker','help','other','bconv','game','g_up','g_low','g_guess','exc','exc_1','exc_2','exc_1_1','exc_2_1']
transitions = [
    {'trigger': 'text', 'source': 'init', 'dest': 'text'},
     {'trigger': 'stickers', 'source': 'init', 'dest': 'sticker'},
    {'trigger': 'nop', 'source': 'sticker', 'dest': 'init'},
    {'trigger': 'nop', 'source': 'other', 'dest': 'init'},
    {'trigger': 'others', 'source': 'init', 'dest': 'other'},
    {'trigger': '/start', 'source': 'text', 'dest': 'start'},
    {'trigger': 'nop', 'source': 'start', 'dest': 'init'},
    {'trigger': '/song', 'source': 'text', 'dest': 'song'},
    {'trigger': 'nop', 'source': 'song', 'dest': 'init'},
    {'trigger': '/res', 'source': 'text', 'dest': 'res'},
    {'trigger': 'nop', 'source': 'res', 'dest': 'init'},
    {'trigger': '/help', 'source': 'text', 'dest': 'help'},
    {'trigger': 'nop', 'source': 'help', 'dest': 'init'},
    {'trigger': '/bconv', 'source': 'text', 'dest': 'bconv'},
    {'trigger': 'number', 'source': 'bconv', 'dest': 'init'},
     { 'trigger': '/exit', 'source': 'bconv', 'dest': 'init'},
     { 'trigger': '/game', 'source': 'text', 'dest': 'game'},
     { 'trigger': 'num', 'source': 'game', 'dest': 'g_up'},
    {'trigger': 'notnum', 'source': 'game', 'dest': 'game'},
    { 'trigger': '/exit', 'source': 'game', 'dest': 'init'},
    { 'trigger': '/exit', 'source': 'g_up', 'dest': 'init'},
     { 'trigger': 'num1', 'source': 'g_up', 'dest': 'g_low'},
    {'trigger': 'notnum1', 'source': 'g_up', 'dest': 'g_up'},
     { 'trigger': 'num2', 'source': 'g_low', 'dest': 'g_guess'},
    {'trigger': 'notnum2', 'source': 'g_low', 'dest': 'g_low'},
    {'trigger': 'num2>num1', 'source': 'g_low', 'dest': 'g_up'},
     { 'trigger': '/exit', 'source': 'g_low', 'dest': 'init'},
     { 'trigger': 'cor_nums', 'source': 'g_guess', 'dest': 'init'},
    {'trigger': 'notnums', 'source': 'g_guess', 'dest': 'g_guess'},
    {'trigger': 'err_nums', 'source': 'g_guess', 'dest': 'g_guess'},
    { 'trigger': '/exc', 'source': 'text', 'dest': 'exc'},
     { 'trigger': '/exit', 'source': 'exc', 'dest': 'init'},
     { 'trigger': '1', 'source': 'exc', 'dest': 'exc_1'},
     { 'trigger': '2', 'source': 'exc', 'dest': 'exc_2'},
    {'trigger': 'not2andnot1', 'source': 'exc', 'dest': 'exc'},
         { 'trigger': '/exit', 'source': 'g_guess', 'dest': 'init'},
    { 'trigger': '/exit', 'source': 'exc_1', 'dest': 'init'},
     { 'trigger': '/exit', 'source': 'exc_2', 'dest': 'init'},
     { 'trigger': '0~18', 'source': 'exc_1', 'dest': 'exc_1_1'},
    {'trigger': 'outof0~18', 'source': 'exc_1', 'dest': 'exc_1'},
     { 'trigger': '0~18', 'source': 'exc_2', 'dest': 'exc_2_1'},
    {'trigger': 'outof0~18', 'source': 'exc_2', 'dest': 'exc_2'},
         { 'trigger': '/exit', 'source': 'exc_1_1', 'dest': 'init'},
     { 'trigger': '/exit', 'source': 'exc_2_1', 'dest': 'init'},
         { 'trigger': 'num3', 'source': 'exc_2_1', 'dest': 'init'},
    {'trigger': 'notnum3', 'source': 'exc_2_1', 'dest': 'exc_2_1'},
     { 'trigger': 'num4', 'source': 'exc_1_1', 'dest': 'init'},
    {'trigger': 'notnum4', 'source': 'exc_1_1', 'dest': 'exc_1_1'},

]


machine = GraphMachine(model=Basic,
                       states=states,
                       transitions=transitions,
                       initial='init',
                       auto_transitions=False,
                       show_conditions=True,
                       )

machine.get_graph().draw('my_state_diagram.png', prog='dot')
display(Image('my_state_diagram.png')) 

import RFSE


RFSE.Stage('*Messenger*')
RFSE.Messenger('set', 'Messenger_1', 'Message №1. It has the type \'\'set\'\'. Displays a window with some title and '
                                     'content. Each message has a title and content that may be empty. '
                                     'After pressing the \'\'OK\'\' button, the message closes.')
RFSE.Messenger('set', 'Messenger_2', 'Message №2. It has the type \'\'set\'\'. Has a timer after which the message closes'
                                     '. After pressing the \'\'OK\'\' button, the message will be closed regardless of '
                                     'whether the timer has expired.', 'void', str(5))
c = RFSE.Messenger('get', 'Messenger_3', 'Message №3. It has the type \'\'get\'\'. Gets data from a message of a specific'
                                         'type. The default is \'\'void\'\'. Messages like \'\'get\'\' do not have a timer.',
                                         'string')
RFSE.Messenger('set', 'Messenger_4', 'Message №4. You entered: ' + c)
RFSE.Report("exmessenger", 'set', 'string', c)
b = RFSE.Messenger('get', 'Messenger_5', 'Message №5. It has the type \'\'get\'\'. '
                                         'Retrieves \'\'string\'\' data from the message.', 'string')
RFSE.Messenger('set', 'Messenger_6', 'Message №6. You entered: ' + b)
RFSE.Report("exmessenger_1", 'set', 'string', b)
a = RFSE.Messenger('get', 'Messenger_7', 'Message №7. It has the type \'\'get\'\'. '
                                         'Retrieves boolean data from the message. '
                                         'When you click on the \'\'Yes\'\' button, returns True, when you click on \'\'No\'\','
                                         ' it returns False.', 'boolean')
if a == True:
    RFSE.Messenger('set', 'True', 'You clicked on the \'\'Yes\'\' button.')
    RFSE.Report("exmessenger_2", 'set', 'string', 'True')
else:
    RFSE.Messenger('set', 'False', 'You clicked on the \'\'No\'\' button.')
    RFSE.Report("exmessenger_2", 'set', 'string', 'False')
RFSE.Report("exmessenger_3", 'set', 'string', 'The script completed successfully.')


RFSE.EndScript()
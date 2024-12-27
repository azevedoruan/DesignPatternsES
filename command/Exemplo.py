from abc import ABC, abstractmethod

class Command:
    app
    editor
    backup

    def __init__(self, app, editor):
        self.app = app
        self.editor = editor
    
    # faz um backup do estado do editor
    def saveBackup(self):
        backup = editor.text
    
    # restaura o estado anterior do editor
    def undo(self):
        editor.text = text
    
    # método estático para a execução exclusiva dos comandos concretos
    @abstractmethod
    def execute(self):
        pass

class CopyCommand(Command):
    # o comando Copy não faz mudanças no estado do editor. Portanto, não é preciso
    # salva-lo no histórico e retorna false.
    def execute(self):
        app.clipboard = editor.getSelection()
        return false

class CutCommand(Command):
    # o comando Cut faz mudança no estado do editor. Portanto, ele deve ser salvo no
    # histórico e retornar true.
    def execute(self):
        saveBackup()
        app.clipboard = editor.getSelection()
        editor.deleteSelection()
        return true

class PasteCommand(Command):
    def execute(self):
        saveBackup()
        editor.replaceSelection(app.clipboard)
        return true

class UndoCommand(Command):
    def execute(self):
        app.undo()
        return false

class CommandHistory:
    # coleção de commands
    history = {}

    def push(self, command):
        # adiciona o command passado no parâmetro para o fim da coleção history
        pass
    
    def pop(self):
        # retorna o command mais recente adicionado no history
        pass

class Editor:
    text

    def getSelection(self):
        # retorna o texto selecionado
        pass
    
    def deleteSelection(self):
        # deleta o texto selecionado
        pass
    
    def replaceSelection(self, text):
        # insere o conteúdo do clipBoard na posição do texto selecionado
        pass

class Application:
    clipBoard
    editors = {}
    activeEditor
    history

    # inicializando os comandos e atribuindo-os ao objetos de interface (GUI e shortcuts)
    def createUI(self):
        copy = lambda : executeCommand(CopyCommand(self, activeEditor))
        copyButton.setCommand(copy)
        shortcuts.onKeyPress("Ctrl+C", copy)

        cut = lambda : executeCommand(CutCommand(self, activeEditor))
        cutButton.setCommand(cut)
        shortcuts.onKeyPress("Ctrl+X", cut)

        paste = lambda : executeCommand(PasteCommand(self, activeEditor))
        pasteButton.setCommand(paste)
        shortcuts.onKeyPress("Ctrl+V", paste)

        undo = lambda : executeCommand(UndoCommand(self, activeEditor))
        undoButton.setCommand(undo)
        shortcuts.onKeyPress("Ctrl+Z", undo)

    # executa o comando e salva-o no histórico
    def executeCommand(command):
        if command.execute():
            history.push(command)
    
    # retorna o último comando mais recente e chama o seu método undo().
    # note que não precisamos saber de qual comando se trata.
    def undo(self):
        command = history.pop()
        if command != none:
            command.undo()
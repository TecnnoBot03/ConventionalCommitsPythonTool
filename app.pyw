import os
import jsonreader
import tkinter as tk
from tkinter import ttk

projects = jsonreader.downloadScopes()
names = [project["name"] for project in projects]

def update_combobox(*args):
    selected_value = project.get()
    for i in projects:
        if selected_value == i["name"]:
            scopeBox["values"] = i["scopes"]
            scopeBox.current(0)
            break

def enableBreakingChange():
    if(breakingChange.instate(['selected']) != True):
        breakingChangeFooter.config(state='disabled')
        breakingChangeFooterText.config(state='disabled')
    else:
        breakingChangeFooter.config(state='normal')
        breakingChangeFooterText.config(state='normal')

def enableScope():
    if(scope.instate(["selected"]) != True):
        scopeBox.config(state='disabled')
    else:
        scopeBox.config(state='normal')

def enableBody():
    if(body.instate(["selected"]) != True):
        bodyText.config(state='disabled')
    else:
        bodyText.config(state='normal')

def enableBreakingChangeFooter():
    if(breakingChangeFooter.instate(["selected"]) != True):
        breakingChangeFooterText.config(state='disabled')
    else:
        breakingChangeFooterText.config(state='normal')

def createCommitMessage(*args):
    commitType = type.get()
    commitScope = f"({scopeBox.get()})" if scope.instate(['selected']) else ""
    commitBreakingChange = "!" if breakingChange.instate(['selected']) else ""
    commitMessage = message.get()
    commitBody = f"-m \"{bodyText.get()}\"" if body.instate(['selected']) else ""
    commitFooter = f"-m \"BREAKING CHANGE: {breakingChangeFooterText.get()}\"" if breakingChangeFooter.instate(['selected']) else ""

    commit = f"git commit -m \"{commitType}{commitScope}{commitBreakingChange}: {commitMessage}\" {commitBody} {commitFooter}"

    textToCopy = ttk.Label(frm, text=commit)
    textToCopy.grid(column=1, row=14, columnspan=2)

root = tk.Tk()
root.title("Conventional Commits Tool")
root.geometry('600x450')
root.resizable(False, False)

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Button(frm, text="Commit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Projects", command=root.destroy).grid(column=2, row=0)

ttk.Label(frm, text="Type").grid(column=1, row=2)
breakingChange = ttk.Checkbutton(frm, text="Breaking Change", command=enableBreakingChange)
breakingChange.grid(column=2, row=3)
type = ttk.Combobox(frm, state="readonly", values=["build", "chore", "ci", "docs", "feat", "fix", "perf", "refactor", "revert", "style", "test"])
type.grid(column=1, row=3)

scope = ttk.Checkbutton(frm, text="Scope", command=enableScope)
scope.grid(column=1, row=6)
scopeBox = ttk.Combobox(frm, state="readonly", values=[])
scopeBox.grid(column=2, row=6)

ttk.Label(frm, text="Message").grid(column=1, row=7)
message = ttk.Entry(frm)
message.grid(column=1, row=8)

body = ttk.Checkbutton(frm, text="Body", command=enableBody)
body.grid(column=1, row=10)
bodyText = ttk.Entry(frm)
bodyText.grid(column=2, row=10)

breakingChangeFooter = ttk.Checkbutton(frm, text="Breaking Change Footer", command=enableBreakingChangeFooter)
breakingChangeFooter.grid(column=1, row=12)
breakingChangeFooterText = ttk.Entry(frm)
breakingChangeFooterText.grid(column=2, row=12)

ttk.Label(frm, text="Project Template").grid(column=1, row=1)
project = ttk.Combobox(frm, state="readonly", values=names)
project.grid(column=2, row=1)

generateCommit = ttk.Button(frm, text="Generate Commit Message", command=createCommitMessage)
generateCommit.grid(column=1, row=13)

project.bind("<<ComboboxSelected>>", update_combobox)

root.mainloop()

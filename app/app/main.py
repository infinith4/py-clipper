#PySimpleGUIをimportしてsgとします。
import PySimpleGUI as sg

#テーマを決めます。
#テーマの種類は、sg.preview_all_look_and_feel_themes()で確認できます。
sg.theme("DarkBlue")

#表示する画面の設定をします。
layout=[[sg.Text("これはPySimpleGUIのテストです。")]]

window=sg.Window("test",layout)

#無限ループで画面を表示させます。×ボタンで無限ループを抜けます。
while True:
    event,values=window.read()
    if event == sg.WIN_CLOSED:
        break

#画面を閉じます。
window.close()
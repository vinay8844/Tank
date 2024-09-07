import FreeSimpleGUI as sg

FILEPATH = "D:\Data Science\Directory_A\practice_txt_files1\groceries.txt"


def table_r(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data  # "My Grocery List App prepared and working"


def table_w(data, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(data)


label = sg.Text('Type in a Grocery Item')
input_box = sg.InputText(tooltip='Enter Item', key='New-Item')
add_button = sg.Button("Add-Item")
list_box = sg.Listbox(values=table_r(), key="Item-listed", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit-Item")
remove_button = sg.Button("Remove-Item")
exit_button = sg.Button("Exit")
layout_1 = [[label], [input_box, add_button],
            [list_box, edit_button, remove_button],
            [exit_button]]
window = sg.Window("My Grocery List App", layout=layout_1, font=('Helvetica', 20))

while True:
    key1, values1 = window.read()
    print(1, key1)
    print(2, values1)
    print(3, values1["Item-listed"])
    match key1:
        case "Add-Item":
            with open("D:\Data Science\Directory_A\practice_txt_files1\groceries.txt", 'r') as file:
                data = file.readlines()

            latest_item = values1['New-Item'] + "\n"
            data.append(latest_item)

            with open("D:\Data Science\Directory_A\practice_txt_files1\groceries.txt", 'w') as file:
                file.writelines(data)
            window["Item-listed"].update(values=data)

        case "Edit-Item":

            item_to_edit = values1['Item-listed'][0]
            latest_item = values1['New-Item']

            data = table_r()

            index = data.index(item_to_edit)
            data[index] = latest_item

            table_w(data)
            window["Item-listed"].update(values=data)

        case "Remove-Item":
            item_tobe_removed = values1['Item-listed'][0]
            data = table_r()
            data.remove(item_tobe_removed)
            table_w(data)
            window["Item-listed"].update(values=data)
            window['New-Item'].update(value=" ")
        case "Exit":
            break

        case "Item-listed":
            window['New-Item'].update(value=values1['Item-listed'][0])

print("Bye")
window.close()
import tkinter as tk
from tkhtmlview import HTMLLabel



# Create a label to display the result HTML
result_label = HTMLLabel(window, html=result_html)
result_label.grid(row=5, column=0, columnspan=2)
window = tk.Tk()
window.title("Salary Comparison")

def clear_results():
    for label in result_labels:
        label.destroy()

def compare():
    clear_results()

    tpt = 0
    ida = 38.3
    cafetaria = 26
    hra = 18

    bp = float(basic_pay_entry.get())
    level = int(pay_level_var.get())
    da = float(da_percentage_entry.get())
    cea = int(num_children_entry.get())

    # calculation logic

    nbp = round((bp * ((1 + (da / 100)) / (1 + (ida / 100)))), 10)

    if nbp < 20000 and level == 1:
        nbp = 20000

    if nbp < 21000 and level == 2:
        nbp = 21000

    if nbp < 23000 and level == 3:
        nbp = 23000

    daval = round(bp * (da / 100))
    idaval = round(nbp * (ida / 100))

    hraval = round(bp * (hra / 100))
    ihraval = round(nbp * (hra / 100))

    ceaval = cea * 2250

    if level >= 7:
        newsval = 500
    else:
        newsval = 0

    if level >= 13:
        televal = 2000
    else:
        televal = 0

    if level >= 1 and level <= 2:
        if bp >= 24200:
            tpt = round(1800 * (1 + (da / 100)))
        else:
            tpt = round(900 * (1 + (da / 100)))
    elif level >= 3 and level <= 8:
        tpt = round(1800 * (1 + (da / 100)))
    elif level >= 9:
        tpt = round(3600 * (1 + (da / 100)))

    cafetariaval = round(nbp * (cafetaria / 100))

    allow = tpt + ceaval + newsval + televal

    if allow > cafetariaval:
        sca = allow - cafetariaval
    else:
        sca = 0

    # Create HTML table for results
    result_html = f"""
    <table>
        <tr>
            <th colspan="2">Existing Pay</th>
            <th colspan="2">After Absorption</th>
        </tr>
        <tr>
            <td>Basic Pay:</td>
            <td>{bp:.2f}</td>
            <td>New Basic Pay:</td>
            <td>{nbp:.2f}</td>
        </tr>
        <tr>
            <td>DA:</td>
            <td>{daval:.2f}</td>
            <td>IDA:</td>
            <td>{idaval:.2f}</td>
        </tr>
        <tr>
            <td>HRA:</td>
            <td>{hraval:.2f}</td>
            <td>I HRA:</td>
            <td>{ihraval:.2f}</td>
        </tr>
        <tr>
            <td>TPT:</td>
            <td>{tpt:.2f}</td>
            <td>Cafeteria Allowance:</td>
            <td>{cafetariaval:.2f}</td>
        </tr>
        <tr>
            <td>CEA:</td>
            <td>{ceaval:.2f}</td>
            <td>Special Comp. Allowance:</td>
            <td>{sca:.2f}</td>
        </tr>
        <tr>
            <td>Newspaper Allowance:</td>
            <td>{newsval:.2f}</td>
            <td>Total Proposed:</td>
            <td>{nbp + idaval + ihraval + cafetariaval + sca:.2f}</td>
        </tr>
    </table>
    """

    # Create a label to display the result HTML
    result_label = tkhtml.HTMLLabel(window, html=result_html)
    result_label.grid(row=5, column=0, columnspan=2)

    result_labels.append(result_label)

# Input components
basic_pay_label = tk.Label(window, text="Basic Pay:")
basic_pay_label.grid(row=0, column=0, sticky="W")
basic_pay_entry = tk.Entry(window)
basic_pay_entry.grid(row=0, column=1)

pay_level_label = tk.Label(window, text="Pay Level:")
pay_level_label.grid(row=1, column=0, sticky="W")
pay_level_var = tk.StringVar()
pay_level_dropdown = tk.OptionMenu(window, pay_level_var, *range(1, 11))
pay_level_dropdown.grid(row=1, column=1)

da_percentage_label = tk.Label(window, text="DA Percentage:")
da_percentage_label.grid(row=2, column=0, sticky="W")
da_percentage_entry = tk.Entry(window)
da_percentage_entry.grid(row=2, column=1)

num_children_label = tk.Label(window, text="Number of Children for CEA:")
num_children_label.grid(row=3, column=0, sticky="W")
num_children_entry = tk.Entry(window)
num_children_entry.grid(row=3, column=1)

compare_button = tk.Button(window, text="Compare", command=compare)
compare_button.grid(row=4, columnspan=2)

result_labels = []

window.mainloop()

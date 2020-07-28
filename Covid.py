from covid import Covid
from colored import fg, bg, attr
from datetime import datetime
import matplotlib.pyplot as plt
from tabulate import tabulate


def cvd19():
    now = datetime.today()
# dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y")

    covid = Covid()
    act = covid.get_total_active_cases()
    cfd = covid.get_total_confirmed_cases()
    rcd = covid.get_total_recovered()
    dts = covid.get_total_deaths()

    green1 = fg('#008000')
    blue1 = fg('#0000FF')
    black1 = fg('#fff')
    orange1 = fg('#ffa500')
    res = attr('reset')


    print()
    print()
    print()
    print()
    print()
    title = ("COVID 19 Cases (World Wide Data as per "  + dt_string + " )")
    title1 = title.center(40)
    print("\033[1m" +".", title1 + "\033[0m")

    print(tabulate([[act, cfd, rcd, dts]] ,headers=[orange1 + "Active" + res , blue1 + "Confirmed" + res , black1 + "Deaths" + res , green1 + "Recovered" + res]))

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal')
    langs = [ "Active"  , "Confirmed" , "Deaths" , "Recovered"]
    students = [act, cfd, rcd, dts]
    ax.pie(students, labels = langs, autopct='%1.2f%%')
    plt.show()

x = 1

while (x):
    cvd19()

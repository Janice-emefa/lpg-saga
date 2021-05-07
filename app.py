# if __name__ == '__main__':
#     running = True
#     while running:
#         price = int(input('Enter the price(In Cedis): '))
#         gas_source = input('Select gas source(Tema/Atoabo): ')
#         if (gas_source.upper() != "TEMA"):
#             gas_source = input('Please pick a valid gas source(Tema/Atoabo): ')
#         elif (gas_source.upper() != "ATOABO"):
#             gas_source = input('Please pick a valid gas source(Tema/Atoabo): ')
#         calc = LPGCal(price)
#         mass = calc.lpg_mass()
#         volume = calc.lpg_vol(gas_source)

#         print(f'Mass(in KG) : {mass}')
#         if gas_source.lower() == 'tema':
#             print(f'Volume(gas source -- {gas_source}: {volume}')
#         else:
#             print(f'Volume(gas source -- {gas_source}: {volume}')


# LPG Calculation

class LPGCal:

    tema_dens = 0.56
    atoabo_dens = 0.53
    mass_per_price = 0.145

    def __init__(self, price):
        self.price = price

    def lpg_mass(self):
        return self.price * self.mass_per_price

    def lpg_vol(self, gas_source):
        if gas_source.lower() == 'tema':
            volume = (self.price * self.mass_per_price) / self.tema_dens
            return volume
        else:
            volume = (self.price * self.mass_per_price) / self.atoabo_dens
            return volume



# FLASK IMPLEMENTATION

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'GET':
      return(render_template('index.html'))

   if request.method == 'POST':
      amount = float(request.form['amount'])
      gs = str(request.form['gs'])

      calc = LPGCal(amount)
      mass = calc.lpg_mass()
      volume = calc.lpg_vol(gs)

      
      return(render_template('index.html', orignal_input={'Price':amount, 'Gas Source':gs}, m=mass, vol=volume, success = True))


if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/', methods=['POST', 'GET'])
# def results():
# return "The Ma: {}, {}, {}".format(request.form['city1'], request.form['city2'], request.form['city3'])

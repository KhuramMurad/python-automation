'''
# Flask Example
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><h1>Salam</h1><br><body>Asalam o Alykum !!!<br>from Khuram Murad , This is test message through flash module</html>'

if __name__ == '__main__':
    app.run()
'''
# Matplotlib Example
import matplotlib.pyplot as plt

x = [1, 13, 5, 17,9]
y = [10, 13, 16, 19, 22]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

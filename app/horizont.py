import logging
import numpy as np
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import time
import threading


class Hud:
    # ============================================
    def __init__(self):

        self.state = [1000,1000,1000,1000,0.0,0.0,0.0]
        plt.ion()
        self.fig, self.ax1 = plt.subplots(1, 1)
        self.lines = {}

        #self.thread = threading.Thread(target=self._run)
        #self.thread.daemon = True
        self.stopThread = False

    # ===========================================
    def start(self):
        self._initPlot()
        #self.thread.start()

    # ===========================================
    def stop(self):
        self.stopThread = True

    # ===========================================
    def _run(self):
        while True:
            self.update()
            time.sleep(0.01)

    # ===========================================
    def _initPlot(self):

        xah, xaht, xhth = self._linePlots()

        self.lines = {}

        self.lines["engines"] = self.ax1.text(-0.35, 0.8, str(self.state[:4]), color="w")

        self.lines["line_xah0"] = self.ax1.plot(xah[:, 0], xah[:, 1], "w", lw=3)[0]

        for k in range(xhth.shape[0]):
            self.lines["line_xhth{}".format(k)] = self.ax1.plot(
                [xhth[k], xhth[k]], [0.1, -0.1], "w"
            )[0]

        self.lines["blue"] = self.ax1.fill_between(
            [xaht[0, 0], xaht[-1, 0]],
            [1, 1],
            [xaht[0, 1], xaht[-1, 1]],
            facecolor="blue",
        )
        self.lines["brown"] = self.ax1.fill_between(
            [xaht[0, 0], xaht[-1, 0]],
            [-1, -1],
            [xaht[0, 1], xaht[-1, 1]],
            facecolor="brown",
        )

        self.ax1.axis([-1, 1, -1, 1])
        self.ax1.axis("off")
        plt.draw()
        plt.pause(0.01)

        self.fig.canvas.draw()

    # ============================================
    def _linePlots(self):

        PHI = np.deg2rad(self.state[4:7])
        xah, xaht = np.zeros((6, 2)), np.zeros((6, 2))
        xah[0, :] = [-2, 0]
        xah[1, :] = [-0.15, 0]
        xah[2, :] = [-0.1, -0.2]
        xah[3, :] = [0.1, -0.2]
        xah[4, :] = [0.15, 0]
        xah[5, :] = [2, 0]

        for k in range(xah.shape[0]):
            xaht[k, 0] = xah[k, 0] * np.cos(-PHI[0]) + xah[k, 1] * np.sin(-PHI[0])
            xaht[k, 1] = (
                xah[k, 0] * np.sin(--PHI[0])
                + xah[k, 1] * np.cos(-PHI[0])
                + np.sin(--PHI[1])
            )

        xhth = np.linspace(-180, 180, 180) - np.rad2deg(PHI[2])

        return xah, xaht, xhth 

    # ============================================
    def update(self):
        xah, xaht, xhth = self._linePlots()

        self.lines["line_xah0"].set_data(xah[:, 0], xah[:, 1])

        for k in range(xhth.shape[0]):
            self.lines["line_xhth{}".format(k)].set_data([xhth[k], xhth[k]], [0.1, -0.1])

        self.lines["engines"].set_text(str(self.state[:4]))

        self.lines["blue"].remove()
        self.lines["brown"].remove()
        self.lines["blue"] = self.ax1.fill_between(
            [xaht[0, 0], xaht[-1, 0]],
            [1, 1],
            [xaht[0, 1], xaht[-1, 1]],
            facecolor="blue",
        )
        self.lines["brown"] = self.ax1.fill_between(
            [xaht[0, 0], xaht[-1, 0]],
            [-1, -1],
            [xaht[0, 1], xaht[-1, 1]],
            facecolor="brown",
        )

        self.fig.canvas.draw()


    # ============================================


if __name__ == "__main__":
    hud = Hud()
    hud.start()

    print(np.random.rand(3))
    while True:
        hud.state = [1000,1000,1000,1000]+np.random.rand(3).tolist()
        hud.update()
        time.sleep(0.01)
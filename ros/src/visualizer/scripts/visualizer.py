import sys
import time
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph as pg


class App(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        #### Create Gui Elements ###########
        self.mainbox = QtGui.QWidget()
        self.setCentralWidget(self.mainbox)
        self.mainbox.setLayout(QtGui.QVBoxLayout())

        self.canvas = pg.GraphicsLayoutWidget()
        self.mainbox.layout().addWidget(self.canvas)

        self.label = QtGui.QLabel()
        self.mainbox.layout().addWidget(self.label)

        # self.view = self.canvas.addViewBox()
        # self.view.setAspectLocked(True)
        # self.view.setRange(QtCore.QRectF(0, 0, 200, 200))

        #  image plot
        # self.img = pg.ImageItem(border='w')
        # self.view.addItem(self.img)

        # self.canvas.nextRow()
        #  line plot
        self.otherplot = self.canvas.addPlot()
        self.otherplot.setLabel('bottom', text='X', units='m')
        self.otherplot.setLabel('left', text='Y', units='m')
        self.otherplot.showGrid(x=True, y=True, alpha=0.5)
        self.otherplot.setXRange(-1, 1)
        self.otherplot.setYRange(-1, 1)

        self.h1 = self.otherplot.plot(pen='y')
        self.h2 = self.otherplot.plot(pen=None, symbol='o')

        #### Set Data  #####################
        self.theta = np.linspace(0, 1., 100) * np.pi * 2
        self.x = np.cos(self.theta)
        self.y = np.sin(self.theta)
        self.nYaw = 2

        # self.X, self.Y = np.meshgrid(self.x,self.x)
        
        self.h1.setData(self.x, self.y)

        self.counter = 0
        self.fps = 0.
        self.lastupdate = time.time()

        #### Start  #####################
        self._update()

    def _update(self):

        # self.data = np.sin(self.X/3.+self.counter/9.)*np.cos(self.Y/3.+self.counter/9.)
        # self.ydata = np.sin(self.x/3. + self.counter/9.)
        # self.ydata = np.sin(self.x/3. + self.counter)

        # self.img.setImage(self.data)
        # self.h2.setData(self.ydata)

        now = time.time()
        dt = (now-self.lastupdate)
        if dt <= 0:
            dt = 0.000000000001
        fps2 = 1.0 / dt
        self.lastupdate = now
        self.fps = self.fps * 0.9 + fps2 * 0.1
        tx = 'Mean Frame Rate:  {fps:.3f} FPS'.format(fps=self.fps )
        self.label.setText(tx)
        QtCore.QTimer.singleShot(1, self._update)
        self.counter += 1

        self.theta = self.nYaw * now
        self.x = np.cos(self.theta)
        self.y = np.sin(self.theta)

        self.h2.setData([self.x], [self.y])


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    thisapp = App()
    thisapp.show()
    sys.exit(app.exec_())
import matplotlib.pyplot as plt
import numpy as np

def PlotMesh(points, triangles, segment_idex, index_nodes = False, scatted_nodes = False, index_regions = False):
    x, y = points[:, 0], points[:, 1]
    plt.triplot(x, y, triangles, color='green')

    if scatted_nodes:
        plt.scatter(x, y, s=100, c=segment_idex)    

    if index_nodes:
        for point_index in range(len(x)):
            plt.text(x=x[point_index], y=y[point_index], s = point_index, color='red', fontsize=14)

    if index_regions:
        for point_index in range(len(x)):
            plt.text(x=x[point_index], y=y[point_index], s = segment_idex[point_index], color='red', fontsize=14)
    plt.show()

def PlotNodes(points, Fi):
    x, y = points[:, 0], points[:, 1]

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    cf = ax.tricontourf(x,y,Fi)
    fig.colorbar(cf, ax=ax)
    plt.show()

def PlotScatter(points, z):
    x, y = points[:, 0], points[:, 1]

    plt.scatter(x, y, s=100, c=z) 
    plt.show()

def PlotElements(triang, z):
    fig1, ax1 = plt.subplots()
    ax1.set_aspect('equal')
    tpc = ax1.tripcolor(triang, z, shading='flat')
    fig1.colorbar(tpc)
    plt.show()


class CoolPlots:
    def PlotLevel(x, y, F, **kwargs):
        import numpy as np
        import matplotlib.pyplot as plot
        import pylab

        title = kwargs.get("title", "")
        xrange =  kwargs.get("xrange", (-10,10))
        yrange =  kwargs.get("yrange", (-10,10))

        manual = kwargs.get("manual", False)

        levels = []
        if "nlevels" in kwargs:
            nlevels = kwargs["nlevels"]
            indecies = list(filter(lambda i: xrange[0]<=x[i]<=xrange[1] and yrange[0]<=y[i]<=yrange[1], range(len(F))))
            maxF = max(F[indecies])
            minF = min(F[indecies])

            step = (maxF-minF)/nlevels
            levels = np.arange(minF, maxF + step/2, step)
            

        plot.title(title)

        pylab.xlim(xrange)
        pylab.ylim(yrange)

        plot.xlabel('X')
        plot.ylabel('Y')

        if len(levels):
            contours = plot.tricontour(x, y, F, levels = levels)
        else:
            contours = plot.tricontour(x, y, F)

        plot.clabel(contours, inline=1, fontsize=10, manual = manual)

        plot.show()

    def PlotLevelNodes(nodes, F, **kwargs):
        x, y = nodes[:,0], nodes[:,1]
        CoolPlots.PlotLevel(x,y,F, **kwargs)

    def PlotLevelTriangles(nodes, triangles, F, **kwargs):
        XPoints, YPoints = [], []
        for triangle in triangles:
            points = [nodes[node] for node in triangle]
            x, y = sum(points)
            XPoints.append(x/3)
            YPoints.append(y/3)
        
        CoolPlots.PlotLevel(XPoints, YPoints, F, **kwargs)


def main():
    pass

if __name__ == "__main__":
    main()


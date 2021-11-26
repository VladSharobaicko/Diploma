def readPoints(mesh, *segment_files):
    import numpy as np

    points_len = int(mesh.readline())
    points = np.empty((points_len, 2))
    region_tags = np.zeros(points_len)

    for i in range(points_len):
        x, y, z = np.asfarray(mesh.readline().split(), dtype = float)
        points[i] = x,y

    for args in segment_files:
        bordet_segment, segment_tags = args[0], args[1:]
        is_complete = False
        border_len = int(bordet_segment.readline())

        while not is_complete:
            for _ in range(border_len):
                line = np.asfarray(bordet_segment.readline().split(), dtype = float)
                if len(line) == 3:
                    x, y, z = line
                    for point_index in [i for i in range(points_len) if points[i][0]==x and points[i][1]==y]:
                        region_tags[point_index] = segment_tags
            
            last_line = bordet_segment.readline()
            if last_line:
                border_len = int(last_line)
            else:
                is_complete = True
        print(segment_tags)
            

    triangles = []
    triangles_len = int(mesh.readline())
    for i in range(triangles_len):
        a, b, c, _ = mesh.readline().split()
        triangles.append([int(a)-1, int(b)-1, int(c)-1])

    neighbors = [[] for _ in range(points_len)] 
    for point_index in range(points_len):
        for n_triangle, triangle in enumerate(triangles):
            if point_index in triangle:
                neighbors[point_index].append(n_triangle)
        # neighbors[point_index] = list(dict.fromkeys(neighbors[point_index]))
        # if point_index in neighbors[point_index]:
        #     neighbors[point_index].remove(point_index)

    return points, triangles, region_tags, neighbors
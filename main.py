from rlgeom2d import *

def create_shape_1():
    """ create a first shape"""
    r1 = create_rectangle(0, 0, 10, 10)
    r2 = create_rectangle(5, 5, 10, 3)
    r3 = create_rectangle(-5, 0, 7, 2)
    fuse([r1, r2, r3])

def create_shape_2():
    """ create a first shape"""
    r1 = create_rectangle(0, 0, 10, 5)
    r2 = create_rectangle(0, 0, 5, 10)
    fuse([r1, r2])

def create_shape_3():
    """ create a first shape"""
    r1 = create_rectangle(0, 0, 5, 2)
    r2 = create_rectangle(5, 0, 2, 2.2)
    r3 = create_rectangle(1, 0, 1, 2.4)
    r4 = create_rectangle(2, 0, 2, 3)
    r5 = create_rectangle(5, 0, 2, 2.4)
    fuse([r1, r2, r3, r4, r5])


def create_shape_4():
    """ create a first shape"""
    r1 = create_rectangle(0, 0, 2, 1)
    r2 = create_rectangle(-2, 0, 2, 1.1)
    r3 = create_rectangle(-0.1, -2, 1, 2)
    r4 = create_rectangle(0, 0, 1.1, 2)
    fuse([r1, r2, r3, r4])
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # first, we initialize the gmsh environment
    initialize()
    create_shape_1()

    print_infos()
    ## Cut from point 13, face 2 in direction 3 (east)
    cut(13, 2, 3)
    print_infos()
    ## Cut from point 3, face 1 in direction 2 (south)
    cut(3, 1, 2)
    print_infos()

    ## final meshing
    remesh()
    gmsh.write("mesh_gmsh.vtk")
    finalize()


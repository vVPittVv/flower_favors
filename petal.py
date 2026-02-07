import trimesh
import numpy as np

petal = trimesh.creation.icosphere()
num_pets = 50
golden_ratio = (1.0 + np.sqrt(5.0)) / 2.0
golden_angle = 2*3.14159*(1-golden_ratio)

#def petal_param:
    
def gen_petal():
    tmtrx = trimesh.transformations.scale_and_translate([1,5,10])
    petal.apply_transform(tmtrx)

def gen_flower(petal):
    petals = []
    for petal_pos in range(num_pets):
        new_petal = petal.copy()
        # Tilt back
        tmtrx = trimesh.transformations.rotation_matrix((petal_pos/num_pets)*3.14/4, [0,1,0], [0,0,0])
        new_petal.apply_transform(tmtrx)
        # Move into position axially
        tmtrx = trimesh.transformations.scale_and_translate(1,[np.sqrt(petal_pos+1),0,0])
        new_petal.apply_transform(tmtrx)
        # Move into position radially
        tmtrx = trimesh.transformations.rotation_matrix(golden_angle*petal_pos, [0,0,1], [0,0,0])
        new_petal.apply_transform(tmtrx)
        petals += new_petal
    return trimesh.util.concatenate(petals)


def export_petal():
    petal.export('petal.stl')

gen_petal()
flower = gen_flower(petal)
flower.show()

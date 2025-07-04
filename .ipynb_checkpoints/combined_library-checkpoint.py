# combined_library.py

# ------------------------------
# Library for (x, y)
# ------------------------------
library_xy = [
     ## From x variable
    lambda x, y: 1,
    lambda x, y: x,
    lambda x, y: x*y, 
    lambda x, y: x*y/(1 + y),
    
     ## From y variable
    lambda x, y: y,
    lambda x, y: y**2,
    # lambda x, y: x*y,
]

library_names_xy = [
     ## From x variable
    lambda x, y: "1",
    lambda x, y: "x",
    lambda x, y: "xy",
    lambda x, y: "xy/(1+y)",
    
     ## From y variable
    lambda x, y: "y",
    lambda x, y: "y^2",
    # lambda x, y: "xy",
]



# ------------------------------
# Library for (x, y, z), Z = I or N
# ------------------------------
library_xyz = [
     ## From x variable
    lambda x, y, z: 1,
    lambda x, y, z: x,  
    lambda x, y, z: x*y,
    lambda x, y, z: x*z/(1+z), 
    lambda x, y, z: z*y/(1+y),

     ## From y variable
    lambda x, y, z: y,
    lambda x, y, z: y**2,
     # lambda x, y, z: x*y,
    lambda x, y, z: x*y/(1+y),
    
     ## From z variable
    # lambda x, y, z: 1,
    lambda x, y, z: z,
    # lambda x, y, z: x*y/(1+y),
    # lambda x, y, z: z*y/(1+y),
]

library_names_xyz = [
     ## From x variable
    lambda x, y, z: "1",
    lambda x, y, z: "x",  
    lambda x, y, z: "xy",
    lambda x, y, z: "xz/(1+z)", 
    lambda x, y, z: "zy/(1+y)",

     ## From y variable
    lambda x, y, z: "y",
    lambda x, y, z: "y^2",
     # lambda x, y, z: "xy",
    lambda x, y, z: "xy/(1+y)",
    
     ## From z variable
    # lambda x, y, z: "1",
    lambda x, y, z: "z",
    # lambda x, y, z: "xy/(1+y)",
    # lambda x, y, z: "zy/(1+y)",
]

# ------------------------------
# Library for (x, y, z, u), z = I, u = N
# ------------------------------
library_xyzu = [
    lambda x, y, z, u: 1,
    lambda x, y, z, u: x,
    lambda x, y, z, u: x*y,
    lambda x, y, z, u: x*y/(1 + y),
   
    lambda x, y, z, u: y,
    lambda x, y, z, u: y**2,
     # lambda x, y, z, u: x*y,
    # lambda x, y, z, u: x*y/(1 + y),

    # lambda x, y, z, u: 1,
    lambda x, y, z, u: z,
    # lambda x, y, z, u: x*y/(1 + y),
    lambda x, y, z, u: z*y/(1 + y),
        
    lambda x, y, z, u: u,
    lambda x, y, z, u: u*y/(1+y),
]

library_names_xyzu = [
    lambda x, y, z, u: "1",
    lambda x, y, z, u: "x",
    lambda x, y, z, u: "xy",
    lambda x, y, z, u: "xy/(1 + y)",
   
    lambda x, y, z, u: "y",
    lambda x, y, z, u: "y^2",
     # lambda x, y, z, u: "xy",
    # lambda x, y, z, u: "xy/(1 + y)",

    # lambda x, y, z, u: "1",
    lambda x, y, z, u: "z",
    # lambda x, y, z, u: "xy/(1 + y)",
    lambda x, y, z, u: "zy/(1 + y)",
        
    lambda x, y, z, u: "u",
    lambda x, y, z, u: "uy/(1+y)",
]

# ------------------------------
# Utility to return library based on variables
# ------------------------------
def get_library(var_names):
    """
    Returns (library, library_names) given a list of variable names like ['x', 'y'], ['x', 'y', 'z'], etc.
    """

    if var_names == ['x', 'y']:
        return library_xy, library_names_xy

    elif var_names == ['x', 'y', 'z']:
        return library_xyz, library_names_xyz

    elif var_names == ['x', 'y', 'z', 'u']:
        return library_xyzu, library_names_xyzu

    else:
        raise ValueError(f"Unsupported variable set: {var_names}. Supported: ['x','y'], ['x','y','z'], ['x','y','z','u']")

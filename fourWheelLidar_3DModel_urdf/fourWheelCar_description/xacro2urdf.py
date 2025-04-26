import os
import shutil
import urllib.request
import subprocess

def main():
    # Check if the urdf folder exists
    if not os.path.exists("urdf"):
        print("Error, the 'urdf' folder doesn't exist. Please place this script into the same folder as the 'urdf' folder.")
        input("Press Enter to exit...")
        return

    # Get the parent directory name (xxx_description)
    robot_mesh = os.path.basename(os.getcwd())

    # Set robot_name by removing '_description' from robot_mesh
    robot_name = robot_mesh.replace("_description", "")

    # Check if the urdf/<robot_name>.xacro file exists
    xacro_file = os.path.join("urdf", f"{robot_name}.xacro")
    if not os.path.exists(xacro_file):
        print(f"Error, the '{xacro_file}' file doesn't exist.")
        input("Press Enter to exit...")
        return

    # Download xacro.py only if it doesn't exist
    xacro_script = "xacro.py"
    if not os.path.exists(xacro_script):
        url = "https://raw.githubusercontent.com/doctorsrn/xacro2urdf/master/xacro.py"
        urllib.request.urlretrieve(url, xacro_script)

    # Create directories and copy meshes
    urdf_mesh_dir = os.path.join("urdf", robot_mesh, "meshes")
    os.makedirs(urdf_mesh_dir, exist_ok=True)
    if os.path.exists("meshes"):
        shutil.copytree("meshes", urdf_mesh_dir, dirs_exist_ok=True)

    # Run xacro.py to generate the URDF file
    urdf_output = f"{robot_name}.urdf"
    subprocess.run(["python", xacro_script, "-o", urdf_output, xacro_file])

    # Overwrite output directory if it exists
    output_dir = f"{robot_name}_to_unity"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    shutil.move(urdf_output, output_dir)
    shutil.move(os.path.join("urdf", robot_mesh), output_dir)

    print(f"Success. Your files are ready in the folder '{output_dir}'.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

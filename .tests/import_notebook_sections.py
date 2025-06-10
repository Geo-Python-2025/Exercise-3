import nbformat
import types
import copy


def import_notebook(path):
   
    notebook = nbformat.read(str(path), as_version=nbformat.NO_CONVERT)

    namespace = {}
    section_data = {}  # Dictionary to store variables by section
    variables_to_save = ["station_names", "station_start_years","selected_month_index","months","average_temp","print_statement"]  # List of variables to save
    current_section = None  # To track the current section tag

    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            try:
                exec(cell["source"], namespace)
            except Exception:  # Ignore any cell that has any error
                pass

        # Get the section tag, if any, or set to None if not present
        tags = cell.get("metadata", {}).get("tags", [])
        section = tags[0] if tags else None
        
        # Check if the section has changed
        if section and section != current_section:
            current_section = section

        # After executing the cell, check if the variables in variables_to_save exist and save them
        section_data[current_section] = {}

        for var_name in variables_to_save:
            if var_name in namespace:
                # Save a snapshot of the variables to section_data
                section_data[current_section][var_name] = copy.deepcopy(namespace[var_name])

        # Print the section and the variables in variables_to_save
        print(section)
        for var_name in variables_to_save:
            if var_name in namespace:
                print(f"{var_name}: {namespace[var_name]}")

    # Clean up namespace and convert it to SimpleNamespace
    del namespace["__builtins__"]
    namespace = types.SimpleNamespace(**namespace)

    return section_data, namespace
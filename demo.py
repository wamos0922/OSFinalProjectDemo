#Import files.


# Helper function to safely get a float input from the user.
try:
    from ossimg.proc import ( 
        load_image, 
        adjust_brightness, 
        adjust_saturation, 
        adjust_sharpness, 
        adjust_shadows,
        apply_golden_hour,
        apply_gritty_contrast,
        apply_pastel_matte,
        # Import the new manual edit sequence function
        process_manual_edits 
    )
except ImportError:
    print("FATAL ERROR: Library 'ossimg' not found. Please run 'pip3 install -e .' in the ossimg folder.")
    exit(1)

def get_float_input(prompt: str, default_value: float) -> float:
    while True:
        try:
            user_input = input(f"{prompt} (Default: {default_value:.2f}): ")
            if not user_input:
                return default_value
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

# Create a Dummy Image.




# Manual Edit Function





# Main Function
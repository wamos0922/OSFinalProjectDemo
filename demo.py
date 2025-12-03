#Import files.
import os 
from PIL import Image


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
def main():
    INPUT_FILE = "sample_input.png"
    create_dummy_image(INPUT_FILE)
    
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file '{INPUT_FILE}' is missing.")
        return

    try:
        original_img = load_image(INPUT_FILE)
        
        print("\n=======================================================")
        print("    Welcome to the Image Editor Demo")
        print("=======================================================")
        print("Choose an option:")
        print(" 1: Apply 'Golden Hour Warmth' Template (Warm, Soft)")
        print(" 2: Apply 'Urban Gritty Contrast' Template (High Detail, Deep Blacks)")
        print(" 3: Apply 'Soft Pastel Matte' Template (Faded, Bright)")
        print(" 4: Manually Edit All 4 Features (Your custom look)")
        print("=======================================================")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        final_img = None
        output_suffix = None
        
        if choice == '1':
            print("--- Applying Template: Golden Hour Warmth ---")
            final_img = apply_golden_hour(original_img)
            output_suffix = "GOLDEN_HOUR"
        
        elif choice == '2':
            print("--- Applying Template: Urban Gritty Contrast ---")
            final_img = apply_gritty_contrast(original_img)
            output_suffix = "GRITTY_CONTRAST"
            
        elif choice == '3':
            print("--- Applying Template: Soft Pastel Matte ---")
            final_img = apply_pastel_matte(original_img)
            output_suffix = "PASTEL_MATTE"
            
        elif choice == '4':
            final_img = run_manual_edit(original_img)
            output_suffix = "MANUAL_EDIT"

            
        else:
            print("\n⚠️ Invalid choice. Exiting demo.")
            return

        if final_img and output_suffix and choice != '4':
            FINAL_OUTPUT_NAME = f"output_FINAL_{output_suffix}.png"
            final_img.save(FINAL_OUTPUT_NAME)
            print(f"\n✅ Processing complete. Image saved as: {FINAL_OUTPUT_NAME}")

    except Exception as e:
        print(f"\nAn error occurred during image processing: {e}")

if __name__ == "__main__":
    main()
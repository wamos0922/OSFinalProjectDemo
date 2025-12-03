Demonstration Outputs

The `demo.py` script generates two types of output: intermediate previews for manual processing, and final images for both manual and template processing.

1. Intermediate Previews (Manual Feature Chain)

The script applies ***four distinct manual features*** sequentially to the input image, saving a preview after each step. This demonstrates the effect of each feature cumulatively.

| File Name | Description | Feature Applied |
| :--- | :--- | :--- |
| `preview_01_saturation.png` | Result after applying the first feature. | **Saturation Adjustment** |
| `preview_02_shadows.png` | Result after applying the second feature. | **Shadows/Highlights Adjustment** |
| `preview_03_brightness.png` | Result after applying the third feature. | **Brightness Adjustment** |
| `preview_04_sharpness.png` | Result after applying the final fourth feature. | **Sharpness Adjustment** |

2. Final Outputs (Templates & Final Manual Result)

The final saved images include the three prepared templates and the final output of the four-step manual chain.

| File Name | Type | Description |
| :--- | :--- | :--- |
| `output_FINAL_MANUAL.png` | Manual Result | The final output of the 4-step feature chain (identical to `preview_04_sharpness.png`). |
| `output_FINAL_GOLDEN.png` | Template Result | Applies the **"Golden Hour"** template (e.g., increased warmth and contrast). |
| `output_FINAL_GRITTY.png` | Template Result | Applies the **"Gritty Film"** template (e.g., high contrast and reduced color). |
| `output_FINAL_PASTEL.png` | Template Result | Applies the **"Soft Pastel"** template (e.g., lower saturation and brightness). |

---
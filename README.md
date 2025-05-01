
# Qwik

A simple Python script to generate customizable QR codes.

## Features

- Generate QR codes from URLs/text
- Customize color, size, and border
- Save QR codes as PNG images
- Auto-open the generated QR code in your browser

## Demo
![Animated Demo](assets/gif/demo.gif) 

## Examples
Generated using:
```bash
python3 qwik.py https://github.com/silentfin --color red --size 10 --border 1 --open
```
| Default (Black) | Red            | Green          | Blue           |
|-----------------|----------------|----------------|----------------|
| ![Default QR](assets/img/default.png) | ![Red QR](assets/img/red.png) | ![Green QR](assets/img/green.png) | ![Blue QR](assets/img/blue.png) |
| No color flag | `--color red` | `--color green` | `--color blue` |

## Installation  
*Requires Python 3.6 or later.*
1. Clone the repository:  
   ```bash
   git clone git@github.com:silentfin/qwik.git
   cd qwik
   ```

2. Set up a virtual environment:  
   - Linux/macOS:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```  
   - Windows:  
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```  

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
## Usage

- Linux/macOS:  
    ```bash    
    python3 qwik.py "https://example.com" --color red --size 20 --border 2 --output myFolder --open
    ```  
- Windows:  
    ```bash
    python qwik.py "https://example.com" --color red --size 20 --border 2 --output myFolder --open
    ```
## Options
| Argument   | Description                            | Default |
| ---------- | -------------------------------------- | ------- |
| `--color`  | QR code color (e.g., `red`)            | `black` |
| `--size`   | Size (pixels per module)               | `10`    |
| `--border` | Border width (modules)                 | `4`     |
| `--output` | Save to file (e.g., `qr.png`)          | `qr_codes/qr_YYYYMMDD_HHMMSS.png` |
| `--open`   | Auto-open in browser                   | `False` |


**Notes**:
- Run `python3 qwik.py -h` to see all available commands in your terminal
- Default `--output` path: Saves to `qr_codes/qr_YYYYMMDD_HHMMSS.png` (folder auto-created if missing)

## Future Plan

- Make `--output file.png` save directly to the specified filename
- Ensure `--output-dir dir/file.png` saves with pattern `dir/file.png`
- Add support for SVG & JPG output format
- Add batch processing for multiple URLs/text


## License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
# OpenAndClosedWorm

## Movement Analysis Tool

The OpenAndClosedWorm - Movement Analysis Tool is a Python-based application for analyzing and visualizing movement data of C. elegans worms. This tool is developed as part of the OpenWorm project's movement analysis initiative to validate the C. elegans model using real worm movement data.

## Features

- Analyze and visualize movement data of C. elegans worms.
- Implement machine learning algorithms for movement pattern recognition.
- Leverage transfer learning techniques for cross-species comparison and validation.
- Integrate with the Geppetto Simulation Engine for interactive simulation visualization.
- Web-based user interface for easy access and visualization of analysis results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HussainAther/OpenAndClosedWorm
   cd OpenAndClosedWorm
   ```

2. Set up a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Activate the virtual environment
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Upload movement data files in CSV format.
2. Choose analysis options and parameters.
3. Visualize movement patterns and analysis results.
4. Export analysis results for further exploration or sharing.

## File structure

movement_analysis_tool/
│
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
│
├── data/                  # Directory for storing data files
│   └── sample_data.csv    # Sample data file (can be replaced with actual data)
│
├── models/                # Directory for storing trained models (if applicable)
│
├── scripts/               # Directory for additional Python scripts (if needed)
│
├── static/                # Directory for static assets (e.g., CSS, JavaScript)
│   ├── js/
│   │   └── main.js        # Frontend JavaScript code
│   └── css/
│       └── style.css      # CSS stylesheets (if needed)
│
└── templates/             # Directory for HTML templates
    └── index.html         # Main HTML template for the web interface


## Contributing

Contributions to the Movement Analysis Tool project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).

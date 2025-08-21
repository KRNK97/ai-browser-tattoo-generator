# AI History Tattoo Generator

Generate personalized tattoo designs based on your browsing history using AI!

## 🎨 What it does

This project analyzes your Google Chrome browsing history and uses AI to:
1. **Analyze your interests** from visited websites
2. **Generate unique tattoo ideas** based on your online life
3. **Create actual tattoo images** using Stable Diffusion

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed and running (for text generation)
3. **Google Chrome** with browsing history

### Installation

1. **Clone or download** this project
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama** (if not already installed):
   - Download from: https://ollama.ai/
   - Install and run: `ollama serve`
   - Install a model: `ollama pull gemma2:2b`

### Setup

1. **Export your Chrome history**:
   - Go to Chrome Settings → Privacy and Security → Clear browsing data
   - Click "Download your data"
   - Select "Chrome" and download
   - Extract and find the `History.json` file

2. **Place the History.json file** in this project directory

3. **Run the history parser**:
   ```bash
   python history_parser.py
   ```

### Usage

**Run the complete workflow**:
```bash
python main.py
```

This will:
- ✅ Load your browsing history
- ✅ Generate personalized tattoo ideas
- ✅ Create actual tattoo images
- ✅ Save everything to files

## 📁 File Structure

```
ai_history_tattoo_generator/
├── main.py                 # Main script (run this!)
├── history_parser.py       # Parses Chrome history
├── summarize_history.py    # Analyzes browsing patterns
├── generate_prompts.py     # Generates tattoo ideas (legacy)
├── generate_image.py       # Creates images (legacy)
├── History.json           # Your Chrome history (you provide)
├── history_summary.json   # Analyzed history (generated)
├── generated_prompts.json # Generated prompts (generated)
├── tattoo_hf_*.png        # Generated images (generated)
└── requirements.txt       # Python dependencies
```

## 🔧 Configuration

### Changing the AI Model

Edit `main.py` and change the model name:
```python
self.model_name = "gemma2:2b"  # Change to any model you have
```

Popular models:
- `gemma2:2b` (fast, good quality)
- `llama3.2` (better quality, slower)
- `mistral` (balanced)

### Image Generation APIs

The tool supports multiple image generation services:

#### 1. Google Imagen 4.0 API (Primary - Highest Quality)
- **State-of-the-art image generation** with exceptional quality
- **Requires Google AI API token** (paid service)
- **Best results** for detailed, artistic images
- Get your API key from: https://aistudio.google.com/
- Set environment variable:
   ```bash
   # Windows
   set GOOGLE_API_TOKEN=your-token-here
   
   # Linux/Mac
   export GOOGLE_API_TOKEN=your-token-here
   ```

#### 2. ModelsLab API (Fallback)
- **Free tier available** with high-quality results
- **Default API key included** in the code
- **No setup required** - works out of the box
- Get your own key from: https://modelslab.com/

#### 3. Replicate API (Fallback)
For higher quality images, get a free Replicate API token:

1. Sign up at https://replicate.com/
2. Get your API token
3. Set environment variable:
   ```bash
   # Windows
   set REPLICATE_API_TOKEN=your-token-here
   
   # Linux/Mac
   export REPLICATE_API_TOKEN=your-token-here
   ```

#### 4. Hugging Face API (Final Fallback)
- Free tier available
- Get token from: https://huggingface.co/settings/tokens
- Set environment variable:
   ```bash
   # Windows
   set HUGGINGFACE_API_TOKEN=your-token-here
   
   # Linux/Mac
   export HUGGINGFACE_API_TOKEN=your-token-here
   ```

## 🎯 How it Works

1. **History Analysis**: Extracts keywords and domains from your browsing
2. **Prompt Generation**: Uses Ollama to create tattoo ideas based on your interests
3. **Image Creation**: Uses Hugging Face (free) or Replicate (optional) to generate images
4. **Output**: Saves both text ideas and actual tattoo images

## 📊 Output Files

- **`generated_prompts.json`**: Full tattoo ideas with descriptions
- **`tattoo_google_[timestamp].png`**: Generated tattoo images (Google Imagen 4.0 - highest quality)
- **`tattoo_modelslab_[timestamp].png`**: Generated tattoo images (ModelsLab API)
- **`tattoo_replicate_[timestamp].png`**: Higher quality images (if using Replicate)
- **`tattoo_hf_[timestamp].png`**: Generated images (Hugging Face API)
- **`tattoo_placeholder_[timestamp].png`**: Placeholder images (when APIs fail)

## 🛠️ Troubleshooting

### Ollama Issues
```bash
# Check if Ollama is running
ollama list

# Start Ollama
ollama serve

# Install a model
ollama pull gemma2:2b
```

### Missing Dependencies
```bash
pip install -r requirements.txt
```

### No History File
Make sure `History.json` is in the project directory and run:
```bash
python history_parser.py
```

## 🎨 Customization

### Adding New Tattoo Styles

Edit the prompt in `main.py` to include different styles:
```python
prompt = f"""You are a world-class tattoo artist...
Generate 5 unique tattoo ideas with styles like:
- Traditional American
- Japanese Irezumi
- Minimalist
- Geometric
- Watercolor
..."""
```

### Changing Image Generation

Modify the image generation parameters in `main.py`:
```python
# Hugging Face parameters
response = requests.post(
    self.hf_api_url,
    json={
        "inputs": prompt,
        "parameters": {
            "num_inference_steps": 50,
            "guidance_scale": 7.5
        }
    }
)
```

## 📝 License

This project is for educational and personal use. Please respect copyright and use generated images responsibly.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Enjoy your AI-generated tattoos! 🎨✨** 
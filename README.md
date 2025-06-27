# 🚀 Startup Pitch Deck Analyzer

An AI-powered tool that analyzes startup pitch deck PDFs and provides detailed evaluations using OpenAI's GPT-4.

## Features

- **PDF Text Extraction**: Automatically extracts text from uploaded pitch deck PDFs
- **AI-Powered Analysis**: Uses GPT-4 to evaluate startups based on key criteria
- **Team Information Extraction**: Identifies team members, contacts, and qualifications
- **Market Analysis**: Evaluates problem-solution fit, market size, and competitive advantages
- **Traction Assessment**: Analyzes evidence of product-market fit and growth
- **Debug Mode**: Provides detailed error information for troubleshooting

## Analysis Framework

The tool evaluates pitch decks based on five critical questions:

1. **Problem**: What painful problem is this solving, and for whom?
2. **Solution**: Why is this solution uniquely better than existing alternatives?
3. **Market**: How big is the market opportunity, and how fast is it growing?
4. **Traction**: What evidence is there that this works (users, pilots, revenue)?
5. **Team**: Why is this team the right one to win?

## Setup

### Environment Variables

You'll need to set up your OpenAI API key:

```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

### Local Development

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pitch-deck-analyzer.git
cd pitch-deck-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

4. Run the application:
```bash
python app.py
```

The app will launch at `http://localhost:7860`

## Deployment Options

### Hugging Face Spaces (Recommended)

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Choose "Gradio" as the SDK
3. Connect your GitHub repository
4. Add your `OPENAI_API_KEY` in the Space settings under "Variables and secrets"
5. Your app will automatically deploy!

### Railway

1. Connect your GitHub repo to [Railway](https://railway.app)
2. Add `OPENAI_API_KEY` environment variable
3. Railway will automatically deploy your app

### Render

1. Connect your GitHub repo to [Render](https://render.com)
2. Add `OPENAI_API_KEY` environment variable
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`

## Usage

1. Upload one or more PDF pitch deck files
2. Click "Submit" to analyze
3. Review the detailed evaluation results
4. Check the debug output if any errors occur

## File Format Support

- PDF files only
- Multiple files can be uploaded simultaneously
- Text extraction works best with text-based PDFs (not scanned images)

## API Costs

This tool uses OpenAI's GPT-4 API. Costs depend on:
- Length of PDF content
- Number of files processed
- Current OpenAI pricing

Typical cost per pitch deck analysis: $0.10 - $0.50

## Security

- API keys are stored as environment variables (never in code)
- No data is stored permanently
- Files are processed in memory only

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

If you encounter issues:
1. Check the debug output in the app
2. Verify your OpenAI API key is set correctly
3. Ensure your PDF files contain extractable text
4. Open an issue on GitHub with error details

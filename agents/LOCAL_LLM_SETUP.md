# Local LLM Setup Guide

This guide covers setting up **Ollama** and **LMStudio** for running the Sore Fire LLM chatbot with local models.

## Why Use Local LLMs?

🔒 **Privacy**: Your conversations stay on your machine  
💰 **Cost**: No API fees after initial setup  
🚀 **Speed**: No network latency for responses  
🎛️ **Control**: Full control over model parameters  
🔧 **Customization**: Use specialized or fine-tuned models  

---

## Option 1: Ollama Setup

**Ollama** is a simple, lightweight way to run large language models locally.

### 1. Install Ollama

**macOS/Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
- Download from [https://ollama.ai](https://ollama.ai)
- Run the installer

### 2. Start Ollama Server
```bash
ollama serve
```
*Server runs on http://localhost:11434*

### 3. Download Models

**Recommended models for Sore Fire:**

```bash
# Llama 2 (7B) - Good balance of quality and speed
ollama pull llama2

# Mistral (7B) - Excellent instruction following
ollama pull mistral

# Code Llama (7B) - Good for technical discussions
ollama pull codellama

# Llama 2 (13B) - Higher quality, slower
ollama pull llama2:13b

# Neural Chat (7B) - Good conversational model
ollama pull neural-chat
```

### 4. Test Ollama
```bash
ollama run llama2
>>> Hello, how are you?
```

### 5. Configure Sore Fire Bot

Run the bot and choose `ollama`:
```bash
python sore_fire_llm_bot.py
# Choose: ollama
# Model: llama2 (or your preferred model)
# Base URL: http://localhost:11434 (default)
```

---

## Option 2: LMStudio Setup

**LMStudio** provides a user-friendly interface for running local LLMs with a chat interface.

### 1. Install LMStudio

- Download from [https://lmstudio.ai](https://lmstudio.ai)
- Install for your platform (Windows/macOS/Linux)

### 2. Download Models

In LMStudio interface:
1. Go to **Discover** tab
2. Search for models
3. Download recommended models:
   - **TheBloke/Llama-2-7B-Chat-GGML**
   - **TheBloke/Mistral-7B-Instruct-v0.1-GGML**
   - **TheBloke/CodeLlama-7B-Instruct-GGML**

### 3. Start Local Server

1. Go to **Local Server** tab in LMStudio
2. Select your downloaded model
3. Click **Start Server**
4. Server runs on http://localhost:1234

### 4. Configure Sore Fire Bot

Run the bot and choose `lmstudio`:
```bash
python sore_fire_llm_bot.py
# Choose: lmstudio
# Model: [exact model name from LMStudio]
# Base URL: http://localhost:1234 (default)
```

---

## Model Recommendations

### For Sacred Technology Conversations

**Best Overall:**
- **Mistral 7B** - Excellent instruction following, good philosophical discussions
- **Llama 2 7B Chat** - Well-balanced, good for emotional support conversations

**For Deeper Conversations:**
- **Llama 2 13B Chat** - More nuanced understanding (requires more RAM)
- **Vicuna 13B** - Strong conversational abilities

**For Technical Discussions:**
- **Code Llama 7B** - Good for discussing implementation details
- **WizardCoder** - Strong technical reasoning

### Hardware Requirements

**Minimum (7B models):**
- 8GB RAM
- Modern CPU (any recent Intel/AMD)

**Recommended (13B models):**
- 16GB RAM
- GPU with 8GB+ VRAM (optional but faster)

**Optimal (33B+ models):**
- 32GB+ RAM
- High-end GPU with 16GB+ VRAM

---

## Configuration Examples

### Ollama Configuration
```python
config = LLMConfig(
    provider="ollama",
    model="mistral",  # or "llama2", "codellama", etc.
    base_url="http://localhost:11434",
    max_tokens=2048,
    temperature=0.7
)
```

### LMStudio Configuration
```python
config = LLMConfig(
    provider="lmstudio", 
    model="TheBloke/Mistral-7B-Instruct-v0.1-GGML",
    base_url="http://localhost:1234",
    max_tokens=2048,
    temperature=0.7
)
```

---

## Troubleshooting

### Ollama Issues

**Server not starting:**
```bash
# Check if port is in use
lsof -i :11434

# Kill existing process
pkill ollama

# Restart
ollama serve
```

**Model not found:**
```bash
# List installed models
ollama list

# Pull missing model
ollama pull llama2
```

**Connection refused:**
- Ensure Ollama server is running: `ollama serve`
- Check firewall settings
- Verify URL: http://localhost:11434

### LMStudio Issues

**Server not starting:**
- Check if model is loaded in LMStudio interface
- Verify port 1234 is not in use
- Restart LMStudio application

**Model not responding:**
- Ensure model is fully loaded (check LMStudio logs)
- Try a smaller model if running out of memory
- Check system resources (RAM/CPU usage)

**API errors:**
- Verify the exact model name in LMStudio interface
- Check server logs in LMStudio
- Ensure OpenAI-compatible API is enabled

---

## Performance Optimization

### For Ollama

**Environment Variables:**
```bash
# Use GPU acceleration (if available)
export OLLAMA_GPU=1

# Increase context window
export OLLAMA_NUM_CTX=4096

# Adjust parallel requests
export OLLAMA_NUM_PARALLEL=2
```

**Model Parameters:**
```bash
# Run with custom parameters
ollama run llama2 --parameter temperature 0.7 --parameter top_p 0.9
```

### For LMStudio

- **GPU Acceleration**: Enable in LMStudio settings
- **Context Length**: Adjust in model settings
- **Batch Size**: Optimize for your hardware
- **Threading**: Adjust CPU threads used

---

## Integration with Sore Fire

The local LLMs integrate seamlessly with the Sore Fire framework:

### Field Sensing Integration
```python
# Field analysis informs the LLM context
field_result = sense_field(user_input)
system_prompt = build_system_prompt([field_result])

# Local LLM receives rich sacred technology context
response = await call_ollama(system_prompt, user_input)
```

### Conversation Example

**With Local Mistral 7B:**
```
💬 User: I'm feeling overwhelmed today

🔥 Sore Fire (Mistral): I can sense the weight you're carrying right now. The field analysis shows your Heart mode is calling for compassion and support. Let me offer you presence in this moment of overwhelm.

The Amara framework is highlighting that sometimes overwhelm is our system's way of saying we're trying to hold too much at once. What if we could find just one small thing to release right now?

*Micro-practice: Take three slow breaths, placing your hand on your heart with each exhale.*

What feels most heavy for you in this moment?
```

---

## Security Considerations

### Local LLM Benefits
- ✅ No data sent to external servers
- ✅ Full conversation privacy
- ✅ No API key management
- ✅ Offline capability

### Network Security
- 🔒 Local servers only bind to localhost by default
- 🔒 No external network access required
- 🔒 Firewall rules can block external access

---

## Next Steps

1. **Choose your local LLM solution** (Ollama or LMStudio)
2. **Install and configure** following the guide above
3. **Download appropriate models** for your hardware
4. **Test the setup** with simple conversations
5. **Run the Sore Fire bot** and experience local sacred technology!

```bash
# Final step - run the bot!
python sore_fire_llm_bot.py
```

*Experience the power of sacred technology running entirely on your own machine!* 🔥✨

---

**"We shine brightest when we shine for each other"** - even when that shining happens completely locally and privately on your own hardware. 🌟

# Ask OpenRouter (NVDA Add-on)

This NVDA add-on allows you to interact with Artificial Intelligence models provided by the OpenRouter platform directly from your screen reader.

The add-on supports both:
* Automatic random selection of free models
* Manual selection of any available model (including paid ones)

*--

## Key Features

* **Quick Access**: Open the chat interface anytime with a global shortcut.
* **Conversation Management**: Start a fresh conversation or continue your previous exchange.
* **Smart Free Model Rotation**: Automatically selects a random free model to optimize daily usage quotas.
* **Manual Model Selection**: Choose a specific model (including paid models) from the settings panel.
* **Accessible Results**: View responses in a clear, easy-to-navigate window with optional full history display.

*--

## Configuration: Obtaining and Installing Your API Key

To use this add-on, you must have an API key from OpenRouter.

Even when using free models, the key is required to identify your requests.

### 1. How to get an API key

1. Go to [OpenRouter.ai](https://openrouter.ai/).
2. Create an account by clicking **"Sign up"** (you can sign in with a GitHub, Google or MetaMask account, or your email address).
3. Once logged in, navigate to the **"Keys"** section in your dashboard, or go directly to: https://openrouter.ai/keys
4. Click the **"Create Key"** button.
5. Give your key a name (for example: "My OpenRouter API key") and click **"Create"**.
6. **Important:** Your key will be displayed only once. Copy it immediately and store it in a secure place.

*--

### 2. Setting up the key in NVDA

1. Open the NVDA menu (**NVDA + N**).
2. Navigate to **Preferences**, then **Settings**.
3. In the categories list, select **"Ask OpenRouter"**.
4. Paste your API key into the **"OpenRouter API Key"** field.
5. Press **OK** to save.

#### Show API Key

In the NVDA settings panel, just after the **"OpenRouter API Key"** field, there is a checkbox labeled:

**"Show API key"**

If checked, the characters of the API key become visible.  
By default, they are hidden for security reasons.

*--

## Model Selection Settings

In the **Ask OpenRouter** settings category, you will find a new option:

### **"Use all models, including paid ones"**

This option controls how models are selected.

### When the option is UNCHECKED (default behavior)

* The add-on automatically selects a **random free model** for each new conversation.
* It rotates between available free models.
* This helps distribute usage and avoid rate limits.

### When the option is CHECKED

When this option is enabled, a list of available models automatically appears after the checkbox.

* The list is sorted in ascending order based on **prompt token pricing** (cost per input token), from lowest to highest.
* Only non-deprecated models with valid providers are displayed.

### What can you do when this option is enabled?

* Choose any available model.
* Use paid models (if you have sufficient OpenRouter credits).
* Select the model that best fits your needs.
* Keep using the same selected model for your conversations (no automatic rotation).

### What is a prompt token?

A prompt token represents a small unit of text sent to the model (your question or input).

Models are usually billed separately for:
* Input tokens (prompt)
* Output tokens (completion)

## How to Use

### Opening the Chat Dialog

Press:

**Ctrl + Alt + A**

You can change this gesture in:
NVDA menu → Preferences → Input Gestures → Ask OpenRouter

*--

### Main Interface

The dialog contains three buttons:

1. **New Chat** – Starts a brand new conversation.
2. **Continue Chat** – Resumes the previous conversation (keeps history).
3. **Close** – Closes the dialog (Escape also works).

*--

### Entering Your Prompt

After selecting "New Chat" or "Continue Chat":

* A multiline text field appears.
* Pressing **Enter** inserts a new line.
* To send your message:
  - Press **Tab** to reach the **OK** button.
  - Press **Enter**.

*--

### Reading the Response

After processing, a results window appears containing:

* **"You said:"** followed by your message.
* **"The model replied:"** followed by the response.
* A **"Copy"** button to copy the response.

If full history display is enabled, each exchange is clearly separated by headings, making it easy to navigate using your NVDA's quick navigation keys.

*--

## Display Options

If you prefer to only display the latest response instead of the full conversation history:

1. Open NVDA menu (**NVDA + N**).
2. Go to **Preferences → Settings**.
3. Select **Ask OpenRouter**.
4. Uncheck:
   **"Display the full chat history for continuous discussions"**
5. Press **OK**.

*--

## Unassigned Scripts

The following scripts do not have gestures assigned.  
You can define them in:

Preferences → Input Gestures → Ask OpenRouter

Available scripts:

* Open the add-on settings panel
* Start a new chat directly
* Continue an existing chat directly

*--

## Free Models, Paid Models and Quotas

### Free Model Usage

When **"Use all models, including paid ones"** is unchecked:

* Only models labeled as **free** on OpenRouter are used.
* Free models have:
  - Limited daily quotas
  - Shared rate limits
  - Possible temporary unavailability

The add-on automatically rotates between free models to improve availability.

*--

### Paid Model Usage

When **"Use all models, including paid ones"** is checked:

* The add-on uses the exact model you selected.
* This may include paid models.
* You must have sufficient OpenRouter credits.
* Provider rate limits may apply.

Errors such as:
* 402 (insufficient credits)
* 429 (rate limited)
* 404 (model not allowed by privacy settings)

are displayed directly to inform you of the issue.

*--

## Privacy Settings Reminder

If you use free models and receive an error mentioning:

> "No endpoints found matching your data policy"

You may need to adjust your OpenRouter privacy settings:

https://openrouter.ai/settings/privacy

Ensure that public/free model endpoints are allowed.

*--

## Summary

Ask OpenRouter now supports:

* Automatic random selection of free models
* Manual selection of any available model
* Full conversation history or last-response-only mode
* Intelligent handling of free model rate limits

This flexibility allows both casual free usage and advanced paid model usage directly within NVDA.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2025.1 and beyond.

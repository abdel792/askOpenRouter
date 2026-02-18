# Ask OpenRouter (NVDA Add-on)

This NVDA add-on allows you to interact with free Artificial Intelligence models provided by the OpenRouter platform directly from your screen reader.

## Key Features

*   **Quick Access**: Open the chat interface anytime with a global shortcut.
*   **Conversation Management**: Start a fresh conversation or continue your previous exchange.
*   **Smart Model Rotation**: Automatically selects a random free model to optimize your daily usage quotas.
*   **Accessible Results**: View responses in a clear, easy-to-navigate window with a full history.

## Configuration: Obtaining and Installing Your API Key

To use this add-on, you must have an API key from OpenRouter. While the models used by this add-on are free, the key is required to identify your requests.

### 1. How to get a free API key

1.  Go to [OpenRouter.ai](https://openrouter.ai/).
2.  Create an account by clicking **"Sign up"** (you can sign in with a GitHub, Google or MetaMask account, or your email address).
3.  Once logged in, navigate to the **"Keys"** section in your dashboard, or go directly to: [https://openrouter.ai/keys](https://openrouter.ai/keys).
4.  Click the **"Create Key"** button.
5.  Give your key a name (for example: "My first OpenRouter API key") and click **"Create"**.
6.  **Important:** Your key will be displayed only once. Copy it immediately and save it in a secure place.

### 2. Setting up the key in NVDA

1.  Open the NVDA menu (**NVDA + N**).
2.  Navigate to **Preferences**, then **Settings**.
3.  In the categories list, find and select **"Ask OpenRouter"**.
4.  Tab once, you're on the **"OpenRouter API Key"** field and paste your key (the characters of the key are hidden by default).
5.  Press the **OK** button to save.

#### **Noticed**
In the NVDA settings panel, just after the **"OpenRouter API key"** field, there is a checkbox labeled **"Show API key"**.

If you check this box, the characters of the API key should appear, in case you want to view it, or copy it again.

By default, the key characters are always hidden, as a security measure.

## How to Use

### Opening the Chat Dialog
You can open the add-on interface at any time by pressing:
*   **Ctrl + Alt + A**

You can change this gesture in the NVDA preferences menu, in the submenu **"Input gestures"**, and more precisely, in the **"Ask OpenRouter"** category.

### Main interface
The dialog box contains three buttons:
1.  **New Chat**: Starts a brand new conversation.
2.  **Continue Chat**: Resumes your previous conversation (keeping the history so the model remembers the context).
3.  **Close**: Closes the dialog box. You can also press the **Escape** key.

### Entering Your Prompt
After selecting "New Chat" or "Continue Chat," a text input field will appear:
*   **Multiline Field**: This field allows for long messages. Since it is a multiline field, pressing **Enter** will create a new line rather than sending the message.

####   **Sending your message**:
To submit your request, press **Tab** to reach the **OK** button, then press **Enter**.

### Reading the Response
After a brief moment of processing, a results page will appear containing:
*   A section labeled **"You said:"** followed by your question.
*   A section labeled **"The model replied:"** followed by the AI's response.
* A **"Copy"** button to copy the response received.

Depending on the length of your conversation, each exchange in the history will be clearly marked with these headers for easy reading with your screen reader's quick navigation keys

### **Noticed**
If you prefer to always have only one answer to your asked questions, you can configure the add-on so that it only displays the last answer received.

To do this, follow these steps:

1.  Open the NVDA menu (**NVDA + N**).
2.  Navigate to **Preferences**, then **Settings**.
3.  In the categories list, find and select **"Ask OpenRouter"**.
4. Tab until you reach the **"Display the full chat history for continuous discussions"** checkbox, then uncheck it with space.
5.  Press the **OK** button to save.

## Unassigned scripts

The following scripts do not have gestures assigned, you can define them from the preferences menu, "Input gestures" submenu, in the "Ask OpenRouter" category.

* A script to open the add-on settings panel.
* A script to open a dialog to create a new chat.
* A script to open a dialog to continue an existing chat.

## Quotas and Free Models

### Usage Limits
This add-on exclusively uses models listed as "free" on OpenRouter. Please keep in mind:
*   Free models have a **limited daily quota** (a maximum number of messages per day).
*   Please use these models with moderation to avoid hitting your daily limit too quickly.

### Automatic Model Rotation
To help you stay within your limits, the add-on features a **Random Selection** tool. Every time you ask a question, the add-on checks for all currently available free models on OpenRouter and picks one at random. This distributes the load and increases the likelihood of getting a response even if one specific model is currently congested.

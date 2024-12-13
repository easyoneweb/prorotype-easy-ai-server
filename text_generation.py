from llama_cpp import Llama

SYSTEM_PROMPT = "Ты - помощник на русском языке. Выполняй передаваемые тебе инструкции."
SYSTEM_TOKEN = 1788
USER_TOKEN = 1404
BOT_TOKEN = 9225
LINEBREAK_TOKEN = 13

ROLE_TOKENS = {
    'user': USER_TOKEN,
    'bot': BOT_TOKEN,
    'system': SYSTEM_TOKEN
}


def get_message_tokens(model, role, content):
    message_tokens = model.tokenize(content.encode('utf-8'))
    message_tokens.insert(1, ROLE_TOKENS[role])
    message_tokens.insert(2, LINEBREAK_TOKEN)
    message_tokens.append(model.token_eos())
    return message_tokens


def get_system_tokens(model, system_prompt):
    system_message = {
        'role': 'system',
        'content': system_prompt
    }
    return get_message_tokens(model, **system_message)


def get_answer(
        system_prompt,
        prompt,
        temperature,
        n_ctx=8192,
        top_k=30,
        top_p=0.9,
        repeat_penalty=1.1
):
    model = Llama(
        model_path='models/model-q4_K.gguf',
        n_ctx=n_ctx,
        n_parts=1
    )

    model.reset()

    system_tokens = get_system_tokens(model, system_prompt)
    tokens = system_tokens
    model.eval(tokens)

    message_tokens = get_message_tokens(model=model, role='user', content=prompt)
    role_tokens = [model.token_bos(), BOT_TOKEN, LINEBREAK_TOKEN]
    tokens += message_tokens + role_tokens
    generator = model.generate(
        tokens,
        top_k=top_k,
        top_p=top_p,
        temp=temperature,
        repeat_penalty=repeat_penalty
    )

    answer = ''

    for token in generator:
        token_str = model.detokenize([token]).decode('utf-8', errors='ignore')
        tokens.append(token)

        if token == model.token_eos():
            break

        answer += token_str

    return answer

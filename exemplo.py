from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente útil, especialista em desenvolvimento MQL5 e forex que responde em português do Brasil. Seus exemplos de código são sempre completos e com comentários."},
        {
            "role": "user",
            "content": "Escreva um expert que compra e vende no cruzamento do preço com a media de 8. Usamos 3 casas decimais."
        }
    ]
)

print(completion.choices[0].message)
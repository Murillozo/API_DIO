import openai

openai.api_key = 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

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em segurança da informação."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância da segurança da informação (máximo de 50 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })
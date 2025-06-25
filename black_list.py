from datetime import datetime

# Пример списка pers_id (замени на свои значения)
pers_ids = [
#Output возвращенным raw.py вносить сюда
]


# Дата в нужном формате
created_at = updated_at = '2025-06-19'
source = 'external'
reason = 'Умершие'
  # Пример списка ID

# Генерация одного запроса с множественными VALUES
values = ",\n".join(
    [f"('{source}', '{reason}', '{created_at}', '{updated_at}', '{pers_id}')" for pers_id in pers_ids]
)

sql = f"INSERT INTO black_list (source, reason, created_at, updated_at, pers_id_c)\nVALUES\n{values};"

print(sql)



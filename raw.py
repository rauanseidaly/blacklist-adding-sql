def clean_and_format_uuids(raw_uuids):
    uuid_list = raw_uuids.strip().split("\n")
    cleaned_uuids = [uuid.strip() for uuid in uuid_list]
    formatted_uuids = [f'"{uuid}"' for uuid in cleaned_uuids]
    final_uuids_list = "[\n" + ",\n".join(formatted_uuids) + "\n]"
    
    return final_uuids_list
raw_uuids = """
#ИИН СЮДА СПИСКОМ
"""

formatted_uuids = clean_and_format_uuids(raw_uuids)
print(formatted_uuids)

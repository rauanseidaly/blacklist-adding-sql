def clean_and_format_uuids(raw_uuids):
    uuid_list = raw_uuids.strip().split("\n")
    cleaned_uuids = [uuid.strip() for uuid in uuid_list]
    formatted_uuids = [f'"{uuid}"' for uuid in cleaned_uuids]
    final_uuids_list = "[\n" + ",\n".join(formatted_uuids) + "\n]"
    
    return final_uuids_list
raw_uuids = """
600322302766
580319450501
940404400147
640607450411
690222302431
830223303703
880220301968
920210351117
970830350496
620630301627
920922350645
870318300336
810305350221
580519450370
900906301943
821220402429
900921302478
590514300927
060329500548
990601300745
581204300566
730715400312
550103302476
060330502292
"""

formatted_uuids = clean_and_format_uuids(raw_uuids)
print(formatted_uuids)

import csv
def export_to_csv(model, filename):
    # 获取模型的所有字段名
    field_names = [field.name for field in model._meta.fields]

    # 打开CSV文件并写入
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # 写入表头
        writer.writerow(field_names)
        
        # 写入数据行
        for obj in model.objects.all():
            row = [getattr(obj, field) for field in field_names]
            writer.writerow(row)

    print(f"数据已导出到 {filename}")
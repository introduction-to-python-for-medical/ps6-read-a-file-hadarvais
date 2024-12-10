def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()
    new_dict = {}
    for row in rows:
      row = row.strip()
      row = row.split('\t')
      key = row[0]
      value = row[2]
      new_dict[key] = value
    return new_dict



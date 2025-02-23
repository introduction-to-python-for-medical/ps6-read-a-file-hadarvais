def create_codon_dict(file_path):
    file = open(file_path) #נפתח את הקובץ שלנו לתוך משתנה חדש
    rows = file.readlines() #נקרא את כל השורות בקוכץ ונכניס אותן לתוך מחרוזת חדשה
    file.close() #נסגור את הקובץ
    new_dict = {} #נגדיר מילון חדש
    for row in rows: #עבור כל שורה ברשימת השורות
      row = row.strip() #ננקה את השורה
      row = row.split('\t') #נפצל את השורה במקומות הרלוונטיים
      key = row[0] #המפתח של המילון מוחזק בשורה במיקום ה0
      value = row[2]  #הערך מוחזק בשורה במיקום השני
      new_dict[key] = value #נוסיף לרשימה שהגדרנו צמדים של מפתח והערך שתואם לו
    return new_dict #נחזיר את המילון החדש



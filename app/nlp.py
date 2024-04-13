import re

def extract_email_regex(text):
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    matches = re.findall(email_regex, text)
    if matches:
        return matches[0]  # Return the first email address

def extract_phone_regex(text):
    phone_regex_1 = r"\+?\d{2}-?\d{10}"  # Matches numbers like +91-9643544185
    phone_regex_2 = r"\+?\d{2} \d{5} \d{5}"  # Matches numbers like +91 82910 13310
    phone_regex_3 = r"\d{3}-\d{2} \d{5}"  # Matches numbers like 80724 58559
    phone_regex_4 = r"\d{3}-\d{3}-\d{4}"  # Matches numbers like 999-921-8543
    phone_regex_5 = r"\d{10}"  # Matches numbers like 9313653888
    phone_regex_6 = r"\+?\d{2}-?\d{10}"  # Matches numbers like +91-8005955426
    
    matches_1 = re.findall(phone_regex_1, text)
    matches_2 = re.findall(phone_regex_2, text)
    matches_3 = re.findall(phone_regex_3, text)
    matches_4 = re.findall(phone_regex_4, text)
    matches_5 = re.findall(phone_regex_5, text)
    matches_6 = re.findall(phone_regex_6, text)
    
    if matches_1:
        return matches_1[0]
    elif matches_2:
        return matches_2[0]
    elif matches_3:
        return matches_3[0]
    elif matches_4:
        return matches_4[0]
    elif matches_5:
        return matches_5[0]
    elif matches_6:
        return matches_6[0]
    else:
        return None  # Return None if no phone number matches

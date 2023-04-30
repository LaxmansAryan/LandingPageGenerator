from .aigenerator import *


def getDescription(businessName, businessDo, length):
    description = returnsection1Description(businessName, businessDo)
    if len(description) < length:
        return description
    else:
        desc_list = description.split('.')
        if len(desc_list) == 1:
            return description
        while True:
            answer = ''
            for desc in desc_list:
                answer += desc

            if len(answer) > length:
                desc_list.remove(desc_list[len(desc_list)-1])
            else:
                return answer

def limitParagraphLength(description, length):
    if len(description) < length:
        return description
    else:
        desc_list = description.split('.')
        if len(desc_list) == 1:
            return description
        while True:
            answer = ''
            for desc in desc_list:
                answer += desc

            if len(answer) > length:
                desc_list.remove(desc_list[len(desc_list)-1])
            else:
                return answer
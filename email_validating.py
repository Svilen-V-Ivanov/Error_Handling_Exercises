class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


e_mail = input()
domains = {'com', 'bg', 'org', 'net'}
while e_mail != 'End':
    e_mail_parts = e_mail.split('@')

    if len(e_mail_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name = e_mail_parts[0]
        domain = e_mail_parts[1]

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_parts = domain.split('.')
    if len(domain_parts) != 2:
        #Тази проверка я има, за да се избегнат невалидни e-mail като 'abv..bg', 'abv.abv.bg'. По така зададеното
        #условие на задачата '.co.uk' също е невалиден.
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        end_part = domain_parts[1]

    if end_part not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print('Email is valid')
    e_mail = input()

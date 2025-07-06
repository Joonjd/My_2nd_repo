def domain(email, old_domain, new_domain):
    if "@"+old_domain in email:
        index = email.index("@"+old_domain)
        new_id = email[:index]+"@"+new_domain
        return new_id
print(domain("das.joon79@gmail.com", "gmail.com", "yahoo.com"))

#This is our fourth file

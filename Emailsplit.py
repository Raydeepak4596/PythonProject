em=input("Enter your email  ")
(username, domain)=em.split("@")
(domain,extension)=domain.split(".")
print("Username - " + username)
print("Domain  - " + domain)
print("Extension  - " + extension)
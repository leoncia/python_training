class Contact:
    
    def __init__(self, firstname = "firstname",
                        middlename = "middlename",
                        lastname = "lastname",
                        nickname = "nickname",
                        title = "title",
                        company = "company",
                        address = "address",
                        home = "home",
                        mobile = "mobile",
                        work = "work",
                        fax = "fax",
                        email = "email",
                        email2 = "email2",
                        email3 = "email3",
                        homepage = "homepage",
                        address2 = "address2",
                        phone2 = "phone2",
                        notes = "notes"):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

class Date:

    def __init__(self, prefix, day="1", month="April", year="1955"):
        self.prefix = prefix
        self.day = day
        self.month = month
        self.year = year

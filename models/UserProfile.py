class UserProfile:

    # we can calculate age from taking datetime.now() - birthdate
    def __init__(self, UserProfileId, UserTypeCode, Name, School, Major, Street1, Street2, City, StateCode, ZipCode, CountryCode, Phone, Email, BirthDate, ProfileImageUrl):
        self.UserProfileId = UserProfileId
        self.UserTypeCode = UserTypeCode
        self.Name = Name
        self.School = School
        self.Major = Major
        self.Street1 = Street1
        self.Street2 = Street2
        self.City = City
        self.StateCode = StateCode
        self.ZipCode = ZipCode
        self.CountryCode = CountryCode
        self.Phone = Phone
        self.Email = Email
        self.BirthDate = BirthDate
        self.ProfileImageUrl = ProfileImageUrl

    def asdict(self):
        return {'UserProfileId':self.UserProfileId, 'UserTypeCode':self.UserTypeCode, 'Name':self.Name, 'School':self.School, 'Major':self.Major, 'Street1':self.Street1, 'Street2':self.Street2, 'City':self.City, 'StateCode':self.StateCode, 'ZipCode':self.ZipCode, 'CountryCode':self.CountryCode, 'Phone':self.Phone, 'Email':self.Email, 'BirthDate':self.BirthDate, 'ProfileImageUrl':self.ProfileImageUrl}
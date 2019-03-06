# contains SQL queries for database transactions for hacker table.

get = "SELECT * FROM UserProfile WHERE UserProfileId = %s;"

insert = ("INSERT INTO UserProfile "
          "(UserProfileId, UserTypeCode, Name, School, "
          "Major, Street1, Street2, City, "
          "StateCode, ZipCode, CountryCode, "
          "Phone, Email, BirthDate, ProfileImageUrl) "
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")

update = ("UPDATE UserProfile SET "
          "UserTypeCode = %s, "
          "Name = %s, "
          "School = %s, "
          "Major = %s, "
          "Street1 = %s, "
          "Street2 = %s, "
          "City = %s, "
          "StateCode = %s, "
          "ZipCode = %s, "
          "CountryCode = %s, "
          "Phone = %s, "
          "Email = %s, "
          "BirthDate = %s, "
          "ProfileImageUrl = %s "
          "WHERE UserProfileId = %s;")

delete =  "DELETE FROM UserProfile WHERE UserProfileId = %s;"
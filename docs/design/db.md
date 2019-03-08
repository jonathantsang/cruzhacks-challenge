# db.md

## NOTE: this is meant to be viewed in a text editor rather than compiled markdown, sorry!

[UserType]
*UserTypeCode {"label":"varchar(10),not null"} # recs=ADM(Admin),HCK(Hacker),MTR(Mentor),JUD(Judge)
Name {"label":"text,not null"}

[UserProfile]
*UserProfileId {"label":"uuid,not null"}
+UserTypeCode {"label":"varchar(10),not null"}
Name {"label":"varchar(100),not null"}
School {"label":"varchar(100),null"}
Major {"label":"varchar(50),null"}
Street1 {"label":"varchar(100),not null"}
Street2 {"label":"varchar(100),null"}
City {"label":"varchar(50),not null"}
+StateCode {"label":"varchar(2),not null"} # ui:c=autocomplete
ZipCode {"label":"varchar(9),not null"}
CountryCode {"label":"varchar(100),not null"}
Phone {"label":"varchar(20),not null"}
Email {"label":"varchar(100),not null"}
BirthDate {"label":"datetime",not null"}
ProfileImageUrl {"label":"nvarchar(200),null"}

[State]
*StateCode {"label":"nvarchar(2),not null"}
StateName {"label":"nvarchar(50),not null"}
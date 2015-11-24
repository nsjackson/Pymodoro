create table Users(
	User_ID integer,
	Display_Name char(100),
	Email char(100),
	CONSTRAINT users_pk PRIMARY KEY(User_ID)
);

create table Pymodoros(
	Pymodoro_ID integer,
	User_ID integer,
	Start_Time timestamp with time zone,
	End_Time timestamp with time zone,
	CONSTRAINT pymodoros_pk PRIMARY KEY(Pymodoro_ID),
	CONSTRAINT users_fk FOREIGN KEY(User_ID) REFERENCES Users(User_ID)
);
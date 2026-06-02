account_key= input("enter your Developer Account key: ")
raw_text= input("enter the Raw Text Dataset Payload: ")
base= float(input("enter the System Baseline Allocation:"))

cr= len(raw_text)

sa= account_key.strip()
usa= sa.upper()

divide= (cr/4)
G_T_P_F= round(divide*1.25,2)

check=(G_T_P_F > base)

message= "metamatrix data session ingestion"
M= message.upper()
message2= "gateway auth key: "
M2= message2.upper()
message3= "payload scale: "
M3= message3.upper()
message4= "threshold breach:"
M4= message4.upper()

print(f"================================\n ⚡ {M} ⚡\n==================================\n{M2} [{usa}]\n{M3}  [{G_T_P_F}]\n{M4} [{check}]\n======================================")

m = 0.2
d = 0.6 

cyber_grade = m * 65
forensics_grade = m * 68
dssa_grade = m * 54
app_ml_grade = m * 69
prnc_ml_grade = m * 50      ### After resit
pp_grade = m * 50         ###     ...

weighted_modules = (cyber_grade + forensics_grade + dssa_grade + app_ml_grade + prnc_ml_grade + pp_grade)

weighted_diss = d * 60

final_grade = ((weighted_diss + weighted_modules) / 180 )

print(final_grade)
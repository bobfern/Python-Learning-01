from openpyxl import load_workbook
wb2 = load_workbook("/Users/robertof/Box Sync/01 - Projects - Active/IBM - Oi - Unifica/03 - Plans and actuals/010 - Financeiro/300 - Saldos TI Billing/Oi Unifica (17-02-24) - Controle de Sados TI - Billing v0.xlsx")
print (wb2.get_sheet_names())

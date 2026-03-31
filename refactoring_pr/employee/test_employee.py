import pytest
from employee import Address, BankDetails, SalaryCalculation, Employee

def test_address_value_object():
    """Тест Address: форматирование и сравнение (Value Object)"""
    addr1 = Address("ул. Абая 10", "Алматы", "050000", "Казахстан")
    addr2 = Address("ул. Абая 10", "Алматы", "050000", "Казахстан")
    
    assert addr1.format_address() == "ул. Абая 10, Алматы, 050000, Казахстан"
    assert addr1 == addr2  # Проверка, что работает сравнение по значениям

def test_bank_details_info():
    """Тест BankDetails: получение информации"""
    bank = BankDetails("KZ123456789", "Kaspi Bank", "KASPKZ77")
    assert bank.get_info() == "Kaspi Bank KZ123456789 (KASPKZ77)"

def test_salary_calculation_logic():
    """Тест SalaryCalculation: расчет чистой зарплаты"""
    # Данные: база 200к, 10ч переработки, налоги 10%+10%+5% = 25%
    salary = SalaryCalculation(200000, 160, 10, 0.1, 0.1, 0.05)
    # Ожидаемый результат: 164062.5
    assert salary.calculate_net() == 164062.5

def test_employee_integration(capsys):
    """Интеграционный тест Employee: проверяем вызов send_payslip"""
    addr = Address("Ленина 5", "Астана", "010000", "Казахстан")
    bank = BankDetails("ACC777", "Halyk", "HALYKZ22")
    salary = SalaryCalculation(100000, 160, 0, 0.1, 0, 0) # Net 90000
    
    emp = Employee("Амина", "IT", salary, bank, addr)
    emp.send_payslip()
    
    captured = capsys.readouterr()
    assert "Амина paid 90000.0 to Halyk ACC777 (HALYKZ22)" in captured.out
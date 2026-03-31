from dataclasses import dataclass
import logging

# Заглушки внешних сервисов (чтобы код работал)
class PostalService:
    @staticmethod
    def send(address: str, message: str):
        print(f"[PostalService] Отправлено на {address}: {message}")

class BankService:
    @staticmethod
    def transfer(details: str, amount: float):
        print(f"[BankService] Переведено {amount} на счет {details}")

class Logger:
    @staticmethod
    def log(message: str):
        print(f"[Logger] {message}")

# 1) Address.java -> class Address
@dataclass(frozen=True)
class Address:
    street: str
    city: str
    zip_code: str
    country: str

    def format_address(self) -> str:
        return f"{self.street}, {self.city}, {self.zip_code}, {self.country}"

# 2) BankDetails.java -> class BankDetails
@dataclass(frozen=True)
class BankDetails:
    account: str
    name: str
    routing_number: str

    def get_info(self) -> str:
        return f"{self.name} {self.account} ({self.routing_number})"

# 4) SalaryCalculation.java -> class SalaryCalculation
@dataclass
class SalaryCalculation:
    base_salary: float
    hours_worked: int
    overtime_hours: int
    tax_rate: float
    pension_rate: float
    health_insurance_rate: float

    def calculate_net(self) -> float:
        gross = self.base_salary + (self.overtime_hours * self.base_salary / 160 * 1.5)
        deductions = gross * (self.tax_rate + self.pension_rate + self.health_insurance_rate)
        return round(gross - deductions, 2)

# 3) Employee.java -> class Employee
class Employee:
    def __init__(self, name: str, department: str, 
                 salary: SalaryCalculation, 
                 bank_details: BankDetails, 
                 address: Address):
        self.name = name
        self.department = department
        self.salary = salary
        self.bank_details = bank_details
        self.address = address

    def send_payslip(self):
        net = self.salary.calculate_net()
        addr_str = self.address.format_address()
        bank_info = self.bank_details.get_info()

        # Вызов сервисов
        PostalService.send(addr_str, f"Payslip: {net}")
        BankService.transfer(bank_info, net)
        Logger.log(f"{self.name} paid {net} to {bank_info}")
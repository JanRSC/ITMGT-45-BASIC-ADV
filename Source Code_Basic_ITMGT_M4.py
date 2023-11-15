import math

def savings(gross_pay, tax_rate, expenses):
    after_tax_pay = math.floor(gross_pay * (1 - tax_rate))
    remaining_money = after_tax_pay - expenses
    return remaining_money

def material_waste(total_material, material_units, num_jobs, job_consumption):
    waste = num_jobs * job_consumption
    remaining_material = total_material - waste
    result_str = f"{remaining_material}{material_units}"
    return result_str

def interest(principal, rate, periods):
    final_value = math.floor(principal * (1 + rate * periods))
    return final_value

def body_mass_index(weight, height):
    # Convert weight from pounds to kilograms
    weight_kg = weight * 0.453592
    
    # Convert height from imperial to metric
    height_m = (height[0] * 0.3048) + (height[1] * 0.0254)
    
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    
    return bmi

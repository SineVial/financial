#NOTE - this model is INCOMPLETE, and has a number of SIMPLIFYING ASSUMPTIONS baked into it that decrease its accuracy.

YEARS_UNTIL_RETIREMENT = 40
INVESTMENT = 17500
#Note - my model assumes the ENTIRE investment exists within the marginal tax rate.
MARGINAL_TAX_RATE_NOW = 0.25
#Note - my model makes the simplifying assumption that the ENTIRE investment, when taken out, is taxed at the marginal rate instead of the average rate
MARGINAL_TAX_RATE_RETIREMENT = 0.25
APPRECIATION = 1.065


def toPct(decimal):
    return decimal * 100

def main():
    if INVESTMENT > 17500:
        print("IRA Contribution Limit is $17,500 - you entered", INVESTMENT, ", larger than the contribution limit")
    else:
        traditionalTaxSavings = MARGINAL_TAX_RATE_NOW * INVESTMENT
        traditionalInvestment = INVESTMENT + traditionalTaxSavings
        rothInvestment = INVESTMENT

        traditionalPretaxOutcome = traditionalInvestment * (APPRECIATION ** YEARS_UNTIL_RETIREMENT)
        traditionalOutcome = traditionalPretaxOutcome  - traditionalPretaxOutcome * MARGINAL_TAX_RATE_RETIREMENT
        rothOutcome = rothInvestment * (APPRECIATION ** YEARS_UNTIL_RETIREMENT) 

        appreciationPct = (APPRECIATION - 1.0) * 100
        
        print("After", YEARS_UNTIL_RETIREMENT, "years, your investment this year of $", INVESTMENT, "appreciating at", appreciationPct, "% per year, and a marginal tax rate now of ", toPct(MARGINAL_TAX_RATE_NOW), "and a marginal tax rate in retirement of", toPct(MARGINAL_TAX_RATE_RETIREMENT)," you will have $", rothOutcome, "investing in Roth, and $", traditionalOutcome, "investing in traditional")

main()


#! /usr/bin/env python

import argparse
import csv

import tabulate


def main(args):
    """
    The main function.
    """
    coverage = [0.7, 0.8, 0.9]
    deductibles = [100, 250, 500]
    monthly_premiums = {
        (0.7, 100): 36.10,
        (0.7, 250): 28.02,
        (0.7, 500): 23.82,
        (0.8, 100): 40.39,
        (0.8, 250): 31.33,
        (0.8, 500): 26.63,
        (0.9, 100): 50.47,
        (0.9, 250): 39.11,
        (0.9, 500): 33.24,
    }
    sample_vet_bills = range(500, 20_501, 2_000)
    headers = [
        "Vet Bill",
        "Monthly Premium",
        "Annual Premium",
        "Coverage",
        "Deductible",
        "Co-Insurance",
        "Total Annual Spend",
    ]
    table = []
    for coverage in coverage:
        for deductible in deductibles:
            premium = monthly_premiums[(coverage, deductible)]
            for bill in sample_vet_bills:
                annual_premium = premium * 12.0
                co_insurance = (1.0 - coverage) * bill
                total_annual_spend = co_insurance + annual_premium
                row = (
                    bill,
                    premium,
                    annual_premium,
                    coverage,
                    deductible,
                    co_insurance,
                    total_annual_spend,
                )
                table.append(row)
    table.sort(key=lambda x: (x[0], x[6]))
    print(tabulate.tabulate(table, headers=headers, tablefmt="github", floatfmt=".2f"))
    with open("./pet_insurance_stats.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "vet_bill",
                "monthly_premium",
                "annual_premium",
                "coverage",
                "deductible",
                "co_insurance",
                "total_annual_spend",
            ]
        )
        writer.writerows(table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Compute costs for a range of expenses, deductibles, and coverage."
    )
    args = parser.parse_args()
    main(args)

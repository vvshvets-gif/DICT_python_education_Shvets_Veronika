import math
import argparse


def months_to_str(n):
    years, months = divmod(n, 12)
    parts = []
    if years:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if months:
        parts.append(f"{months} month{'s' if months > 1 else ''}")
    return " and ".join(parts)


def calc_diff(principal, periods, interest):
    i = interest / (12 * 100)
    total = 0
    for m in range(1, periods + 1):
        payment = math.ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
        print(f"Month {m}: payment is {payment}")
        total += payment
    print(f"\nOverpayment = {total - principal}")


def calc_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    payment = math.ceil(principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    overpayment = payment * periods - principal
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {overpayment}")


def calc_annuity_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = round(payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    overpayment = payment * periods - principal
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {overpayment}")


def calc_annuity_periods(principal, payment, interest):
    i = interest / (12 * 100)
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    overpayment = payment * n - principal
    print(f"It will take {months_to_str(n)} to repay this loan!")
    print(f"Overpayment = {overpayment}")


def is_valid(args):
    # --interest is always required
    if args.interest is None:
        return False

    # --type must be annuity or diff
    if args.type not in ("annuity", "diff"):
        return False

    # diff doesn't use --payment
    if args.type == "diff" and args.payment is not None:
        return False

    # no negative values allowed
    values = [args.principal, args.payment, args.periods, args.interest]
    if any(v is not None and v < 0 for v in values):
        return False

    # need exactly 3 of the 3 non-type params for diff (principal, periods, interest — all required)
    if args.type == "diff":
        return all(v is not None for v in [args.principal, args.periods, args.interest])

    # for annuity: exactly one of principal/payment/periods may be missing
    annuity_params = [args.principal, args.payment, args.periods]
    return annuity_params.count(None) == 1


parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if not is_valid(args):
    print("Incorrect parameters")
elif args.type == "diff":
    calc_diff(args.principal, args.periods, args.interest)
elif args.principal is None:
    calc_annuity_principal(args.payment, args.periods, args.interest)
elif args.payment is None:
    calc_annuity_payment(args.principal, args.periods, args.interest)
else:
    calc_annuity_periods(args.principal, args.payment, args.interest)

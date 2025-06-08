def calculate_bond_price(face_value, coupon_rate, coupon_frequency, maturity, ytm):
    # Convert percentage inputs to decimals
    coupon_rate /= 100
    ytm /= 100

    if coupon_frequency.lower() == 'annual':
        freq = 1
    elif coupon_frequency.lower() == 'semi-annual':
        freq = 2
    else:
        raise ValueError("Invalid coupon frequency. Please enter 'Annual' or 'Semi-annual'.")

    n_periods = int(maturity * freq)
    coupon_payment = face_value * coupon_rate / freq
    ytm_periodic = ytm / freq

    # Calculate present value of coupon payments
    pv_coupons = sum([coupon_payment / (1 + ytm_periodic)**t for t in range(1, n_periods + 1)])
    
    # Calculate present value of face value
    pv_face = face_value / (1 + ytm_periodic)**n_periods

    bond_price = pv_coupons + pv_face
    return bond_price


# User input
try:
    face_value = float(input("Enter the Face Value of the Bond: "))
    coupon_rate = float(input("Enter the Coupon Rate (in %): "))
    coupon_frequency = input("Enter the Coupon Frequency (Annual/Semi-annual): ").strip()
    maturity = float(input("Enter the Maturity of the Bond (in years): "))
    ytm = float(input("Enter the Yield to Maturity (in %): "))

    price = calculate_bond_price(face_value, coupon_rate, coupon_frequency, maturity, ytm)
    
    print(f"\nThe Bond's price should be {price:.2f} if coupons are paid {coupon_frequency.capitalize()}.")
except ValueError as e:
    print(f"Error: {e}")
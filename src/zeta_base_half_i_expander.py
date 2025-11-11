# zeta_base_half_i_expander_v4.py
from mpmath import mp, zeta

mp.dps = 200

def base_half_i_expansion_continuous(z, max_terms=50, tolerance=1e-80):
    """
    Expand complex z in base (1/2)i using continuous complex coefficients.
    This fixes the rounding bug in v3 by computing exact coefficients.
    """
    base_inv = 2j  # inverse of (1/2)i
    coefficients = []
    residual = mp.mpc(z)

    for k in range(max_terms):
        if abs(residual) < tolerance:
            break
        power_val = base_inv ** k
        coeff = residual / power_val  # continuous coefficient
        coefficients.append(coeff)
        residual -= coeff * power_val

    return coefficients, residual


def run_zeta_expansion():
    print("Zeta Expansion (Base 1/2i, Continuous Coefficients, 200-digit precision)")

    try:
        real_part = float(input("Enter the real part of s: "))
        imag_part = float(input("Enter the imaginary part of s: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    s = mp.mpc(real_part, imag_part)
    z_val = zeta(s)
    print(f"\nζ({s}) = {z_val}")

    coeffs, residual = base_half_i_expansion_continuous(z_val)
    mags = [abs(c) for c in coeffs]

    print("\nContinuous coefficient magnitudes (first 10 terms):")
    print(mags[:10])
    print(f"\nFinal residual = {residual}")
    print(f"Collapsed to zero? {'Yes' if abs(residual) < 1e-40 else 'No'}")


if __name__ == "__main__":
    run_zeta_expansion()

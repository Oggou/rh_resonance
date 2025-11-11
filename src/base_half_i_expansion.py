from mpmath import mp

mp.dps = 100

def base_half_i_expansion(z, max_terms=50, tolerance=1e-80):
    """Expand z in base (1/2)i using continuous coefficients."""
    base_inv = 2j
    coefficients = []
    residual = mp.mpc(z)
    
    for k in range(max_terms):
        if abs(residual) < tolerance:
            break
        power_val = base_inv ** k
        coeff = residual / power_val
        coefficients.append(abs(coeff))
        residual -= coeff * power_val
    return coefficients, residual

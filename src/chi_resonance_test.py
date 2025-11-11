from mpmath import mp, zeta, mpc, power, pi, sin, gamma

mp.dps = 100

def chi(s):
    """χ(s) from functional equation"""
    return (power(2, s) * power(pi, s-1) * 
            sin(pi * s / 2) * gamma(1 - s))

def base_half_i_expansion_fixed(z, max_terms=50, tolerance=1e-80):
    """Expand z in base (1/2)i"""
    base_inv = 2j
    coefficients = []
    residual = mp.mpc(z)
    
    for k in range(max_terms):
        if abs(residual) < tolerance:
            break
        power_val = base_inv ** k
        coeff = residual / power_val
        coefficients.append(float(abs(coeff)))
        residual -= coeff * power_val
    
    return coefficients, residual

def test_chi_structure():
    """Test if χ(s) has special structure related to |χ(s)| = 1"""
    
    t = 14.134725  # First zero height
    sigmas = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]
    
    print("Testing χ(s) structure in base-(1/2)i")
    print("="*80)
    print(f"{'σ':^6} | {'|χ(s)|':^12} | {'|χ|-1':^12} | {'# terms':^8} | {'Max |coeff|':^12}")
    print("-"*80)
    
    results = []
    for sigma in sigmas:
        s = mpc(sigma, t)
        chi_val = chi(s)
        chi_mag = float(abs(chi_val))
        chi_deviation = abs(chi_mag - 1.0)
        
        coeffs, residual = base_half_i_expansion_fixed(chi_val, max_terms=100)
        
        max_coeff = max(coeffs) if len(coeffs) > 0 else 0
        num_terms = len(coeffs)
        
        print(f"{sigma:^6.2f} | {chi_mag:^12.8f} | {chi_deviation:^12.8e} | {num_terms:^8} | {max_coeff:^12.4e}")
        
        results.append({
            'sigma': sigma,
            'chi_mag': chi_mag,
            'chi_dev': chi_deviation,
            'num_terms': num_terms,
            'max_coeff': max_coeff,
            'coeffs': coeffs[:10]  # Store first 10
        })
    
    print("\n" + "="*80)
    print("ANALYSIS")
    print("="*80)
    
    # Check correlation
    import numpy as np
    deviations = [r['chi_dev'] for r in results]
    num_terms_list = [r['num_terms'] for r in results]
    max_coeffs = [r['max_coeff'] for r in results]
    
    corr_terms = np.corrcoef(deviations, num_terms_list)[0,1] if len(set(num_terms_list)) > 1 else 0
    corr_max = np.corrcoef(deviations, max_coeffs)[0,1] if len(set(max_coeffs)) > 1 else 0
    
    print(f"\nCorrelation between |χ|-1 and # terms needed: {corr_terms:.4f}")
    print(f"Correlation between |χ|-1 and max coefficient: {corr_max:.4f}")
    
    print("\nAt σ=0.5 (where |χ|=1):")
    critical = results[4]
    print(f"  |χ(s)| = {critical['chi_mag']:.10f}")
    print(f"  Deviation from 1: {critical['chi_dev']:.4e}")
    print(f"  Terms needed: {critical['num_terms']}")
    print(f"  Max coefficient: {critical['max_coeff']:.4e}")
    print(f"  First 10 coefficients: {[f'{c:.2e}' for c in critical['coeffs']]}")

if __name__ == "__main__":
    test_chi_structure()
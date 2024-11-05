import numpy as np
import flow


class ComponentSplitter:
    def split(
            self,
            f: flow.Flow,
            split_coeffs: np.ndarray
    ) -> flow.Flow:
        new_molar_fractions = f.molar_fractions * split_coeffs
        new_flow = ...
        return ...
    

if __name__ == '__main__':
    ...

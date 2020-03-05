"""#############################################################################
equations.py
================================================================================
Equations from 'Patterns for Parallel Programming'.
#############################################################################"""
import typing as tp

# ------------------------------------------------------------------------------
def computation_time(
    setup_time: int,
    compute_time: int,
    finalization_time: int,
    n_processing_elements: int,
) -> float:
    """
    EQUATION 2.1

    Calculate the time taken to complete a computation consisting of three
    parts - a setup stage, a compute stage, and a finalization stage - as a
    function of how many processing elements the computation takes place on.

    The expression is as follows:

    T_total(P) = T_setup + (T_compute(1) / P) + T_finalization

    where P is the number of processing elements assigned for computation.

    Args:
        setup_time:            The time in seconds for computation setup.
        compute_time:          The time in seconds for computation on a single
                               processing element.
        finalization_time:     The time in seconds for computation finalization.
        n_processing_elements: The number of processing elements assigned for
                               computation.
    
    Returns:
        float:                 The total computation time in seconds.
    """
    return (
        setup_time + (compute_time / n_processing_elements) + finalization_time
    )


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    pass

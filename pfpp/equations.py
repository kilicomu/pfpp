"""#############################################################################
equations.py
================================================================================
Equations from 'Patterns for Parallel Programming'.
#############################################################################"""
import typing as tp

# ------------------------------------------------------------------------------
def computation_time(
    setup_time: tp.Union[int, float],
    compute_time: tp.Union[int, float],
    finalization_time: tp.Union[int, float],
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

    Raises:
        TypeError:             If n_processing_elements is not an int; if any
                               of setup_time, compute_time, finalization_time
                               are not either int or float.
        ValueError:            If any of setup_time, compute_time, finalization_
                               time < 0; if n_processing_elements < 1.
    """
    for arg, value in locals().items():
        if arg in ("setup_time", "compute_time", "finalization_time"):
            error_message = (
                f"{arg} must be an int or float greater than or equal to 0 - "
                "it represents times in seconds"
            )
            if not isinstance(value, (int, float)):
                raise TypeError(error_message)
            if value < 0:
                raise ValueError(error_message)
        if arg == "n_processing_elements":
            error_message = (
                f"{arg} must be an integer greater than 0 - you cannot compute "
                "on nonexistent or fractional processing elements"
            )
            if not isinstance(value, int):
                raise TypeError(error_message)
            if value < 1:
                raise ValueError(error_message)
    return (
        setup_time + (compute_time / n_processing_elements) + finalization_time
    )

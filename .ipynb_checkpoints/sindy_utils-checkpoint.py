# ---------------------------------------------
# Hyperparameter Tuning for SINDy with STLSQ
# Finds the best hyperparameter and fit the SINDy
# ---------------------------------------------

# Import Necessary Libraries
import numpy as np
import pysindy as ps
from tqdm import tqdm

## Define the function
def run_sindy_grid_search(
    x_train,
    t_train,
    custom_library,
    symbolic_names,
    x_test=None,
    t_test=None,
    alpha_range=None,
    threshold_range=None,
    verbose=True,
    use_test_data=False
):
    """
    Perform a grid search over alpha and threshold for SINDy with STLSQ optimizer.

    Parameters
    ----------
    x_train : np.ndarray
        Training data (selected variables only)
    t_train : np.ndarray
        Time array for training data
    custom_library : ps.CustomLibrary
        Fitted custom library (same number of variables as x_train)
    symbolic_names : list of str
        Variable names like ['x', 'y', 'z']
    x_test : np.ndarray, optional
        Test data (optional, used if use_test_data=True)
    t_test : np.ndarray, optional
        Test time vector (optional, used if use_test_data=True)
    alpha_range : array-like, optional
        Range of alpha (L2 regularization strength). Default: logspace(-6, -1)
    threshold_range : array-like, optional
        Range of sparsity thresholds. Default: logspace(-5, -1)
    verbose : bool
        Whether to print progress and best results
    use_test_data : bool
        Whether to score on test data instead of training data

    Returns
    -------
    scores : np.ndarray
        Score matrix (shape: [len(alpha_range), len(threshold_range)])
    best_params : dict
        Dictionary with keys 'alpha', 'threshold', 'score'
    best_model : ps.SINDy
        Trained model with best hyperparameters
    """
    if alpha_range is None:
        alpha_range = np.logspace(-6, -1, num=20)
    if threshold_range is None:
        threshold_range = np.logspace(-5, -1, num=25)

    scores = np.zeros((len(alpha_range), len(threshold_range)))

    for i, alpha in enumerate(tqdm(alpha_range, desc="Alpha values")):
        for j, threshold in enumerate(tqdm(threshold_range, desc="Thresholds", leave=False)):
            optimizer = ps.STLSQ(
                threshold=threshold,
                alpha=alpha,
                max_iter=5000,
                normalize_columns=False
            )

            model = ps.SINDy(
                optimizer=optimizer,
                feature_library=custom_library,
                feature_names=symbolic_names
            )

            model.fit(x_train, t=t_train)

            if use_test_data and x_test is not None and t_test is not None:
                score = model.score(x_test, t=t_test)
            else:
                score = model.score(x_train, t=t_train)

            scores[i, j] = score

    # Find best (alpha, threshold) pair
    best_idx = np.unravel_index(np.argmax(scores), scores.shape)
    best_alpha = alpha_range[best_idx[0]]
    best_threshold = threshold_range[best_idx[1]]
    best_score = scores[best_idx]

    # Re-train best model
    best_optimizer = ps.STLSQ(
        threshold=best_threshold,
        alpha=best_alpha,
        max_iter=5000,
        normalize_columns=False
    )

    best_model = ps.SINDy(
        optimizer=best_optimizer,
        feature_library=custom_library,
        feature_names=symbolic_names
    )
    best_model.fit(x_train, t=t_train)

    best_params = {
        "alpha": best_alpha,
        "threshold": best_threshold,
        "score": best_score
    }

    if verbose:
        print("\n Grid search complete!")
        print(f"  Optimal alpha     : {best_alpha:.1e}")
        print(f"  Optimal threshold : {best_threshold:.1e}")
        print(f"  Optimal score     : {best_score:.6f}")

    return scores, best_params, best_model

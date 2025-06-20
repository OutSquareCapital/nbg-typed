import numpy as np
from numpy.typing import NDArray
from typing import overload

type FloatScalar = np.float64 | np.float32
type NumericScalar = np.float64 | np.float32 | np.int32 | np.int64
type IntArray = NDArray[np.int64] | NDArray[np.int32]
type NumericArray = (
    NDArray[np.float64] | NDArray[np.float32] | np.int32 | NDArray[np.int64]
)

def bfill[T: FloatScalar](
    arr: NDArray[T],
    /,
    *,
    limit: int | None = None,
    axis: int = -1,
) -> NDArray[T]: ...
def ffill[T: FloatScalar](
    arr: NDArray[T],
    /,
    *,
    limit: int | None = None,
    axis: int = -1,
) -> NDArray[T]: ...
def allnan(
    arr: NumericArray,
    /,
    *,
    axis: int,
) -> NDArray[np.bool_]: ...
def anynan(
    arr: NumericArray,
    /,
    *,
    axis: int,
) -> NDArray[np.bool_]: ...
def nancount(
    arr: NumericArray,
    /,
    *,
    axis: int,
) -> NDArray[np.int64]: ...
def nansum[T: NumericScalar](
    arr: NDArray[T],
    /,
    *,
    axis: int,
) -> NDArray[T]: ...
def nanmean[T: FloatScalar](
    arr: NDArray[T],
    /,
    *,
    axis: int,
) -> NDArray[T]: ...
def nanvar[T: FloatScalar](
    arr: NDArray[T],
    /,
    *,
    ddof: int = 1,
    axis: int,
) -> NDArray[T]: ...
def nanstd[T: FloatScalar](
    arr: NDArray[T],
    /,
    *,
    ddof: int = 1,
    axis: int,
) -> NDArray[T]: ...
def nanargmax(arr: NumericArray, /, *, axis: int) -> NDArray[np.int64]: ...
def nanargmin(arr: NumericArray, /, *, axis: int) -> NDArray[np.int64]: ...
@overload
def nanmax(
    arr: NDArray[np.int64] | NDArray[np.int32], /, *, axis: int
) -> NDArray[np.int64]: ...
@overload
def nanmax(arr: NDArray[np.float32], /, *, axis: int) -> NDArray[np.float32]: ...
@overload
def nanmax(arr: NDArray[np.float64], /, *, axis: int) -> NDArray[np.float64]: ...
@overload
def nanmin(
    arr: IntArray, /, *, axis: int
) -> NDArray[np.int64]: ...
@overload
def nanmin(arr: NDArray[np.float32], /, *, axis: int) -> NDArray[np.float32]: ...
@overload
def nanmin(arr: NDArray[np.float64], /, *, axis: int) -> NDArray[np.float64]: ...
@overload
def nanmedian(
    arr: IntArray, /, *, axis: int
) -> NDArray[np.float64]: ...
@overload
def nanmedian(arr: NDArray[np.float32], /, *, axis: int) -> NDArray[np.float32]: ...
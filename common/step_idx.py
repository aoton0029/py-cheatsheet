class StepIdx:
    def __init__(self, start_idx: int = 0) -> None:
        self.current = start_idx

    def step(self) -> None:
        self.current += 1

    @property
    def previous(self) -> int:
        if self.current == 0:
            raise ValueError("`current` was 0 which has no `previous` index.")
        return self.current - 1

    @property
    def next(self) -> int:
        return self.current + 1
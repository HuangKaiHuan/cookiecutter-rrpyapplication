from unittest import mock

from {{ cookiecutter.project_slug }}.presenters.counter_presenter import (
    CounterModel,
    CounterPresenter,
    CounterView,
)


class TestCounterPresenter:
    def setup(self):
        self.view = mock.create_autospec(CounterView)
        self.view.signal_add_pressed = mock.Mock()
        self.view.signal_sub_pressed = mock.Mock()

        self.model = CounterModel()
        self.presenter = CounterPresenter(self.view, self.model)

    def test_add(self):
        self.presenter.add()
        self.view.set_count.assert_called_with(1)

    def test_sub(self):
        self.presenter.sub()
        self.view.set_count.assert_called_with(-1)

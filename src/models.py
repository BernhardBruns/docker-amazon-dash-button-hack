from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class TimeSummary(BaseModel):  # type: ignore
    """Summary for a time interval."""

    summary: str
    before: Optional[str] = None
    image: str


class DashBoardAbsent(BaseModel):  # type: ignore
    """Absent images."""

    summary: str
    image_grid: str
    image_plot: str


class DashboardItem(BaseModel):  # type: ignore
    """Dashboard item."""

    summary: str
    empty_image: str
    absent: List[DashBoardAbsent]


class SheetAction(BaseModel):  # type: ignore
    """Action for a google sheet."""

    type: str
    name: str
    press_sheet: str
    event_sheet: str
    restart: int
    autoclose: int
    default: int


class CalendarAction(BaseModel):  # type: ignore
    """Action for a google calendar."""

    type: str
    calendar_id: str
    dashboard: Optional[str] = None
    restart: int
    autoclose: int
    default: int


class IftttAction(BaseModel):  # type: ignore
    """Action for a IFTTT."""

    type: str
    summary: str
    value1: Optional[str] = ""
    value2: Optional[str] = ""
    value3: Optional[str] = ""


class OpenhabAction(BaseModel):  # type: ignore
    """Action for a OpenHab.""" ""

    type: str
    path: str
    item: str
    command: str


ActionItem = Union[SheetAction, CalendarAction, IftttAction, OpenhabAction]


class ButtonActions(BaseModel):  # type: ignore
    """Actions for a button."""

    summary: Union[str, List[TimeSummary]]
    actions: List[ActionItem]


class Settings(BaseModel):  # type: ignore
    """Settings for the application.""" ""

    latitude: str
    longitude: str
    credentials_file_name: str
    ifttt_key_file_name: str
    openweathermap_key_file_name: str
    images_folder: str
    bounce_delay: int
    dashboards: Dict[str, DashboardItem]
    actions: Dict[str, ButtonActions]

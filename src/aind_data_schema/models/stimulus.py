""" schema for session stimulus """

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import Field

from aind_data_schema.base import AindModel
from aind_data_schema.models.units import (
    ConcentrationUnit,
    FrequencyUnit,
    PowerUnit,
    SoundIntensityUnit,
    TimeUnit,
    VolumeUnit
)


class StimulusModality(str, Enum):
    """Types of stimulus modalities"""

    AUDITORY = "Auditory"
    OLFACTORY = "Olfactory"
    OPTOGENETICS = "Optogenetics"
    NONE = "None"
    VIRTUAL_REALITY = "Virtual reality"
    VISUAL = "Visual"
    WHEEL_FRICTION = "Wheel friction"


class PulseShape(str, Enum):
    """Types of Opto stim pulse shapes"""

    SQUARE = "Square"
    RAMP = "Ramp"
    SINE = "Sinusoidal"


class FilterType(str, Enum):
    """Types of bandpass filters for auditory stim"""

    BUTTERWORTH = "Butterworth"
    OTHER = "Other"


class OptoStimulation(AindModel):
    """Description of opto stimulation parameters"""

    stimulus_name: str = Field(..., title="Stimulus name")
    pulse_shape: PulseShape = Field(..., title="Pulse shape")
    pulse_frequency: int = Field(..., title="Pulse frequency (Hz)")
    pulse_frequency_unit: FrequencyUnit = Field(FrequencyUnit.HZ, title="Pulse frequency unit")
    number_pulse_trains: int = Field(..., title="Number of pulse trains")
    pulse_width: int = Field(..., title="Pulse width (ms)")
    pulse_width_unit: TimeUnit = Field(TimeUnit.MS, title="Pulse width unit")
    pulse_train_duration: Decimal = Field(..., title="Pulse train duration (s)")
    pulse_train_duration_unit: TimeUnit = Field(TimeUnit.S, title="Pulse train duration unit")
    fixed_pulse_train_interval: bool = Field(..., title="Fixed pulse train interval")
    pulse_train_interval: Optional[Decimal] = Field(
        None, title="Pulse train interval (s)", description="Time between pulse trains"
    )
    pulse_train_interval_unit: TimeUnit = Field(TimeUnit.S, title="Pulse train interval unit")
    baseline_duration: Decimal = Field(
        ...,
        title="Baseline duration (s)",
        description="Duration of baseline recording prior to first pulse train",
    )
    baseline_duration_unit: TimeUnit = Field(TimeUnit.S, title="Baseline duration unit")
    other_parameters: Dict[str, Any] = Field(dict())
    notes: Optional[str] = Field(None, title="Notes")


class VisualStimulation(AindModel):
    """Description of visual stimulus parameters. Provides a high level description of stimulus."""

    stimulus_name: str = Field(..., title="Stimulus name")
    stimulus_parameters: Dict[str, Any] = Field(
        dict(),
        title="Stimulus parameters",
        description="Define and list the parameter values used (e.g. all TF or orientation values)",
    )
    stimulus_template_name: List[str] = Field(
        default=[],
        title="Stimulus template name",
        description="Name of image set or movie displayed",
    )
    notes: Optional[str] = Field(None, title="Notes")


class PhotoStimulationGroup(AindModel):
    """Description of a photostimulation group"""

    group_index: int = Field(..., title="Group index")
    number_of_neurons: int = Field(..., title="Number of neurons")
    stimulation_laser_power: Decimal = Field(..., title="Stimulation laser power (mW)")
    stimulation_laser_power_unit: PowerUnit = Field(PowerUnit.MW, title="Stimulation laser power unit")
    number_trials: int = Field(..., title="Number of trials")
    number_spirals: int = Field(..., title="Number of spirals")
    spiral_duration: Decimal = Field(..., title="Spiral duration (s)")
    spiral_duration_unit: TimeUnit = Field(TimeUnit.S, title="Spiral duration unit")
    inter_spiral_interval: Decimal = Field(..., title="Inter trial interval (s)")
    inter_spiral_interval_unit: TimeUnit = Field(TimeUnit.S, title="Inter trial interval unit")
    other_parameters: Dict[str, Any] = Field({})
    notes: Optional[str] = Field(None, title="Notes")


class PhotoStimulation(AindModel):
    """Description of a photostimulation session"""

    stimulus_name: str = Field(..., title="Stimulus name")
    number_groups: int = Field(..., title="Number of groups")
    groups: List[PhotoStimulationGroup] = Field(..., title="Groups")
    inter_trial_interval: Decimal = Field(..., title="Inter trial interval (s)")
    inter_trial_interval_unit: TimeUnit = Field(TimeUnit.S, title="Inter trial interval unit")
    other_parameters: Dict[str, Any] = Field(dict())
    notes: Optional[str] = Field(None, title="Notes")


class OlfactometerChannelConfig(AindModel):
    """Description of olfactometer channel configurations"""

    channel_index: int = Field(..., title="Channel index")
    odorant: str = Field(..., title="Odorant")
    odorant_dilution: Decimal = Field(..., title="Odorant dilution")
    odorant_dilution_unit: ConcentrationUnit = Field(ConcentrationUnit.VOLUME_PERCENT, title="Dilution unit")
    notes: Optional[str] = Field(None, title="Notes")


class OlfactoryStimulation(AindModel):
    """Description of a olfactory stimulus"""

    channels: List[OlfactometerChannelConfig]
    notes: Optional[str] = Field(None, title="Notes")


class AuditoryStimulation(AindModel):
    """Description of an auditory stimulus"""

    sample_frequency: Decimal = Field(..., title="Sample frequency")
    amplitude_modulation_frequency: Optional[int] = Field(None, title="Amplitude modulation frequency")
    frequency_unit: FrequencyUnit = Field(FrequencyUnit.HZ, title="Tone frequency unit")
    bandpass_low_frequency: Optional[Decimal] = Field(None, title="Bandpass low frequency")
    bandpass_high_frequency: Optional[Decimal] = Field(None, title="Bandpass high frequency")
    bandpass_filter_type: Optional[FilterType] = Field(None, title="Bandpass filter type")
    bandpass_order: Optional[int] = Field(None, title="Bandpass order")
    notes: Optional[str] = Field(None, title="Notes")


class StimulusEpoch(AindModel):
    """Description of stimulus used during session"""

    stimulus_start_time: datetime = Field(
        ...,
        title="Stimulus start time",
        description="When a specific stimulus begins. This might be the same as the session start time.",
    )
    stimulus_end_time: datetime = Field(
        ...,
        title="Stimulus end time",
        description="When a specific stimulus ends. This might be the same as the session end time.",
    )
    stimulus_name: str = Field(..., title="Stimulus name")
    session_number: int = Field(..., title="Session number")
    software: List[Software] = Field(
        ...,
        title="Software",
        description="The software used to control the behavior/stimulus (e.g. Bonsai)",
    )
    script: Software = Field(
        ...,
        title="Script",
        description="provide URL to the commit of the script and the parameters used",
    )
    stimulus_modalities: List[StimulusModality] = Field(..., title="Stimulus modalities")
    olfactory_stimulus: Optional[OlfactoryStimulation] = Field(None, title="Olfactory stimulus")
    visual_stimulus: Optional[VisualStimulation] = Field(None, title="Visual stimulus")
    opto_stimulus: Optional[OptoStimulation] = Field(None, title="Optogenetic stimulus")
    auditory_stimulus: Optional[AuditoryStimulation] = Field(None, title="Auditory stimulus")
    output_parameters: Dict[str, Any] = Field(
        ...,
        title="Performance parameters",
        description="Performance metrics from session",
    )
    reward_consumed_during_epoch: Decimal = Field(..., title="Reward consumed during training (uL)")
    reward_consumed_unit: VolumeUnit = Field(VolumeUnit.UL, title="Reward consumed unit")
    trials_total: Optional[int] = Field(None, title="Total trials")
    trials_finished: Optional[int] = Field(None, title="Finished trials")
    trials_rewarded: Optional[int] = Field(None, title="Rewarded trials")
    notes: Optional[str] = Field(None, title="Notes")

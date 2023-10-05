""" example SmartSPIM instrument """
import datetime

from aind_data_schema.device import Manufacturer
from aind_data_schema.imaging.instrument import (
    AdditionalImagingDevice,
    Com,
    Detector,
    Filter,
    Instrument,
    Lightsource,
    MotorizedStage,
    Objective,
    OpticalTable,
    ScanningStage,
)

inst = Instrument(
    instrument_id="SmartSPIM1-3",
    instrument_type="SmartSPIM",
    modification_date=datetime.datetime.now(),
    manufacturer=Manufacturer.LIFECANVAS,
    objectives=[
        Objective(
            numerical_aperture=0.1,
            magnification=1.6,
            immersion="multi",
            manufacturer=Manufacturer.THORLABS,
            model="TL2X-SAP",
            serial_number="Unknown",
            notes="",
        ),
        Objective(
            numerical_aperture=0.2,
            magnification=3.6,
            immersion="multi",
            manufacturer=Manufacturer.THORLABS,
            model="TL4X-SAP",
            serial_number="Unknown",
            notes="Thorlabs TL4X-SAP with LifeCanvas dipping cap and correction optics",
        ),
        Objective(
            numerical_aperture=0.8,
            magnification=16.0,
            immersion="water",
            manufacturer=Manufacturer.NIKON,
            model="MRP07220",
            serial_number="Unknown",
            notes="",
        ),
        Objective(
            numerical_aperture=1.1,
            magnification=25.0,
            immersion="water",
            manufacturer=Manufacturer.NIKON,
            model="MRD77220",
            serial_number="Unknown",
            notes="",
        ),
    ],
    detectors=[
        Detector(
            type="Camera",
            data_interface="USB",
            # chiller -> water circulator / #cooling="air", # Cooling changed to reduce vibration ~ February 01
            cooling="water",
            manufacturer=Manufacturer.HAMAMATSU,
            model="C14440-20UP",
            serial_number="220302-SYS-060443",
        ),
    ],
    light_sources=[
        Lightsource(
            name="Ex_445",
            type="laser",
            coupling="Single-mode fiber",
            wavelength=445,
            max_power=150,
            serial_number="VL08223M03",
            manufacturer=Manufacturer.VORTRAN,
            model="Stradus",
            notes="All lasers controlled via Vortran VersaLase System",
        ),
        Lightsource(
            name="Ex_488",
            type="laser",
            coupling="Single-mode fiber",
            wavelength=488,
            max_power=150,
            serial_number="VL08223M03",
            manufacturer=Manufacturer.VORTRAN,
            model="Stradus",
            notes="All lasers controlled via Vortran VersaLase System",
        ),
        Lightsource(
            name="Ex_561",
            type="laser",
            coupling="Single-mode fiber",
            wavelength=561,
            max_power=150,
            serial_number="VL08223M03",
            manufacturer=Manufacturer.VORTRAN,
            model="Stradus",
            notes="All lasers controlled via Vortran VersaLase System",
        ),
        Lightsource(
            name="Ex_594",
            type="laser",
            coupling="Single-mode fiber",
            wavelength=594,
            max_power=150,
            serial_number="VL08223M03",
            manufacturer=Manufacturer.VORTRAN,
            model="Stradus",
            notes="All lasers controlled via Vortran VersaLase System",
        ),
        Lightsource(
            name="Ex_639",
            type="laser",
            coupling="Single-mode fiber",
            wavelength=639,
            max_power=160,
            serial_number="VL08223M03",
            manufacturer=Manufacturer.VORTRAN,
            model="Stradus",
            notes="All lasers controlled via Vortran VersaLase System",
        ),
        Lightsource(
            name="Ex_665",
            type="laser",
            coupling="Single-mode fiber",
            wavelength=665,
            max_power=160,
            serial_number="VL08223M03",
            manufacturer=Manufacturer.VORTRAN,
            model="Stradus",
            notes="All lasers controlled via Vortran VersaLase System",
        ),
    ],
    motorized_stages=[
        MotorizedStage(
            model="LS-100",
            manufacturer=Manufacturer.ASI,
            serial_number="Unknown-0",
            travel=100,
            notes="Focus stage",
        ),
        MotorizedStage(
            model="L12-20F-4",
            manufacturer=Manufacturer.MIGHTY_ZAP,
            serial_number="Unknown-1",
            travel=41,
            notes="Cylindrical lens #1",
        ),
        MotorizedStage(
            model="L12-20F-4",
            manufacturer=Manufacturer.MIGHTY_ZAP,
            serial_number="Unknown-2",
            travel=41,
            notes="Cylindrical lens #2",
        ),
        MotorizedStage(
            model="L12-20F-4",
            manufacturer=Manufacturer.MIGHTY_ZAP,
            serial_number="Unknown-3",
            travel=41,
            notes="Cylindrical lens #3",
        ),
        MotorizedStage(
            model="L12-20F-4",
            manufacturer=Manufacturer.MIGHTY_ZAP,
            serial_number="Unknown-4",
            travel=41,
            notes="Cylindrical lens #4",
        ),
    ],
    scanning_stages=[
        ScanningStage(
            model="LS-50",
            manufacturer=Manufacturer.ASI,
            serial_number="Unknown-0",
            stage_axis_direction="Detection axis",
            stage_axis_name="Z",
            travel=50,
            notes="Sample stage Z",
        ),
        ScanningStage(
            model="LS-50",
            manufacturer=Manufacturer.ASI,
            serial_number="Unknown-1",
            stage_axis_direction="Illumination axis",
            stage_axis_name="X",
            travel=50,
            notes="Sample stage X",
        ),
        ScanningStage(
            model="LS-50",
            manufacturer=Manufacturer.ASI,
            serial_number="Unknown-2",
            stage_axis_direction="Perpendicular axis",
            stage_axis_name="Y",
            travel=50,
            notes="Sample stage Y",
        ),
    ],
    optical_tables=[
        OpticalTable(  # ~ 3 months ago
            model="VIS3648-PG4-325A",  # model="VIS2424-IG2-125A",
            length=36,  # length=24,
            width=48,  # width=24,
            vibration_control=True,
            manufacturer=Manufacturer.MKS_NEWPORT,
            serial_number="Unknown",
        )
    ],
    humidity_control=False,
    temperature_control=False,
    com_ports=[
        Com(
            hardware_name="Laser Launch",
            com_port="COM3",
        ),
        Com(
            hardware_name="ASI Tiger",
            com_port="COM5",
        ),
        Com(hardware_name="MightyZap", com_port="COM10"),
    ],
    fluorescence_filters=[
        Filter(
            name="Em_469",
            filter_type="Band pass",
            manufacturer=Manufacturer.SEMROCK,
            diameter=25,
            thickness=2.0,
            model="FF01-469/35-25",
            filter_wheel_index=0,
            serial_number="Unknown-0",
        ),
        Filter(
            name="Em_525",
            filter_type="Band pass",
            manufacturer=Manufacturer.SEMROCK,
            diameter=25,
            thickness=2.0,
            model="FF01-525/45-25",
            filter_wheel_index=1,
            serial_number="Unknown-1",
        ),
        Filter(
            name="Em_593",
            filter_type="Band pass",
            manufacturer=Manufacturer.SEMROCK,
            diameter=25,
            thickness=2.0,
            model="FF01-593/40-25",
            filter_wheel_index=2,
            serial_number="Unknown-2",
        ),
        Filter(
            name="Em_624",
            filter_type="Band pass",
            manufacturer=Manufacturer.SEMROCK,
            diameter=25,
            thickness=2.0,
            model="FF01-624/40-25",
            filter_wheel_index=3,
            serial_number="Unknown-3",
        ),
        Filter(
            name="Em_667",
            filter_type="Band pass",
            manufacturer=Manufacturer.CHROMA,
            diameter=25,
            thickness=2.0,
            model="ET667/30m",
            filter_wheel_index=4,
            serial_number="Unknown-4",
        ),
        Filter(
            name="Em_700",
            filter_type="Long pass",
            manufacturer=Manufacturer.THORLABS,
            diameter=25,
            thickness=2.0,
            model="FELH0700",
            filter_wheel_index=5,
            serial_number="Unknown-5",
        ),
    ],
    additional_devices=[
        AdditionalImagingDevice(
            type="Other",
            manufacturer=Manufacturer.JULABO,
            model="200F",
            serial_number="10436130",
        ),
        AdditionalImagingDevice(
            type="Sample Chamber",
            manufacturer=Manufacturer.LIFECANVAS,
            model="Large-uncoated-glass",
            serial_number="Unknown-1",
        ),
    ],
)

inst.write_standard_file(prefix="aind_smartspim")

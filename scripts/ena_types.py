from abc import abstractmethod

from pyxb.binding import generate
import os
from sra import SRA_common_xsd
from sra import SRA_experiment_xsd
from xmljson import yahoo as bf
from json import dumps
from xml.etree.ElementTree import fromstring
from sra import SRA_study_xsd
from sra import SRA_run_xsd
from sra import SRA_sample_xsd



SAMPLE_FILE_NAME = "sample"
STUDY_FILE_NAME = "study"
EXPERIMENT_FILE_NAME = "experiment"
RUN_FILE_NAME = "run"
JSON_FILE_ENDING = ".json"

#def pull_sra_xsds():

#def xsdToPy(input_dir):
#    def generate_code(input_file):
#        generator = generate.Generator()
#        generator.argAddSchemaLocation(join(input_dir, input_file))
#        generator.addModuleName(join(input_dir, input_file.replace('.', '_')))
#        generator.resolveExternalSchema()
#        modules = generator.bindingModules()
#        for m in modules:
#            m.writeToModuleFile()
#        generator.writeNamespaceArchive()

#    from os import listdir
#    from os.path import isfile, join
#    onlyfiles = [file for file in listdir(input_dir) if isfile(join(input_dir, file))  and file.endswith('.xsd') ]
#    map(lambda file: generate_code(file), onlyfiles)
#xsdToPy('/home/pbelmann/projects/CAMISIM/scripts/sra')

class ENA:

    @abstractmethod
    def provide_ena_type_element(self):
        pass

    @abstractmethod
    def build(self):
        pass

    def get_ena_type(self):
        if(self.provide_ena_type_element() == None):
            self.build()
        return self.provide_ena_type_element()


class Study(ENA):

    def __init__(self):
        self.existing_study_type = "Metagenomics"
        self.study_title = ""
        self.center_name = ""
        self.center_project_name = ""
        self.project_id = 0
        self.study_description = ""
        self.study_abstract = ""
        self.ena_study = None

    def existing_study_type(self, type):
        self.existing_study_type = type

    def study_title(self, title):
        self.study_title = title

    def center_name(self, name):
        self.center_name = name

    def center_project_name(self, name):
        self.center_project_name = name

    def study_description(self, description):
        self.study_description = description

    def study_abstract(self, abstract):
        self.study_abstract = abstract

    def provide_ena_type_element(self):
        return self.ena_study

    def build(self):
        study = SRA_study_xsd.StudyType()
        cn = SRA_study_xsd.CTD_ANON_5()
        cn.existing_study_type = self.existing_study_type
        ctd_anon = SRA_study_xsd.CTD_ANON()
        ctd_anon.STUDY_TITLE = self.study_title
        ctd_anon.CENTER_NAME = self.center_name
        ctd_anon.CENTER_PROJECT_NAME = self.center_project_name
        ctd_anon.PROJECT_ID = self.project_id
        ctd_anon.STUDY_DESCRIPTION = self.study_description
        ctd_anon.STUDY_ABSTRACT = self.study_abstract
        ctd_anon.STUDY_TYPE = cn
        study.DESCRIPTOR = ctd_anon
        self.ena_study = study
        return study


class Sample(ENA):

    def __init__(self):
        self.ena_sample = None

    def provide_ena_type_element(self):
        return self.ena_sample

    def build(self):
        cn = SRA_sample_xsd.CTD_ANON()
        cn.TAXON_ID = 0
        sample = SRA_sample_xsd.SampleType()
        sample.SAMPLE_NAME
        sample.TITLE = "title"
        sample.SAMPLE_NAME = cn
        sample.DESCRIPTION = "description"
        self.ena_sample = sample
        return sample


class Run(ENA):

    def __init__(self, experiment):
        self.experiment = experiment
        self.ena_run = None
        self.cn6 = None
        self.files = []

    def provide_ena_type_element(self):
        return self.ena_run

    def add_file(self, name):
        cn4 = SRA_run_xsd.STD_ANON_4("MD5")
        cn6 = SRA_run_xsd.CTD_ANON_6()
        cn6.checksum_method = cn4
        cn6.checksum = "fastq"
        cn6.filetype = SRA_run_xsd.STD_ANON("tab")
        cn6.filename = name
        self.files.append(cn6)

    def build(self):
        cn5 = SRA_run_xsd.CTD_ANON_5(self.experiment.get_ena_type().IDENTIFIERS)
        cn2 = SRA_run_xsd.CTD_ANON_2()
        cn2.FILE = self.files
        cn = SRA_run_xsd.CTD_ANON_()
        cn.FILES = cn2
        run = SRA_run_xsd.RunType()
        run.EXPERIMENT_REF = cn5
        run.DATA_BLOCK = cn
        self.ena_run = run
        return run


class Experiment(ENA):

    def __init__(self, study):
        self.study = study
        self.ena_experiment = None

    def build(self):
        cn = SRA_experiment_xsd.CTD_ANON_9()
        cn.existing_study_type = self.study

        anon = SRA_experiment_xsd.CTD_ANON_()
        anon.MEMBER = "mem"

        sampleType = SRA_experiment_xsd.SampleDescriptorType()
        sampleType.POOL = anon

        strategy = SRA_experiment_xsd.typeLibraryStrategy("WGS")
        source = SRA_experiment_xsd.typeLibrarySource("METAGENOMIC")
        selection = SRA_experiment_xsd.typeLibrarySelection("CAGE")

        layout = SRA_experiment_xsd.CTD_ANON_2()
        layout.SINGLE = SRA_experiment_xsd.CTD_ANON_3()

        libraryDescriptor = SRA_experiment_xsd.LibraryDescriptorType()
        libraryDescriptor.LIBRARY_LAYOUT = layout
        libraryDescriptor.LIBRARY_STRATEGY = strategy
        libraryDescriptor.LIBRARY_SOURCE = source
        libraryDescriptor.LIBRARY_SELECTION = selection

        libraryType = SRA_experiment_xsd.LibraryType()
        libraryType.DESIGN_DESCRIPTION = "test"
        libraryType.SAMPLE_DESCRIPTOR = sampleType
        libraryType.LIBRARY_DESCRIPTOR = libraryDescriptor

        model = SRA_common_xsd.typeIlluminaModel('Illumina HiScanSQ')
        anon7 = SRA_common_xsd.CTD_ANON_7()
        anon7.INSTRUMENT_MODEL = model

        platformType = SRA_common_xsd.PlatformType()
        platformType.ILLUMINA = anon7
        experiment = SRA_experiment_xsd.ExperimentType()
        experiment.TITLE = "title"
        experiment.STUDY_REF = cn
        experiment.PLATFORM = platformType
        experiment.DESIGN = libraryType
        self.ena_experiment = experiment
        return experiment

    def provide_ena_type_element(self):
        return self.ena_experiment


def write(filename, xmlObj, element_name):
    with open(filename, "w") as text_file:
        text_file.write(dumps(bf.data(fromstring(xmlObj.toxml("utf-8", element_name=element_name).decode('utf-8'))), indent=1))


def output(basePath, sample, study, experiment, run):
    map(lambda (x, y, z): write(x, y, z), [
        (os.path.join(basePath, SAMPLE_FILE_NAME + JSON_FILE_ENDING), sample, SAMPLE_FILE_NAME),
        (os.path.join(basePath, STUDY_FILE_NAME + JSON_FILE_ENDING), study, STUDY_FILE_NAME),
        (os.path.join(basePath, RUN_FILE_NAME + JSON_FILE_ENDING), run, RUN_FILE_NAME),
        (os.path.join(basePath, EXPERIMENT_FILE_NAME + JSON_FILE_ENDING), experiment, EXPERIMENT_FILE_NAME)])

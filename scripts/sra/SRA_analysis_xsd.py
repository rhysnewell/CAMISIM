# ./SRA_analysis_xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-12-19 19:18:15.848228 by PyXB version 1.2.6 using Python 2.7.14.final.0
# Namespace AbsentNamespace2

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:fb325a98-e4e8-11e7-811d-1c4d7044c0ff')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import SRA_common_xsd as _ImportedBinding_SRA_common_xsd

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 16, 12)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.tab = STD_ANON._CF_enumeration.addEnumeration(unicode_value='tab', tag='tab')
STD_ANON.bam = STD_ANON._CF_enumeration.addEnumeration(unicode_value='bam', tag='bam')
STD_ANON.bai = STD_ANON._CF_enumeration.addEnumeration(unicode_value='bai', tag='bai')
STD_ANON.cram = STD_ANON._CF_enumeration.addEnumeration(unicode_value='cram', tag='cram')
STD_ANON.crai = STD_ANON._CF_enumeration.addEnumeration(unicode_value='crai', tag='crai')
STD_ANON.vcf = STD_ANON._CF_enumeration.addEnumeration(unicode_value='vcf', tag='vcf')
STD_ANON.vcf_aggregate = STD_ANON._CF_enumeration.addEnumeration(unicode_value='vcf_aggregate', tag='vcf_aggregate')
STD_ANON.bcf = STD_ANON._CF_enumeration.addEnumeration(unicode_value='bcf', tag='bcf')
STD_ANON.tabix = STD_ANON._CF_enumeration.addEnumeration(unicode_value='tabix', tag='tabix')
STD_ANON.wig = STD_ANON._CF_enumeration.addEnumeration(unicode_value='wig', tag='wig')
STD_ANON.bed = STD_ANON._CF_enumeration.addEnumeration(unicode_value='bed', tag='bed')
STD_ANON.gff = STD_ANON._CF_enumeration.addEnumeration(unicode_value='gff', tag='gff')
STD_ANON.fasta = STD_ANON._CF_enumeration.addEnumeration(unicode_value='fasta', tag='fasta')
STD_ANON.fastq = STD_ANON._CF_enumeration.addEnumeration(unicode_value='fastq', tag='fastq')
STD_ANON.flatfile = STD_ANON._CF_enumeration.addEnumeration(unicode_value='flatfile', tag='flatfile')
STD_ANON.chromosome_list = STD_ANON._CF_enumeration.addEnumeration(unicode_value='chromosome_list', tag='chromosome_list')
STD_ANON.sample_list = STD_ANON._CF_enumeration.addEnumeration(unicode_value='sample_list', tag='sample_list')
STD_ANON.readme_file = STD_ANON._CF_enumeration.addEnumeration(unicode_value='readme_file', tag='readme_file')
STD_ANON.phenotype_file = STD_ANON._CF_enumeration.addEnumeration(unicode_value='phenotype_file', tag='phenotype_file')
STD_ANON.BioNano_native = STD_ANON._CF_enumeration.addEnumeration(unicode_value='BioNano_native', tag='BioNano_native')
STD_ANON.Kallisto_native = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Kallisto_native', tag='Kallisto_native')
STD_ANON.agp = STD_ANON._CF_enumeration.addEnumeration(unicode_value='agp', tag='agp')
STD_ANON.unlocalised_list = STD_ANON._CF_enumeration.addEnumeration(unicode_value='unlocalised_list', tag='unlocalised_list')
STD_ANON.info = STD_ANON._CF_enumeration.addEnumeration(unicode_value='info', tag='info')
STD_ANON.other = STD_ANON._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 50, 12)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.MD5 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='MD5', tag='MD5')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 195, 50)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.Whole_genome_sequencing = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Whole genome sequencing', tag='Whole_genome_sequencing')
STD_ANON_2.Exome_sequencing = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Exome sequencing', tag='Exome_sequencing')
STD_ANON_2.Genotyping_by_array = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Genotyping by array', tag='Genotyping_by_array')
STD_ANON_2.transcriptomics = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='transcriptomics', tag='transcriptomics')
STD_ANON_2.Curation = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Curation', tag='Curation')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 227, 48)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.genomic_DNA = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='genomic DNA', tag='genomic_DNA')
STD_ANON_3.genomic_RNA = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='genomic RNA', tag='genomic_RNA')
STD_ANON_3.viral_cRNA = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='viral cRNA', tag='viral_cRNA')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 260, 48)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.BioNano = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='BioNano', tag='BioNano')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Complex type AnalysisSetType with content type ELEMENT_ONLY
class AnalysisSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type AnalysisSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnalysisSetType')
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 78, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ANALYSIS uses Python identifier ANALYSIS
    __ANALYSIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ANALYSIS'), 'ANALYSIS', '__AbsentNamespace2_AnalysisSetType_ANALYSIS', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 80, 12), )

    
    ANALYSIS = property(__ANALYSIS.value, __ANALYSIS.set, None, None)

    _ElementMap.update({
        __ANALYSIS.name() : __ANALYSIS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AnalysisSetType = AnalysisSetType
Namespace.addCategoryObject('typeBinding', 'AnalysisSetType', AnalysisSetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """The type of the analysis. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 180, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element REFERENCE_ALIGNMENT uses Python identifier REFERENCE_ALIGNMENT
    __REFERENCE_ALIGNMENT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'REFERENCE_ALIGNMENT'), 'REFERENCE_ALIGNMENT', '__AbsentNamespace2_CTD_ANON_REFERENCE_ALIGNMENT', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 182, 32), )

    
    REFERENCE_ALIGNMENT = property(__REFERENCE_ALIGNMENT.value, __REFERENCE_ALIGNMENT.set, None, '')

    
    # Element SEQUENCE_VARIATION uses Python identifier SEQUENCE_VARIATION
    __SEQUENCE_VARIATION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SEQUENCE_VARIATION'), 'SEQUENCE_VARIATION', '__AbsentNamespace2_CTD_ANON_SEQUENCE_VARIATION', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 188, 32), )

    
    SEQUENCE_VARIATION = property(__SEQUENCE_VARIATION.value, __SEQUENCE_VARIATION.set, None, None)

    
    # Element SEQUENCE_ASSEMBLY uses Python identifier SEQUENCE_ASSEMBLY
    __SEQUENCE_ASSEMBLY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SEQUENCE_ASSEMBLY'), 'SEQUENCE_ASSEMBLY', '__AbsentNamespace2_CTD_ANON_SEQUENCE_ASSEMBLY', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 216, 32), )

    
    SEQUENCE_ASSEMBLY = property(__SEQUENCE_ASSEMBLY.value, __SEQUENCE_ASSEMBLY.set, None, None)

    
    # Element SEQUENCE_FLATFILE uses Python identifier SEQUENCE_FLATFILE
    __SEQUENCE_FLATFILE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SEQUENCE_FLATFILE'), 'SEQUENCE_FLATFILE', '__AbsentNamespace2_CTD_ANON_SEQUENCE_FLATFILE', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 238, 32), )

    
    SEQUENCE_FLATFILE = property(__SEQUENCE_FLATFILE.value, __SEQUENCE_FLATFILE.set, None, None)

    
    # Element SEQUENCE_ANNOTATION uses Python identifier SEQUENCE_ANNOTATION
    __SEQUENCE_ANNOTATION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SEQUENCE_ANNOTATION'), 'SEQUENCE_ANNOTATION', '__AbsentNamespace2_CTD_ANON_SEQUENCE_ANNOTATION', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 239, 32), )

    
    SEQUENCE_ANNOTATION = property(__SEQUENCE_ANNOTATION.value, __SEQUENCE_ANNOTATION.set, None, '')

    
    # Element REFERENCE_SEQUENCE uses Python identifier REFERENCE_SEQUENCE
    __REFERENCE_SEQUENCE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'REFERENCE_SEQUENCE'), 'REFERENCE_SEQUENCE', '__AbsentNamespace2_CTD_ANON_REFERENCE_SEQUENCE', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 245, 32), )

    
    REFERENCE_SEQUENCE = property(__REFERENCE_SEQUENCE.value, __REFERENCE_SEQUENCE.set, None, None)

    
    # Element SAMPLE_PHENOTYPE uses Python identifier SAMPLE_PHENOTYPE
    __SAMPLE_PHENOTYPE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SAMPLE_PHENOTYPE'), 'SAMPLE_PHENOTYPE', '__AbsentNamespace2_CTD_ANON_SAMPLE_PHENOTYPE', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 248, 32), )

    
    SAMPLE_PHENOTYPE = property(__SAMPLE_PHENOTYPE.value, __SAMPLE_PHENOTYPE.set, None, '')

    
    # Element PROCESSED_READS uses Python identifier PROCESSED_READS
    __PROCESSED_READS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROCESSED_READS'), 'PROCESSED_READS', '__AbsentNamespace2_CTD_ANON_PROCESSED_READS', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 254, 32), )

    
    PROCESSED_READS = property(__PROCESSED_READS.value, __PROCESSED_READS.set, None, None)

    
    # Element GENOME_MAP uses Python identifier GENOME_MAP
    __GENOME_MAP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GENOME_MAP'), 'GENOME_MAP', '__AbsentNamespace2_CTD_ANON_GENOME_MAP', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 255, 32), )

    
    GENOME_MAP = property(__GENOME_MAP.value, __GENOME_MAP.set, None, None)

    
    # Element AMR_ANTIBIOGRAM uses Python identifier AMR_ANTIBIOGRAM
    __AMR_ANTIBIOGRAM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AMR_ANTIBIOGRAM'), 'AMR_ANTIBIOGRAM', '__AbsentNamespace2_CTD_ANON_AMR_ANTIBIOGRAM', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 271, 32), )

    
    AMR_ANTIBIOGRAM = property(__AMR_ANTIBIOGRAM.value, __AMR_ANTIBIOGRAM.set, None, None)

    
    # Element PATHOGEN_ANALYSIS uses Python identifier PATHOGEN_ANALYSIS
    __PATHOGEN_ANALYSIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PATHOGEN_ANALYSIS'), 'PATHOGEN_ANALYSIS', '__AbsentNamespace2_CTD_ANON_PATHOGEN_ANALYSIS', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 272, 32), )

    
    PATHOGEN_ANALYSIS = property(__PATHOGEN_ANALYSIS.value, __PATHOGEN_ANALYSIS.set, None, None)

    
    # Element TRANSCRIPTOME_ASSEMBLY uses Python identifier TRANSCRIPTOME_ASSEMBLY
    __TRANSCRIPTOME_ASSEMBLY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TRANSCRIPTOME_ASSEMBLY'), 'TRANSCRIPTOME_ASSEMBLY', '__AbsentNamespace2_CTD_ANON_TRANSCRIPTOME_ASSEMBLY', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 273, 32), )

    
    TRANSCRIPTOME_ASSEMBLY = property(__TRANSCRIPTOME_ASSEMBLY.value, __TRANSCRIPTOME_ASSEMBLY.set, None, None)

    _ElementMap.update({
        __REFERENCE_ALIGNMENT.name() : __REFERENCE_ALIGNMENT,
        __SEQUENCE_VARIATION.name() : __SEQUENCE_VARIATION,
        __SEQUENCE_ASSEMBLY.name() : __SEQUENCE_ASSEMBLY,
        __SEQUENCE_FLATFILE.name() : __SEQUENCE_FLATFILE,
        __SEQUENCE_ANNOTATION.name() : __SEQUENCE_ANNOTATION,
        __REFERENCE_SEQUENCE.name() : __REFERENCE_SEQUENCE,
        __SAMPLE_PHENOTYPE.name() : __SAMPLE_PHENOTYPE,
        __PROCESSED_READS.name() : __PROCESSED_READS,
        __GENOME_MAP.name() : __GENOME_MAP,
        __AMR_ANTIBIOGRAM.name() : __AMR_ANTIBIOGRAM,
        __PATHOGEN_ANALYSIS.name() : __PATHOGEN_ANALYSIS,
        __TRANSCRIPTOME_ASSEMBLY.name() : __TRANSCRIPTOME_ASSEMBLY
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 217, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element NAME uses Python identifier NAME
    __NAME = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NAME'), 'NAME', '__AbsentNamespace2_CTD_ANON__NAME', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 219, 44), )

    
    NAME = property(__NAME.value, __NAME.set, None, None)

    
    # Element PARTIAL uses Python identifier PARTIAL
    __PARTIAL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PARTIAL'), 'PARTIAL', '__AbsentNamespace2_CTD_ANON__PARTIAL', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 220, 44), )

    
    PARTIAL = property(__PARTIAL.value, __PARTIAL.set, None, None)

    
    # Element COVERAGE uses Python identifier COVERAGE
    __COVERAGE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'COVERAGE'), 'COVERAGE', '__AbsentNamespace2_CTD_ANON__COVERAGE', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 221, 44), )

    
    COVERAGE = property(__COVERAGE.value, __COVERAGE.set, None, None)

    
    # Element PROGRAM uses Python identifier PROGRAM
    __PROGRAM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROGRAM'), 'PROGRAM', '__AbsentNamespace2_CTD_ANON__PROGRAM', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 222, 44), )

    
    PROGRAM = property(__PROGRAM.value, __PROGRAM.set, None, None)

    
    # Element PLATFORM uses Python identifier PLATFORM
    __PLATFORM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PLATFORM'), 'PLATFORM', '__AbsentNamespace2_CTD_ANON__PLATFORM', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 223, 44), )

    
    PLATFORM = property(__PLATFORM.value, __PLATFORM.set, None, None)

    
    # Element MIN_GAP_LENGTH uses Python identifier MIN_GAP_LENGTH
    __MIN_GAP_LENGTH = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MIN_GAP_LENGTH'), 'MIN_GAP_LENGTH', '__AbsentNamespace2_CTD_ANON__MIN_GAP_LENGTH', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 224, 44), )

    
    MIN_GAP_LENGTH = property(__MIN_GAP_LENGTH.value, __MIN_GAP_LENGTH.set, None, None)

    
    # Element MOL_TYPE uses Python identifier MOL_TYPE
    __MOL_TYPE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MOL_TYPE'), 'MOL_TYPE', '__AbsentNamespace2_CTD_ANON__MOL_TYPE', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 226, 44), )

    
    MOL_TYPE = property(__MOL_TYPE.value, __MOL_TYPE.set, None, None)

    _ElementMap.update({
        __NAME.name() : __NAME,
        __PARTIAL.name() : __PARTIAL,
        __COVERAGE.name() : __COVERAGE,
        __PROGRAM.name() : __PROGRAM,
        __PLATFORM.name() : __PLATFORM,
        __MIN_GAP_LENGTH.name() : __MIN_GAP_LENGTH,
        __MOL_TYPE.name() : __MOL_TYPE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 243, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 246, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 252, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 256, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PROGRAM uses Python identifier PROGRAM
    __PROGRAM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROGRAM'), 'PROGRAM', '__AbsentNamespace2_CTD_ANON_5_PROGRAM', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 258, 44), )

    
    PROGRAM = property(__PROGRAM.value, __PROGRAM.set, None, None)

    
    # Element PLATFORM uses Python identifier PLATFORM
    __PLATFORM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PLATFORM'), 'PLATFORM', '__AbsentNamespace2_CTD_ANON_5_PLATFORM', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 259, 44), )

    
    PLATFORM = property(__PLATFORM.value, __PLATFORM.set, None, None)

    
    # Element DESCRIPTION uses Python identifier DESCRIPTION
    __DESCRIPTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DESCRIPTION'), 'DESCRIPTION', '__AbsentNamespace2_CTD_ANON_5_DESCRIPTION', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 266, 44), )

    
    DESCRIPTION = property(__DESCRIPTION.value, __DESCRIPTION.set, None, None)

    _ElementMap.update({
        __PROGRAM.name() : __PROGRAM,
        __PLATFORM.name() : __PLATFORM,
        __DESCRIPTION.name() : __DESCRIPTION
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Files associated with the
                                        analysis."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 283, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element FILE uses Python identifier FILE
    __FILE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FILE'), 'FILE', '__AbsentNamespace2_CTD_ANON_6_FILE', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 286, 36), )

    
    FILE = property(__FILE.value, __FILE.set, None, None)

    _ElementMap.update({
        __FILE.name() : __FILE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """ Links to resources related to this analysis.
                    """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 299, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ANALYSIS_LINK uses Python identifier ANALYSIS_LINK
    __ANALYSIS_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ANALYSIS_LINK'), 'ANALYSIS_LINK', '__AbsentNamespace2_CTD_ANON_7_ANALYSIS_LINK', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 301, 32), )

    
    ANALYSIS_LINK = property(__ANALYSIS_LINK.value, __ANALYSIS_LINK.set, None, None)

    _ElementMap.update({
        __ANALYSIS_LINK.name() : __ANALYSIS_LINK
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Properties and attributes of an analysis. These can be
                        entered as free-form tag-value pairs."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 311, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ANALYSIS_ATTRIBUTE uses Python identifier ANALYSIS_ATTRIBUTE
    __ANALYSIS_ATTRIBUTE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ANALYSIS_ATTRIBUTE'), 'ANALYSIS_ATTRIBUTE', '__AbsentNamespace2_CTD_ANON_8_ANALYSIS_ATTRIBUTE', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 313, 32), )

    
    ANALYSIS_ATTRIBUTE = property(__ANALYSIS_ATTRIBUTE.value, __ANALYSIS_ATTRIBUTE.set, None, None)

    _ElementMap.update({
        __ANALYSIS_ATTRIBUTE.name() : __ANALYSIS_ATTRIBUTE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type AnalysisFileType with content type EMPTY
class AnalysisFileType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type AnalysisFileType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnalysisFileType')
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 6, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__AbsentNamespace2_AnalysisFileType_filename', pyxb.binding.datatypes.string, required=True)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 7, 8)
    __filename._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 7, 8)
    
    filename = property(__filename.value, __filename.set, None, 'The file name. ')

    
    # Attribute filetype uses Python identifier filetype
    __filetype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filetype'), 'filetype', '__AbsentNamespace2_AnalysisFileType_filetype', _module_typeBindings.STD_ANON, required=True)
    __filetype._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 12, 8)
    __filetype._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 12, 8)
    
    filetype = property(__filetype.value, __filetype.set, None, 'The type of the file.')

    
    # Attribute checksum_method uses Python identifier checksum_method
    __checksum_method = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'checksum_method'), 'checksum_method', '__AbsentNamespace2_AnalysisFileType_checksum_method', _module_typeBindings.STD_ANON_, required=True)
    __checksum_method._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 46, 8)
    __checksum_method._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 46, 8)
    
    checksum_method = property(__checksum_method.value, __checksum_method.set, None, 'The checksum method. ')

    
    # Attribute checksum uses Python identifier checksum
    __checksum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'checksum'), 'checksum', '__AbsentNamespace2_AnalysisFileType_checksum', pyxb.binding.datatypes.string, required=True)
    __checksum._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 61, 8)
    __checksum._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 61, 8)
    
    checksum = property(__checksum.value, __checksum.set, None, 'The file checksum.')

    
    # Attribute unencrypted_checksum uses Python identifier unencrypted_checksum
    __unencrypted_checksum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unencrypted_checksum'), 'unencrypted_checksum', '__AbsentNamespace2_AnalysisFileType_unencrypted_checksum', pyxb.binding.datatypes.string)
    __unencrypted_checksum._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 66, 8)
    __unencrypted_checksum._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 66, 8)
    
    unencrypted_checksum = property(__unencrypted_checksum.value, __unencrypted_checksum.set, None, 'The checksum of the unencrypted file (used in conjunction with the checksum of an encrypted file).\n                ')

    
    # Attribute checklist uses Python identifier checklist
    __checklist = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'checklist'), 'checklist', '__AbsentNamespace2_AnalysisFileType_checklist', pyxb.binding.datatypes.string)
    __checklist._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 72, 8)
    __checklist._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 72, 8)
    
    checklist = property(__checklist.value, __checklist.set, None, 'The name of the checklist.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __filename.name() : __filename,
        __filetype.name() : __filetype,
        __checksum_method.name() : __checksum_method,
        __checksum.name() : __checksum,
        __unencrypted_checksum.name() : __unencrypted_checksum,
        __checklist.name() : __checklist
    })
_module_typeBindings.AnalysisFileType = AnalysisFileType
Namespace.addCategoryObject('typeBinding', 'AnalysisFileType', AnalysisFileType)


# Complex type AnalysisType with content type ELEMENT_ONLY
class AnalysisType (_ImportedBinding_SRA_common_xsd.ObjectType):
    """A SRA analysis object captures sequence analysis results including sequence alignments, sequence variations and sequence annotations.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnalysisType')
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 89, 4)
    _ElementMap = _ImportedBinding_SRA_common_xsd.ObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_SRA_common_xsd.ObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_SRA_common_xsd.ObjectType
    
    # Element TITLE uses Python identifier TITLE
    __TITLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TITLE'), 'TITLE', '__AbsentNamespace2_AnalysisType_TITLE', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 97, 20), )

    
    TITLE = property(__TITLE.value, __TITLE.set, None, 'Title of the analysis object which will be displayed in\n                        search results. ')

    
    # Element DESCRIPTION uses Python identifier DESCRIPTION
    __DESCRIPTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DESCRIPTION'), 'DESCRIPTION', '__AbsentNamespace2_AnalysisType_DESCRIPTION', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 103, 20), )

    
    DESCRIPTION = property(__DESCRIPTION.value, __DESCRIPTION.set, None, 'Describes the analysis in detail.')

    
    # Element STUDY_REF uses Python identifier STUDY_REF
    __STUDY_REF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_REF'), 'STUDY_REF', '__AbsentNamespace2_AnalysisType_STUDY_REF', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 108, 20), )

    
    STUDY_REF = property(__STUDY_REF.value, __STUDY_REF.set, None, 'Identifies the parent study.')

    
    # Element SAMPLE_REF uses Python identifier SAMPLE_REF
    __SAMPLE_REF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SAMPLE_REF'), 'SAMPLE_REF', '__AbsentNamespace2_AnalysisType_SAMPLE_REF', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 118, 20), )

    
    SAMPLE_REF = property(__SAMPLE_REF.value, __SAMPLE_REF.set, None, 'One of more samples associated with the\n                        analysis.')

    
    # Element EXPERIMENT_REF uses Python identifier EXPERIMENT_REF
    __EXPERIMENT_REF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_REF'), 'EXPERIMENT_REF', '__AbsentNamespace2_AnalysisType_EXPERIMENT_REF', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 135, 20), )

    
    EXPERIMENT_REF = property(__EXPERIMENT_REF.value, __EXPERIMENT_REF.set, None, None)

    
    # Element RUN_REF uses Python identifier RUN_REF
    __RUN_REF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RUN_REF'), 'RUN_REF', '__AbsentNamespace2_AnalysisType_RUN_REF', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 142, 20), )

    
    RUN_REF = property(__RUN_REF.value, __RUN_REF.set, None, 'One or more runs associated with the\n                        analysis.')

    
    # Element ANALYSIS_REF uses Python identifier ANALYSIS_REF
    __ANALYSIS_REF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ANALYSIS_REF'), 'ANALYSIS_REF', '__AbsentNamespace2_AnalysisType_ANALYSIS_REF', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 159, 20), )

    
    ANALYSIS_REF = property(__ANALYSIS_REF.value, __ANALYSIS_REF.set, None, 'One or more runs associated with the\n                        analysis.')

    
    # Element ANALYSIS_TYPE uses Python identifier ANALYSIS_TYPE
    __ANALYSIS_TYPE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ANALYSIS_TYPE'), 'ANALYSIS_TYPE', '__AbsentNamespace2_AnalysisType_ANALYSIS_TYPE', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 176, 20), )

    
    ANALYSIS_TYPE = property(__ANALYSIS_TYPE.value, __ANALYSIS_TYPE.set, None, 'The type of the analysis. ')

    
    # Element FILES uses Python identifier FILES
    __FILES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FILES'), 'FILES', '__AbsentNamespace2_AnalysisType_FILES', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 278, 24), )

    
    FILES = property(__FILES.value, __FILES.set, None, 'Files associated with the\n                                        analysis.')

    
    # Element ANALYSIS_LINKS uses Python identifier ANALYSIS_LINKS
    __ANALYSIS_LINKS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ANALYSIS_LINKS'), 'ANALYSIS_LINKS', '__AbsentNamespace2_AnalysisType_ANALYSIS_LINKS', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 294, 20), )

    
    ANALYSIS_LINKS = property(__ANALYSIS_LINKS.value, __ANALYSIS_LINKS.set, None, ' Links to resources related to this analysis.\n                    ')

    
    # Element ANALYSIS_ATTRIBUTES uses Python identifier ANALYSIS_ATTRIBUTES
    __ANALYSIS_ATTRIBUTES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ANALYSIS_ATTRIBUTES'), 'ANALYSIS_ATTRIBUTES', '__AbsentNamespace2_AnalysisType_ANALYSIS_ATTRIBUTES', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 306, 20), )

    
    ANALYSIS_ATTRIBUTES = property(__ANALYSIS_ATTRIBUTES.value, __ANALYSIS_ATTRIBUTES.set, None, 'Properties and attributes of an analysis. These can be\n                        entered as free-form tag-value pairs.')

    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}ObjectType
    
    # Attribute analysis_center uses Python identifier analysis_center
    __analysis_center = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'analysis_center'), 'analysis_center', '__AbsentNamespace2_AnalysisType_analysis_center', pyxb.binding.datatypes.string)
    __analysis_center._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 319, 16)
    __analysis_center._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 319, 16)
    
    analysis_center = property(__analysis_center.value, __analysis_center.set, None, 'If applicable, the center name of the institution responsible\n                    for this analysis. ')

    
    # Attribute analysis_date uses Python identifier analysis_date
    __analysis_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'analysis_date'), 'analysis_date', '__AbsentNamespace2_AnalysisType_analysis_date', pyxb.binding.datatypes.dateTime)
    __analysis_date._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 325, 16)
    __analysis_date._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 325, 16)
    
    analysis_date = property(__analysis_date.value, __analysis_date.set, None, 'The date when this analysis was produced. ')

    
    # Attribute alias inherited from {SRA.common}ObjectType
    
    # Attribute center_name inherited from {SRA.common}ObjectType
    
    # Attribute broker_name inherited from {SRA.common}ObjectType
    
    # Attribute accession inherited from {SRA.common}ObjectType
    _ElementMap.update({
        __TITLE.name() : __TITLE,
        __DESCRIPTION.name() : __DESCRIPTION,
        __STUDY_REF.name() : __STUDY_REF,
        __SAMPLE_REF.name() : __SAMPLE_REF,
        __EXPERIMENT_REF.name() : __EXPERIMENT_REF,
        __RUN_REF.name() : __RUN_REF,
        __ANALYSIS_REF.name() : __ANALYSIS_REF,
        __ANALYSIS_TYPE.name() : __ANALYSIS_TYPE,
        __FILES.name() : __FILES,
        __ANALYSIS_LINKS.name() : __ANALYSIS_LINKS,
        __ANALYSIS_ATTRIBUTES.name() : __ANALYSIS_ATTRIBUTES
    })
    _AttributeMap.update({
        __analysis_center.name() : __analysis_center,
        __analysis_date.name() : __analysis_date
    })
_module_typeBindings.AnalysisType = AnalysisType
Namespace.addCategoryObject('typeBinding', 'AnalysisType', AnalysisType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (_ImportedBinding_SRA_common_xsd.RefObjectType):
    """Identifies the parent study."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 112, 24)
    _ElementMap = _ImportedBinding_SRA_common_xsd.RefObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_SRA_common_xsd.RefObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_SRA_common_xsd.RefObjectType
    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}RefObjectType
    
    # Attribute refname inherited from {SRA.common}RefObjectType
    
    # Attribute refcenter inherited from {SRA.common}RefObjectType
    
    # Attribute accession inherited from {SRA.common}RefObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (_ImportedBinding_SRA_common_xsd.RefObjectType):
    """One of more samples associated with the
                        analysis."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 123, 24)
    _ElementMap = _ImportedBinding_SRA_common_xsd.RefObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_SRA_common_xsd.RefObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_SRA_common_xsd.RefObjectType
    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}RefObjectType
    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__AbsentNamespace2_CTD_ANON_10_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 126, 36)
    __label._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 126, 36)
    
    label = property(__label.value, __label.set, None, 'A label associating the sample with sample references in data files.')

    
    # Attribute refname inherited from {SRA.common}RefObjectType
    
    # Attribute refcenter inherited from {SRA.common}RefObjectType
    
    # Attribute accession inherited from {SRA.common}RefObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __label.name() : __label
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (_ImportedBinding_SRA_common_xsd.RefObjectType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 136, 24)
    _ElementMap = _ImportedBinding_SRA_common_xsd.RefObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_SRA_common_xsd.RefObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_SRA_common_xsd.RefObjectType
    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}RefObjectType
    
    # Attribute refname inherited from {SRA.common}RefObjectType
    
    # Attribute refcenter inherited from {SRA.common}RefObjectType
    
    # Attribute accession inherited from {SRA.common}RefObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (_ImportedBinding_SRA_common_xsd.RefObjectType):
    """One or more runs associated with the
                        analysis."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 147, 24)
    _ElementMap = _ImportedBinding_SRA_common_xsd.RefObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_SRA_common_xsd.RefObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_SRA_common_xsd.RefObjectType
    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}RefObjectType
    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__AbsentNamespace2_CTD_ANON_12_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 150, 36)
    __label._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 150, 36)
    
    label = property(__label.value, __label.set, None, 'A label associating the run with run references in data files.')

    
    # Attribute refname inherited from {SRA.common}RefObjectType
    
    # Attribute refcenter inherited from {SRA.common}RefObjectType
    
    # Attribute accession inherited from {SRA.common}RefObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __label.name() : __label
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (_ImportedBinding_SRA_common_xsd.RefObjectType):
    """One or more runs associated with the
                        analysis."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 164, 24)
    _ElementMap = _ImportedBinding_SRA_common_xsd.RefObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_SRA_common_xsd.RefObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding_SRA_common_xsd.RefObjectType
    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}RefObjectType
    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__AbsentNamespace2_CTD_ANON_13_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 167, 36)
    __label._UseLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 167, 36)
    
    label = property(__label.value, __label.set, None, 'A label associating the analysis with analysis references in data files.')

    
    # Attribute refname inherited from {SRA.common}RefObjectType
    
    # Attribute refcenter inherited from {SRA.common}RefObjectType
    
    # Attribute accession inherited from {SRA.common}RefObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __label.name() : __label
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (_ImportedBinding_SRA_common_xsd.ReferenceSequenceType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 189, 36)
    _ElementMap = _ImportedBinding_SRA_common_xsd.ReferenceSequenceType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_SRA_common_xsd.ReferenceSequenceType._AttributeMap.copy()
    # Base type is _ImportedBinding_SRA_common_xsd.ReferenceSequenceType
    
    # Element EXPERIMENT_TYPE uses Python identifier EXPERIMENT_TYPE
    __EXPERIMENT_TYPE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_TYPE'), 'EXPERIMENT_TYPE', '__AbsentNamespace2_CTD_ANON_14_EXPERIMENT_TYPE', True, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 193, 50), )

    
    EXPERIMENT_TYPE = property(__EXPERIMENT_TYPE.value, __EXPERIMENT_TYPE.set, None, None)

    
    # Element PROGRAM uses Python identifier PROGRAM
    __PROGRAM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROGRAM'), 'PROGRAM', '__AbsentNamespace2_CTD_ANON_14_PROGRAM', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 205, 50), )

    
    PROGRAM = property(__PROGRAM.value, __PROGRAM.set, None, None)

    
    # Element PLATFORM uses Python identifier PLATFORM
    __PLATFORM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PLATFORM'), 'PLATFORM', '__AbsentNamespace2_CTD_ANON_14_PLATFORM', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 207, 50), )

    
    PLATFORM = property(__PLATFORM.value, __PLATFORM.set, None, None)

    
    # Element IMPUTATION uses Python identifier IMPUTATION
    __IMPUTATION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IMPUTATION'), 'IMPUTATION', '__AbsentNamespace2_CTD_ANON_14_IMPUTATION', False, pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 209, 50), )

    
    IMPUTATION = property(__IMPUTATION.value, __IMPUTATION.set, None, None)

    
    # Element ASSEMBLY (ASSEMBLY) inherited from {SRA.common}ReferenceSequenceType
    
    # Element SEQUENCE (SEQUENCE) inherited from {SRA.common}ReferenceSequenceType
    _ElementMap.update({
        __EXPERIMENT_TYPE.name() : __EXPERIMENT_TYPE,
        __PROGRAM.name() : __PROGRAM,
        __PLATFORM.name() : __PLATFORM,
        __IMPUTATION.name() : __IMPUTATION
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


ANALYSIS_SET = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ANALYSIS_SET'), AnalysisSetType, documentation='A container of analysis objects. ', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 83, 4))
Namespace.addCategoryObject('elementBinding', ANALYSIS_SET.name().localName(), ANALYSIS_SET)

ANALYSIS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ANALYSIS'), AnalysisType, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 88, 4))
Namespace.addCategoryObject('elementBinding', ANALYSIS.name().localName(), ANALYSIS)



AnalysisSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ANALYSIS'), AnalysisType, scope=AnalysisSetType, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 80, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnalysisSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'ANALYSIS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 80, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AnalysisSetType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'REFERENCE_ALIGNMENT'), _ImportedBinding_SRA_common_xsd.ReferenceSequenceType, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 182, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SEQUENCE_VARIATION'), CTD_ANON_14, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 188, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SEQUENCE_ASSEMBLY'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 216, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SEQUENCE_FLATFILE'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 238, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SEQUENCE_ANNOTATION'), CTD_ANON_2, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 239, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'REFERENCE_SEQUENCE'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 245, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SAMPLE_PHENOTYPE'), CTD_ANON_4, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 248, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROCESSED_READS'), _ImportedBinding_SRA_common_xsd.ReferenceSequenceType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 254, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GENOME_MAP'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 255, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AMR_ANTIBIOGRAM'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 271, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PATHOGEN_ANALYSIS'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 272, 32)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TRANSCRIPTOME_ASSEMBLY'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 273, 32)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'REFERENCE_ALIGNMENT')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 182, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'SEQUENCE_VARIATION')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 188, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'SEQUENCE_ASSEMBLY')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 216, 32))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'SEQUENCE_FLATFILE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 238, 32))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'SEQUENCE_ANNOTATION')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 239, 32))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'REFERENCE_SEQUENCE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 245, 32))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'SAMPLE_PHENOTYPE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 248, 32))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'PROCESSED_READS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 254, 32))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'GENOME_MAP')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 255, 32))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'AMR_ANTIBIOGRAM')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 271, 32))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'PATHOGEN_ANALYSIS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 272, 32))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'TRANSCRIPTOME_ASSEMBLY')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 273, 32))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NAME'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 219, 44)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PARTIAL'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 220, 44)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'COVERAGE'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 221, 44)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROGRAM'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 222, 44)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PLATFORM'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 223, 44)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MIN_GAP_LENGTH'), pyxb.binding.datatypes.integer, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 224, 44)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MOL_TYPE'), STD_ANON_3, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 226, 44)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 224, 44))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 226, 44))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'NAME')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 219, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'PARTIAL')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 220, 44))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'COVERAGE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 221, 44))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'PROGRAM')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 222, 44))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'PLATFORM')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 223, 44))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'MIN_GAP_LENGTH')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 224, 44))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'MOL_TYPE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 226, 44))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROGRAM'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 258, 44)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PLATFORM'), STD_ANON_4, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 259, 44)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DESCRIPTION'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 266, 44)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 266, 44))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'PROGRAM')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 258, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'PLATFORM')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 259, 44))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'DESCRIPTION')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 266, 44))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_3()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FILE'), AnalysisFileType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 286, 36)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'FILE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 286, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_4()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ANALYSIS_LINK'), _ImportedBinding_SRA_common_xsd.LinkType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 301, 32)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'ANALYSIS_LINK')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 301, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_5()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ANALYSIS_ATTRIBUTE'), _ImportedBinding_SRA_common_xsd.AttributeType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 313, 32)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'ANALYSIS_ATTRIBUTE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 313, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_6()




AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TITLE'), pyxb.binding.datatypes.string, scope=AnalysisType, documentation='Title of the analysis object which will be displayed in\n                        search results. ', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 97, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DESCRIPTION'), pyxb.binding.datatypes.string, scope=AnalysisType, documentation='Describes the analysis in detail.', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 103, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_REF'), CTD_ANON_9, scope=AnalysisType, documentation='Identifies the parent study.', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 108, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SAMPLE_REF'), CTD_ANON_10, scope=AnalysisType, documentation='One of more samples associated with the\n                        analysis.', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 118, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_REF'), CTD_ANON_11, scope=AnalysisType, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 135, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RUN_REF'), CTD_ANON_12, scope=AnalysisType, documentation='One or more runs associated with the\n                        analysis.', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 142, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ANALYSIS_REF'), CTD_ANON_13, scope=AnalysisType, documentation='One or more runs associated with the\n                        analysis.', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 159, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ANALYSIS_TYPE'), CTD_ANON, scope=AnalysisType, documentation='The type of the analysis. ', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 176, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FILES'), CTD_ANON_6, scope=AnalysisType, documentation='Files associated with the\n                                        analysis.', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 278, 24)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ANALYSIS_LINKS'), CTD_ANON_7, scope=AnalysisType, documentation=' Links to resources related to this analysis.\n                    ', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 294, 20)))

AnalysisType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ANALYSIS_ATTRIBUTES'), CTD_ANON_8, scope=AnalysisType, documentation='Properties and attributes of an analysis. These can be\n                        entered as free-form tag-value pairs.', location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 306, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 8, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 97, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 103, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 108, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 118, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 135, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 142, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 159, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 294, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 306, 20))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 8, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'TITLE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 97, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'DESCRIPTION')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 103, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_REF')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 108, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'SAMPLE_REF')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 118, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_REF')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 135, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'RUN_REF')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 142, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'ANALYSIS_REF')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 159, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'ANALYSIS_TYPE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 176, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'FILES')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 278, 24))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'ANALYSIS_LINKS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 294, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AnalysisType._UseForTag(pyxb.namespace.ExpandedName(None, 'ANALYSIS_ATTRIBUTES')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 306, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AnalysisType._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_10()




def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_11()




def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 42, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_12()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_TYPE'), STD_ANON_2, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 193, 50)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROGRAM'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 205, 50)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PLATFORM'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 207, 50)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IMPUTATION'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 209, 50)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 825, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 830, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 193, 50))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 205, 50))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 207, 50))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 209, 50))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'ASSEMBLY')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 825, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'SEQUENCE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.common.xsd', 830, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_TYPE')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 193, 50))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'PROGRAM')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 205, 50))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'PLATFORM')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 207, 50))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'IMPUTATION')), pyxb.utils.utility.Location('/home/pbelmann/projects/CAMISIM/scripts/sra1/SRA.analysis.xsd', 209, 50))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_13()


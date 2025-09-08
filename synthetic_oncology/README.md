# Synthetic Oncology Data

This project demonstrates how to generate de-identified oncology patient data
using the [Synthea](https://github.com/synthetichealth/synthea) simulator and
create accompanying genomic variant profiles.

## Prerequisites

- Java 8 or later
- Git
- Gradle (or use the Gradle wrapper from Synthea)

## Generate Clinical Records

Clone and build Synthea, then run it to produce cancer-specific patient data.

```bash
git clone https://github.com/synthetichealth/synthea.git
cd synthea
./gradlew run --args="-Ppopulation=10"  # Generates 10 patients
```

The exported FHIR JSON files will appear under `output/fhir/`.

## Generate Variant Profiles

Run the helper script to create a small set of cancer-related variants for each
patient produced by Synthea:

```bash
python synthetic_oncology/make_variants.py
```

The script scans `output/fhir/` for patient IDs and writes corresponding VCF
files to `output/vcf/`.

Each VCF contains one to three randomly selected variants from a curated list of
cancer-associated mutations.

## Output Structure

```
output/
├── fhir/
│   ├── <patientID1>.json
│   └── ...
└── vcf/
    ├── <patientID1>.vcf
    └── ...
```

With this pipeline, every synthetic patient has both clinical records and an
associated genomic variant profile.

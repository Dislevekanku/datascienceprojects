import random
from pathlib import Path

# Known cancer-related variants (example subset)
# Format: chromosome, position, reference, alternate, gene annotation
CANCER_VARIANTS = [
    ("17", 43125483, "T", "G", "BRCA1 p.Val1736Ala"),
    ("13", 32906621, "C", "T", "BRCA2 p.Lys3326*"),
    ("7", 55249071, "G", "A", "EGFR p.L858R"),
    ("12", 25398285, "T", "G", "KRAS p.G12C"),
]


def write_vcf(
    patient_id: str, variants: list[tuple[str, int, str, str, str]], outdir: str
) -> None:
    """Write selected variants to a VCF file for the patient."""
    header = (
        "##fileformat=VCFv4.2\n"
        "##source=SyntheaVariantGenerator\n"
        "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n"
    )
    lines = [
        f"{chrom}\t{pos}\t.\t{ref}\t{alt}\t.\tPASS\tGENE={gene}"
        for chrom, pos, ref, alt, gene in variants
    ]

    path = Path(outdir) / f"{patient_id}.vcf"
    path.write_text(header + "\n".join(lines) + "\n")


def generate_for_patient(patient_id: str, outdir: str = "output/vcf") -> None:
    """Generate 1–3 random cancer-related variants for a patient."""
    Path(outdir).mkdir(parents=True, exist_ok=True)
    num = random.randint(1, 3)
    variants = random.sample(CANCER_VARIANTS, num)
    write_vcf(patient_id, variants, outdir)


def main() -> None:
    """Create VCFs for all patients found in FHIR export directory."""
    fhir_dir = Path("output/fhir")
    for fhir_file in fhir_dir.glob("*.json"):
        pid = fhir_file.stem
        generate_for_patient(pid)


if __name__ == "__main__":
    main()

# P0 A02 Paired Writer｜CURRENT

## STATUS
> RETIRED / INVALIDATED FOR NATIVE-vs-MIRROR A/B EVIDENCE

## REASON
The original protocol stored Native and Mirror instructions in one Git file.
A full-file read could expose Mirror guidance before Native generation.

See:
> `reviews/2026-09-26_reboot_v3_p0_input_boundary_contamination_audit.md`

Existing prose, if any:
> archive only; do not use for formal Native-vs-Mirror causal comparison.

## REPLACEMENT
Use physically isolated V2 Native and Mirror writer roles.

STOP.

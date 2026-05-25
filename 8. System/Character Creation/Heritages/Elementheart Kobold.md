---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kobold|Kobold]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

When you hatched, you imprinted on a creature strongly associated with one of the Elemental Planes, such as an elemental or genie. Choose air, earth, fire, metal, water, or wood for your elemental benefactor. You gain resistance equal to half your level (minimum 1) to the damage type associated with your elemental benefactor: cold for air, electricity for earth, fire for fire, sonic for metal, acid for water, or poison for wood.

**Source:** `= this.source` (`= this.source-type`)

---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Merfolk|Merfolk]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were raised amid colorful corals and schools of tropical fish. Compared to most merfolk, your body is vividly hued with stripes, spots, and patterns like a clownfish or angelfish. You're used to the occasionally toxic denizens of your home and are bothered little by stings or petty poisons. You gain poison resistance equal to half your level (minimum 1), and each of your successful saving throws against a poison affliction reduces its stage by 2, or by 1 for a virulent poison. Each critical success against an ongoing poison reduces its stage by 3, or by 2 for a virulent poison.

**Source:** `= this.source` (`= this.source-type`)

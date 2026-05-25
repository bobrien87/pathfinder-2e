---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Sarangay|Sarangay]]"
traits: ["[[Sarangay]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your ancestors dwelled in the swamps, fens, and flooded forests, where they contended with fierce predators and formed raiding parties to claim scarce resources. Blessed by the growing crescent, you're one of the eviscerators, and you can overcome threats that lurk in murky waters as well as those that hunt on land. You're a powerful swimmer with brown or gray fur and backward- or downward-curving horns. You gain a +2 circumstance bonus to Athletics checks to [[Long Jump]] or [[Swim]].

**Source:** `= this.source` (`= this.source-type`)

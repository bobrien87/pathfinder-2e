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

Some people call you a dwarf sarangay and your kind "hiding ones." Others whisper you go out with the moon when the moon "goes hunting"—a common folk saying for when the new moon vanishes from the sky. Your elusive ancestors built their lodgings in the shade of bamboo thickets, and your ancestral communities valued caution and independence, passing down the knowledge of walking lightly and moving like smoke through bamboo. Your ancestors had dark brown or gray fur with white markings and a V-shaped pair of flat, triangular horns. Your size is Small instead of Medium. You gain 10 Hit Points from your ancestry instead of 8 and gain a +2 circumstance bonus to Athletics checks to [[Shove]].

**Source:** `= this.source` (`= this.source-type`)

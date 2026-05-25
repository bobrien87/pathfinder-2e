---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Attack]]", "[[Composite]]", "[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Spinning wood and metal together, you create a rugged wooden ballista. The ballista is Medium and appears in an unoccupied space within 30 feet. It immediately shoots a bolt with a jagged tip of elemental metal. Make an Impulse check{impulse attack} roll against the AC of a target within 120 feet. The target takes @Damage[(floor((@actor.level -6)/3)+3)d12[piercing]] damage on a hit (or double damage on a critical hit). The ballista can be shot again, but it must first be reloaded with two Interact actions. The ballista lasts until the end of your next turn, and you can Sustain the impulse. Each time you Sustain it, you can roll the ballista up to 20 feet, shoot it if it's loaded, or contribute 1 action toward reloading it.

**Level (+3)** The damage increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)

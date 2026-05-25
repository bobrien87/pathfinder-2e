---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
traits: ["[[Mythic]]", "[[Teleportation]]"]
cast: "1 day"
range: "60 feet"
targets: "1 creature of up to 8th level"
duration: "varies"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

This ritual was developed by a long-dead minotaur hero-god whose cult trained to hunt and trap evil beings. It creates a maze of ever-shifting warped space woven from intertwined demiplanes that twist in ways few can solve.

You and the secondary casters draw a maze of twisted space into being with the target at its center. An unwilling target must be [[Immobilized]], [[Unconscious]], or otherwise prevented from leaving the area for the entire casting time, or the ritual fails. An unwilling target can attempt a Will save to resist the ritual; on a critical success, treat the result as critically failing to cast the ritual. While the target is trapped within the labyrinthine prison, they cannot escape it, as even abilities that give access to other planes are subject to being twisted into the maze. Instead the only way to escape is by succeeding at a Maze Lore, Perception, or Survival check against the labyrinthine prison's DC. This check can be attempted once per week, and the first check can only be attempted after a week has passed. If all casters spend one Mythic Point each, this interval changes to one year, and the DC uses the primary caster's mythic proficiency.
- **Critical Success** As success, and the twisted space renders the target [[Stupefied 2]] while within.
- **Success** The target is trapped within the labyrinthine prison for the duration of ritual.
- **Failure** The ritual fails to trap the target.
- **Critical Failure** As failure, and the casters are all [[Stupefied 4]] for 1 week.

**Heightened (4th)** The maximum level of the target is 10. The cost is the target's level (minimum 1) × 40 gp. The interval becomes 1 month, and spending Mythic Points increases it to 5 years.

**Heightened (5th)** The maximum level of the target is 12. The cost is the target's level (minimum 1) × 75 gp. The interval becomes 2 months, and spending Mythic Points increases it to 10 years.

**Heightened (6th)** The maximum level of the target is 14. The cost is the target's level (minimum 1) × 125 gp. The interval becomes 6 months, and spending Mythic Points increases it to 30 years.

**Heightened (7th)** The maximum level of the target is 16. The cost is the target's level (minimum 1) × 200 gp. The interval becomes 1 year, and spending Mythic Points increases it to 50 years.

**Heightened (8th)** The maximum level of the target is 18. The cost is the target's level (minimum 1) × 300 gp. The interval becomes 2 years, and spending Mythic Points increases it to 100 years.

**Heightened (9th)** The maximum level of the target is 20. The cost is the target's level (minimum 1) × 600 gp. The interval becomes 5 years, and spending Mythic Points increases it to 200 years.

**Source:** `= this.source` (`= this.source-type`)

---
type: action
source-type: "Remaster"
traits: ["[[Arcane]]", "[[Concentrate]]"]
cast: "`pf2:2`"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** Spend 1 Mythic Point. The spirits of the eight runelords of greed (Kaladurnae, Fethryr, Gimmel, Ligniya, Mazmiranna, Aethusa, Haphrama, and Karzoug) appear and bolster the armaments of you and your companions. For each of the spirits, one creature of your choice within 60 feet gains a +2 item bonus to AC, attack rolls, or saving throws (chosen by the creature) for 1 minute. These bonuses increase to +4 while the creature is within 100 feet of Xanderghul, the Runelord of Pride. A creature can receive bonuses from multiple runelords at once (gaining bonuses to both AC and attack rolls, for example), but the bonuses aren't cumulative.

**Source:** `= this.source` (`= this.source-type`)

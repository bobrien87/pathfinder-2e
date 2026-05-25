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

**Effect** Spend 1 Mythic Point. The spirits of four runelords of gluttony (Kaliphesta, Atharend, Aethusa, and Goparlis) briefly appear in spaces within 60 feet of you. Each living creature adjacent to at least one of the spirits takes 4d6 void damage per adjacent spirit, to a maximum of 16d6 void damage if they are adjacent to all four spirits. Each target receives a basic Fortitude save against the damage, against the higher of your class DC or spell DC, but Xanderghul, the Runelord of Pride, treats the result of his saving throw as one degree of success worse.

You gain temporary Hit Points equal to half the damage a single creature takes from this effect; calculate these temporary Hit Points using the creature that took the most damage. These temporary Hit Points last 1 minute.

**Source:** `= this.source` (`= this.source-type`)

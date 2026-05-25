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

**Effect** Spend 1 Mythic Point. The spirits of eight runelords of envy (Naaft, Tannaris, Ivamura, Jurah, Chalsardra, Esedrea, Zarve, Desamelia, and Phirandi) swirl about you for 1 minute. While at least one of the spirits remains, whenever you take damage, you can use a reaction that has the concentrate trait to gain resistance 10 to that damage, or resistance 20 if the damage was dealt by Xanderghul, the runelord of pride. Each time you use this feat to gain resistance, one of the spirits disappears.

**Source:** `= this.source` (`= this.source-type`)

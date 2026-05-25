---
type: action
source-type: "Remaster"
traits: ["[[Arcane]]", "[[Concentrate]]", "[[Healing]]"]
cast: "`pf2:2`"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Trigger** You or an ally within 60 feet uses [[Rewrite Fate]] to reroll a saving throw

**Effect** Spend 1 Mythic Point. The triggering creature regains @Damage[(7d10+28)[healing]] Hit Points. The amount of healing increases to @Damage[(10d10+40)[healing]] Hit Points if Xanderghul, the Runelord of Pride, was the source of the triggering effect.

**Source:** `= this.source` (`= this.source-type`)

---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Heroic Scion|Heroic Scion]]"
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Mythic]]", "[[Spellshape]]"]
prerequisites: "Heroic Scion Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your enemies feel the inevitability of defeat once they feel the potency of your magic. If your next action is to Cast a Spell that allows a saving throw, your spell gains the emotion, fear, and mental traits. The spell gains the following success and failure effects in addition to any other effects it would normally have. If the target is your nemesis or an ally of your nemesis, use mythic proficiency to determine your spell's attack bonus and save DC; if the spell has multiple targets, all targets must be your nemesis or allied with your nemesis for you to use mythic proficiency.
- **Critical Success** The target is unaffected by the daunting spell.
- **Success** The target is [[Frightened]] 1.
- **Failure** The target is [[Frightened]] 2 and [[Stupefied 1]] for as long as they remain frightened. If the daunting spell has a duration, the affected creature can't reduce their frightened condition from this effect below 1 until the spell's duration ends.
- **Critical Failure** As failure, but [[Frightened]] 3 and [[Stupefied 2]].

**Source:** `= this.source` (`= this.source-type`)

---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Five Breath Vanguard|Five Breath Vanguard]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Healing]]", "[[Magical]]"]
prerequisites: "Five-Breath Vanguard Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The first time each round that you [[Cycle Elemental Stance]], you gain temporary Hit Points equal to half your level that last until the start of your next turn. After you've gained temporary Hit Points for entering a specific elemental stance, you can't gain temporary Hit Points from entering that stance again until you've entered every other elemental stance you know or 10 minutes passes, whichever comes first.

> [!danger] Effect: Renewing Cycle

**Source:** `= this.source` (`= this.source-type`)

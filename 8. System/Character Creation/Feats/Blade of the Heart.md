---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Starlit Sentinel|Starlit Sentinel]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Emotion]]"]
prerequisites: "Starlit Sentinel Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The bonds of the heart are stronger than any steel, more powerful than any magic. You plunge your transformed weapon into the heart of a willing adjacent ally, where it phases harmlessly into their body. As you pull the weapon out, your ally's heart inscribes one of the following weapon property runes on your weapon: [[Corrosive]], [[Flaming]], [[Frost]], [[Shock]], [[Thundering]], or [[Vitalizing]]. The first time you use Blade of the Heart with a given ally, the GM should decide which rune best represents your shared relationship (such as elegant frost for a respected mentor or brash thundering for a boisterous sparring partner); thereafter, each time you use Blade of the Heart with that ally, you draw the same rune. This rune lasts for as long as you remain in sentinel form and counts toward your maximum limit of runes as normal.

At 16th level, you draw the greater version of the rune instead.

**Source:** `= this.source` (`= this.source-type`)

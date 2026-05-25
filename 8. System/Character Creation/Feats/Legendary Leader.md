---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Captain|Captain]]"
source-type: "Remaster"
level: "15"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Captain Dedication, legendary in Diplomacy or Intimidation"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your fame has spread throughout the lands. When you first attempt to [[Coerce]] or [[Make an Impression]] on an intelligent creature, the GM rolls a secret DC 11 flat check to see if they have heard of you. On a success, you gain a +2 circumstance modifier to the skill check for that action. The GM can adjust this flat check as appropriate for circumstances in which you may be more or less known.

You can also leverage your notoriety and your network of assistants and admirers to earn money. You can [[Earn Income]] using the skill you used to meet the prerequisites of this feat. When you do, you gain a +2 circumstance bonus to the check; this bonus increases to a +3 if you have the Cadre feat, as your retainers praise your deeds and find those who might pay to meet you.

**Source:** `= this.source` (`= this.source-type`)

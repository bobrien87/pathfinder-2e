---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Auditory]]", "[[Minotaur]]"]
prerequisites: "expert in Intimidation and Stealth"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are not observed by any enemies within 60 feet.

You emit a terrifying growl and snort, stamping your hooves for all to hear so that they know that you hunt them. Attempt an Intimidation check to [[Demoralize]] all enemies within 30 feet, and you do not take a penalty for not sharing a language. If the targets are in a maze or similarly difficult-to-navigate location, you gain a +2 circumstance bonus to this check, and the range increases to 60 feet. Each target is temporarily immune for 1 hour.

**Source:** `= this.source` (`= this.source-type`)

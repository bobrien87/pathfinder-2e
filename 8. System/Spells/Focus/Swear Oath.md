---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]"]
cast: "1 or 2"
duration: "until the end of your next turn"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You loudly and firmly state a course of action that you swear to fulfill. When you Cast this Spell, Ready a single action or free action you can use. If the action is in line with your personal edicts or the edicts presented by your religion, you can Cast this Spell as a single action.

If the trigger you designate occurs and you can use the chosen action as a reaction, you gain a +1 status bonus to any attack roll or skill check required. If the trigger you designate doesn't occur, you can Sustain the spell on your next turn to regain the Focus Point spent for this spell.

**Heightened (5th)** The status bonus is +2.

**Heightened (9th)** The status bonus is +3.

> [!danger] Effect: Spell Effect: Swear Oath

**Source:** `= this.source` (`= this.source-type`)

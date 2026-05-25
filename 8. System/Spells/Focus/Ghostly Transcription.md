---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Glowing letters assemble in the air, providing a transcription of the target's speech in all languages you speak. For the spell's duration, any words spoken aloud by the target are spelled out in letters in front of them.

When you Cast the Spell, you can choose whether these letters are visible to all creatures or only certain creatures you specify. Any words the target mouths silently are similarly spelled out, allowing the target to communicate silently or in areas where sound doesn't carry. This even allows the target to utter the incantations necessary for spells in such areas, but only if you choose to make the letters visible to all creatures.

Furthermore, any of the target's auditory abilities can affect creatures even in areas where sound doesn't carry as long as you have made the glyphs visible to them and they have line of sight to the target; in this case, they gain the visual trait. You can Dismiss the spell.

**Source:** `= this.source` (`= this.source-type`)

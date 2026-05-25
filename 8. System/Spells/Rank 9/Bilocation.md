---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "10 minutes"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You exist in two places at once. When you Cast the Spell, another copy of yourself appears in an adjacent square. During bilocation's duration, whenever you act, you can choose which of your selves does so, and whenever one of you uses a move action, you can both move. Your two selves share Hit Points, and any condition or effect on one affects both. If both of your selves are in the area of the same effect, or targeted by the same multitarget effect, you are only affected once. Even if you are reduced to 0 Hit Points or killed, both selves remain until the duration expires. Your link continues at any distance, even across planar boundaries. You can Dismiss the Spell, and if you do so, you choose which of the selves vanishes and which becomes you, allowing you to extricate one of your selves from a dangerous situation.

**Source:** `= this.source` (`= this.source-type`)

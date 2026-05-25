---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Force]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Visible tendrils of force anchor your body to the ground, preventing unwanted movement. Whenever you're on the ground and a creature or effect attempts to forcibly move you from your space, you can use your spell DC in place of your Fortitude DC as the DC of the check to move you. If a creature wouldn't normally need a check to move you, it must succeed at an appropriate check (usually an Athletics check for physical movement) against your spell DC or you are unmoved; if an effect wouldn't normally need a check to move you, it must counteract *bracing tendrils* or you are unmoved. When a creature fails to move you in this way, you can choose to have the tendrils lash back and push them 5 feet away from you.

While the tendrils anchor you in place when you come to a stop, they uproot easily to cooperate with your own voluntary movement, so you can still move freely while under the effect of the spell.

**Source:** `= this.source` (`= this.source-type`)

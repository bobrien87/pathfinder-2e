---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transform your appearance to that of a Small or Medium humanoid, such as a dwarf, elf, goblin, halfling, human, or orc. You gain the humanoid trait in addition to your other traits while in this form, as well as any trait related to the creature's kind (such as goblin or human). If this transformation reduces your size, it reduces your reach accordingly (typically to 5 feet). This transformation doesn't change your statistics in any way, and you don't gain any special abilities of the humanoid form you assume. You can still wear and use your gear, which changes size (if necessary) to match your new form. If items leave your person, they return to their usual size.

Humanoid form grants you a +4 status bonus to Deception checks to pass as a generic member of the chosen ancestry, and you add your level even if you're untrained, but you can't make yourself look like a specific person. If you want to Impersonate an individual, you still need to create a disguise, though the GM won't factor in the difference in ancestry when determining the DC of your Deception check. You can Dismiss this spell.

> [!danger] Effect: Spell Effect: Humanoid Form

**Heightened (3rd)** You gain darkvision or low-light vision if the form you assume has that ability.

**Heightened (5th)** You can take on the appearance of a Large humanoid. If this increases your size, you gain the effects of the enlarge spell.

**Source:** `= this.source` (`= this.source-type`)

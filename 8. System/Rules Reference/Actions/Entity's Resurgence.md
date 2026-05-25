---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You would be reduced to 0 Hit Points but not immediately killed

**Effect** Instead of letting you fall [[Unconscious]], your entity takes control. You remain at 1 Hit Point and gain temporary Hit Points equal to your level + your key attribute modifier that last for 1 minute. However, the entity is in control for 1 minute or until you fall unconscious, whichever comes first.

While the entity is in control, you gain a +1 status bonus to attack rolls and damage rolls, and the GM usually controls your character, roleplaying the entity. The GM might decide to have you roleplay the entity instead, but they retain final say over any decisions you make. No matter the entity's nature, the entity is sure to wreak vengeance upon the foe who jeopardized the life of their vessel—even a malicious entity won't change allegiances or ignore danger except in the most extreme circumstances.

**Source:** `= this.source` (`= this.source-type`)

---
type: action
source-type: "Remaster"
traits: ["[[Magical]]", "[[Manipulate]]", "[[Thaumaturge]]"]
cast: "`pf2:r`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** The target of your Exploit Vulnerability would damage you or an ally within 15 feet of you.

**Requirements** You're holding your amulet implement and are benefiting from Exploit Vulnerability.

You forcefully present your amulet to turn away harm. You or a target ally within 15 feet gain resistance to all damage against the triggering damage. The resistance is equal to 2 + your level.

> [!danger] Effect: Amulet's Abeyance

**Source:** `= this.source` (`= this.source-type`)

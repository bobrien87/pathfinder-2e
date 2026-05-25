---
type: action
source-type: "Remaster"
traits: ["[[Magical]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

**Effect** You transform a non-magical arrow or bolt on your person into a piece of magical ammunition of one type you chose for the [[Magic Ammunition]] feat. You must shoot the ammunition before the end of your turn or the magic dissipates. If the ammunition has an Activate entry, you still need to spend the required actions to activate the ammunition before shooting it.

You can choose a type of magical ammunition that is typically not available to the type of ammunition you're using—for example, you can use [[Climbing Bolt]] on an arrow, even though that magical ammunition is normally only found on bolts.

**Source:** `= this.source` (`= this.source-type`)

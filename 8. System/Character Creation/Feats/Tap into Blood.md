---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Sorcerer]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are benefiting from a blood magic effect

The power in your blood allows you to perform minor feats of magic. You can perform one of the following actions depending on the tradition of your bloodline.

- **Arcane** Your mind temporarily opens to the secrets of the world. Attempt to Recall Knowledge; you can use Arcana instead of the skill normally needed for that subject. If you critically fail at this check, you get a failure instead.
- **Divine** Whatever divine provenance is in your lineage guides you to instinctively move yourself or others out of harm's way. You Step, or you [[Reposition]] a target within your reach using Religion for the check.
- **Occult** Strange mists or swirling colors hide your movement. You Step up to 10 feet.
- **Primal** The immense power of nature echoes in your voice. You can attempt a Nature check to Demoralize a target.

**Source:** `= this.source` (`= this.source-type`)

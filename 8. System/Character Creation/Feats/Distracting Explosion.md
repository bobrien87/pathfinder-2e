---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Inventor]]", "[[Manipulate]]"]
prerequisites: "offensive boost"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature within your reach uses a concentrate action.

Your enemies think they can concentrate on something else while you're nearby? Oh, you'll give them a distraction, all right! Make a melee Strike against the triggering creature with a weapon or unarmed attack that is benefiting from your offensive boost. This Strike doesn't count toward your multiple attack penalty, and your multiple attack penalty doesn't apply to this Strike.

**Unstable Function** You pull out all the stops to create an explosive distraction. Add the unstable trait to Distracting Explosion. If the attack hits, you disrupt the triggering concentrate action.

**Special** If your innovation is a minion, it can take this reaction instead of you, even though minions can't normally take reactions or act when it's not their turn. It uses your reaction for the turn to do so.

**Source:** `= this.source` (`= this.source-type`)

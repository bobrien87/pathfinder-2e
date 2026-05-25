---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Wayang]]"]
prerequisites: "Inherit the Dreaming Heirloom"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As you whisper to your pusaka, it attempts to cut away an enemy's shadow, leaving them in an eternal sleep. Your pusaka gains the following Activation.

**Activate—Cut the Shadow** `pf2:2` (concentrate, manipulate, mental)

**Frequency** once per day

**Effect** Your pusaka becomes a kris made of darkness and drives itself into an adjacent enemy's shadow. That enemy takes 80 mental damage with a [[Fortitude]] save against your spell DC or class DC, whichever is higher. If this reduces the creature to 0 Hit Points, the target doesn't die, but its shadow is severed from its body, becoming a [[Shadow Spawn]] that attempts to flee from the target's body. As long as the shadow spawn exists, the target remains in a dreamless slumber; if destroyed, the target regains its shadow and awakens (if its body was kept properly while [[Unconscious]]).

**Source:** `= this.source` (`= this.source-type`)

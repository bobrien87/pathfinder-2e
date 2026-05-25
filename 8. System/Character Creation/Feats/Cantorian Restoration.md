---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Healing]]", "[[Hobgoblin]]", "[[Vitality]]"]
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** A living creature within 60 feet would die.

The energy that flows in your blood can save a life in the direst of times. You prevent the creature from dying and restore @Damage[(6d8+@actor.system.abilities.con.mod)[healing]]{6d8 + your Constitution modifier} Hit Points to it. You can't use Cantorian Restoration if the triggering effect was a death effect or an effect that leaves no remains, such as [[Disintegrate]].

**Source:** `= this.source` (`= this.source-type`)

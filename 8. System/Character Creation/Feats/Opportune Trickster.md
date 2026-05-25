---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellbreaker|Hellbreaker]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Mental]]"]
prerequisites: "Hellbreaker Dedication, trained in Deception"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An adjacent ally makes a melee Strike against a creature.

**Requirements** You're adjacent to both your ally and the creature.

You aren't above using underhanded tactics to gain an advantage, easily routing your opponents when they attack. Attempt a [[Deception]] check against the Perception DC of the creature that's the target of the triggering attack. Regardless of the result, the target is temporarily immune to your attempts to use Opportune Trickster for the next 10 minutes.
- **Critical Success** The target is [[Off Guard]] (including against the triggering attack) until the end of your ally's turn.
- **Success** The target is off-guard against the triggering attack.
- **Critical Failure** You lose your balance in your attempt to assist your ally and fall [[Prone]].

**Special** If you have the [[Dirty Trick]] skill feat, you can attempt a [[Thievery]] check instead of a Deception check; if you do, this action loses the mental trait

**Source:** `= this.source` (`= this.source-type`)

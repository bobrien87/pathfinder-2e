---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Twilight Speaker|Twilight Speaker]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Emotion]]", "[[Mental]]", "[[Visual]]"]
prerequisites: "Twilight Speaker Dedication"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You are the target of a melee attack and the attacker has not rolled yet.

**Requirements** You are aware of the attacker, the attacker is an intelligent humanoid creature, and you have not attempted to harm the attacker.

With a wide and sincere smile, you give your attacker pause. You attempt a [[Diplomacy]] check against the triggering attacker's Will DC. After you use Disarming Smile, all creatures who witnessed you use it are temporarily immune to your Disarming Smile for the next 24 hours.
- **Critical Success** Your enemy ceases their attack, momentarily taken aback by your disarming smile. The attack fails and the triggering target can't attempt hostile actions against you until the beginning of its next turn or until you (or your allies) take hostile actions against the enemy (or its allies). You can begin talking to the creature on your next turn to attempt another Diplomacy check; on a success, you sustain the effect until the beginning of your next turn, to a maximum of 1 minute. Talking on subsequent rounds requires that you be able to communicate with the target creature and imparts the auditory and linguistic traits to the action.
- **Success** Your foe pauses momentarily. Their attack fails, but they can attempt further attacks against you.
- **Failure** The target's attack is unaffected.

**Source:** `= this.source` (`= this.source-type`)

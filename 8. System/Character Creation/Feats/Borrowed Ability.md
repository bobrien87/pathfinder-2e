---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Magical]]", "[[Mental]]"]
source: "Gatewalkers Player's Guide (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your touch opens a conduit into the mind of your target, the emptiness within you pulling skills and memories through. You touch an adjacent creature and choose any skill you believe they are trained or better in. If you choose a skill that they are trained or better in, you borrow their proficiency in that skill, becoming trained in that skill for 1 minute. If they are not trained in the skill you choose, the GM chooses the next most applicable skill (for instance, choosing Acrobatics instead of Athletics). At 12th level, you can become an expert in the skill if the target is as well.

If the target of Borrowed Ability is unwilling, the effects depend on the target's Will save.
- **Critical Success** The target resists your touch completely.
- **Success** Your borrowing is unstable. At the beginning of each of your turns, you must either relinquish your hold on the borrowed skill (as a free action), or attempt another backlash check for your deviation; the ability ends if you fail.
- **Failure** Borrowed Ability lasts for its full duration.

**Awakening** You gain some of the target's defensive abilities. When you use Borrowed Ability, you also gain a +1 circumstance bonus to one of your saving throws for the duration, matching the target's highest saving throw. You can choose to apply a –1 circumstance penalty to the target's saving throw when you do so.

**Awakening** Your touch establishes a lingering link through which you can sense what your target does. When you use Borrowed Ability, you gain any special senses—such as darkvision, scent, or tremorsense—that the target possesses. If the target does not have a sense that you normally have (for instance, an ooze that has no vision), you lose those senses as well. Your senses remain altered for the duration of Borrowed Ability.

**Source:** `= this.source` (`= this.source-type`)

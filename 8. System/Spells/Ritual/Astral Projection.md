---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
cast: "1 hour"
range: "touch"
targets: "yourself and up to 5 willing creatures"
duration: "see text"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You project the targets' spiritual essences into the Astral Plane, leaving their inanimate physical forms behind. These astral forms can be used to explore the Astral Plane indefinitely, while the targets' bodies remain safely in stasis on the plane where the ritual was cast (where they remain [[Unconscious]] and can't be awoken normally). The casters must be in physical contact with one another in a circle for the duration of the casting, and all targets must be selected from these casters.

A target's astral form is a duplicate of the target and everything they're carrying; anything that happens to a duplicate item happens to the original as well. For instance, if you use, spend, destroy, lose, or give away an item's duplicate, the original vanishes from your possession. For the duration of the ritual, any of the targets can spend a single action to Dismiss their astral form and immediately return to their physical body. As the primary caster, when you Dismiss your astral form, you can also Dismiss all the other targets' astral forms as part of the same action, returning all targets to their physical forms simultaneously. While in the Astral Plane, the other targets are unable to navigate without you, and if they become separated from you, they must wait for your return or Dismiss their own astral forms. When the ritual ends, the targets' astral forms vanish.

A target's astral form and corresponding physical form are linked by an incorporeal silver cord, which is visible only in the Astral Plane. This nearly unbreakable cord serves as conduit and safety line; if severed, the target's astral and physical forms are both immediately slain. If the ritual is interrupted by an external force, such as dispel magic being cast on a target's physical or astral form, the target is immediately and harmlessly returned to their physical body. If a target's astral form is slain, the silver cord immediately rips them back to their physical body; the strain requires them to attempt a Fortitude save with the same DC as the ritual's primary check. On a failure, the creature dies; on a success, it becomes [[Clumsy]] 2, [[Drained]] 2, [[Doomed]] 2, and enfeebled 2 for 1 week; these conditions can't be removed or reduced by any means until the week has passed. A target's physical body remains in suspended animation for the duration of the ritual, but if it's destroyed, the creature dies and its astral form also vanishes. This ritual only projects a portion of the targets' consciousnesses onto the Astral Plane. To travel physically to the Astral Plane (to reach the Outer Planes, for example) requires spells such as interplanar teleport.
- **Critical Success** All targets are able to navigate independently in the Astral Plane. Each target's silver cord is stronger than usual, providing them a +4 circumstance bonus to its Fortitude save to avoid dying if its astral form dies.
- **Success** You successfully project the targets.
- **Failure** You fail to project the targets.
- **Critical Failure** The process of separating the targets' spirits from their bodies is complicated, and something goes catastrophically wrong. All casters become [[Doomed]] 1, are immediately reduced to 0 Hit Points, and begin dying

**Source:** `= this.source` (`= this.source-type`)

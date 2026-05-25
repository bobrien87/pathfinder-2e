---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
cast: "3 days"
targets: "the secondary caster who doesn't perform the Crafting check"
duration: "1 day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You and the secondary casters spend 2 days drawing sigils on one another. At the end of the second day, the secondary caster responsible for the Crafting check carefully mixes the wine with the herbs and a small amount of saliva or blood from the target. The target then drinks the concoction, entering a state of metaphorical death and rebirth, their body becoming comatose for the final day of the ritual. During this time, you and the other secondary caster bathe the body in dirt, symbolizing a grave, and sprinkle the remainder of the wine around the body. If done properly, swaddled baby orchids grow around the area, enveloping the body in a bed of flowers.

On the final hour, the target returns to life, waking up temporarily possessed by an incarnation from one of their past lives. Though they retain the memories from their current life, their demeanor and personality are different for the remaining duration of the ritual, and they also remember vivid details from their past life. Unfortunately, it's impossible to choose a particular past self or to know whether a given former incarnation has good or bad intentions.
- **Critical Success** The target's personality reverts to a previous incarnation, determined by the GM. Normally they keep their abilities, but in rare cases, the GM might determine that the past incarnation has a different set of abilities based on their previous life. The lingering knowledge of the past incarnation is powerful and sticks with the target, allowing them to retrain one of their skills increases into a skill in which the past incarnation was particularly talented; the list of possible skills depends on the nature of the past incarnation and is determined by the GM.
- **Success** As critical success, except there's no lingering knowledge, and the target isn't able to retrain a skill increase.
- **Failure** Nothing happens, though the target's [[Unconscious]] state is disturbing, and they wake up [[Fatigued]] as well as likely disoriented.
- **Critical Failure** The sigils are drawn improperly, or the wine was tainted. The swaddled baby orchids that grow around the body scream at the moment when the target would've awakened. The target dies and their body is immediately possessed by a malevolent spirit that seeks to destroy their former allies. Use the statistics for a [[Ghost Commoner]] using Malevolent Possession on the target's body.

**Source:** `= this.source` (`= this.source-type`)

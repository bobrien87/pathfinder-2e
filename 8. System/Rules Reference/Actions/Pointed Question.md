---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Investigator]]", "[[Linguistic]]", "[[Mental]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You ask a question that charms or needles someone in just the right way. Ask a question of a non-allied creature that you can see. Attempt a [[Diplomacy]] check against the creature's Will DC. The creature is then temporarily immune for 1 hour.
- **Critical Success** The target must directly answer your question. It doesn't have to answer truthfully, but you gain a +4 circumstance bonus to your Perception DC if the creature attempts to [[Lie]] to you.

Whether it answers truthfully or not, you glean something from its body language, and it is [[Off Guard]] to the Strike you make using [[Devise a Stratagem]] against it before the end of your turn.
- **Success** As critical success, but the circumstance bonus to your Perception DC is +2.

> [!danger] Effect: Pointed Question
- **Failure** The target can refuse to answer you as normal.
- **Critical Failure** The target can refuse to answer you as normal, and its attitude toward you decreases by one step due to your aggravating attention.

**Source:** `= this.source` (`= this.source-type`)

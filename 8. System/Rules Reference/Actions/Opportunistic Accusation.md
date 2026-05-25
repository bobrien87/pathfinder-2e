---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Linguistic]]", "[[Mental]]"]
cast: "`pf2:r`"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A demon you're aware of within 30 feet of you suffers from its sin vulnerability or critical fails at a saving throw against a mental effect

You make a quick cutting remark against the demon that takes advantage of the fiend's momentary disadvantage. The demon must attempt a [[Will]] save against your class DC.
- **Critical Success** The demon is unaffected and likely to focus its attention on you in combat from this point forward.
- **Success** The demon takes 2d6 mental damage.
- **Failure** The demon takes 4d6 mental damage and is [[Off Guard]] until the start of its next turn.
- **Critical Failure** As failure, but the off-guard condition lasts until the end of the next round. The demon also takes 2d6 persistent,mental damage.

**Source:** `= this.source` (`= this.source-type`)

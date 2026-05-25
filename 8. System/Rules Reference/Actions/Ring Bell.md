---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Magical]]", "[[Manipulate]]", "[[Sonic]]", "[[Thaumaturge]]"]
cast: "`pf2:r`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** The target of your Exploit Vulnerability makes a Strike or Casts a Spell that would affect you or one of your allies.

**Requirements** You are holding your bell implement, and the triggering creature is within 30 feet of you.

Your implement sings out abruptly, disrupting your foe. The piece played depends on whether the trigger was a Strike or Spell, and it applies to the triggering Strike or Spell, except where noted otherwise.

- **Distracting Cacophony** The trigger is a spell. You create a musical crash of sonic energy that assails the target and breaks its concentration. The target must succeed at a [[Fortitude]] save against your class DC or become [[Stupefied 1]] until the end of your next turn ([[Stupefied 2]] on a critical failure). The target doesn't have to attempt a flat check to avoid losing the triggering spell, but the discordant ring does lower the spell attack modifier or spell DC of the triggering spell from stupefied.
- **Disrupting Harmony** The trigger is a Strike. You create a strangely discordant harmony that sinks into your foe's body and throws its movements off. The target must succeed at a [[Will]] save against your class DC or become your choice of [[Enfeebled]] 1 or [[Clumsy]] 1 until the end of your next turn ([[Enfeebled]] 2 or [[Clumsy]] 2 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)

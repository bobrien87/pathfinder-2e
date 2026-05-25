---
type: action
source-type: "Remaster"
traits: ["[[Occult]]", "[[Psyche]]", "[[Psychic]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

The heightened power of your psyche lets you recall every lesson you've ever learned. You search your mind for the right teaching, which at first seems cryptic but comes into clarity when it's most relevant. Until the start of your next turn, you count as having prepared to [[Aid]] all allies within 30 feet of you. If you use the Aid reaction to help one of them during that time, you roll an Occultism check for `act aid skill=occultism traits=auditory,linguistic` as you recall a lesson to help them. Most lessons take the form of short axioms, parables, or sayings, meaning that conveying them to your ally usually grants your Aid reaction the auditory and linguistic traits.

**Source:** `= this.source` (`= this.source-type`)

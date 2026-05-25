---
type: action
source-type: "Remaster"
traits: ["[[Psychic]]"]
cast: "`pf2:0`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your turn begins.

**Requirements** You're in an encounter, you Cast a Spell on your previous turn, and you aren't [[Stupefied]].

You call on the depths of your mind and let psychic power flood through. Your Psyche remains Unleashed for 2 rounds or until your fall [[Unconscious]], whichever comes first. You can't voluntarily quell your unleashed psyche. While your Psyche is Unleashed, the following effects occur.

- You're constantly surrounded by the visual manifestation of your psychic magic.
- When you cast a damaging spell using your psychic spellcasting, you gain a status bonus to its damage equal to double the spell's rank. This applies only to the initial damage the spell deals when cast, and an individual creature takes this damage only once per spell, even if the spell would damage that creature multiple times.
- You can use actions that have the psyche trait. After your unleashed psyche subsides, your mind must recover from the strain of channeling its full power. You can't use Unleash Psyche again for 2 rounds, and you're [[Stupefied 1]] for 2 rounds.

**Source:** `= this.source` (`= this.source-type`)

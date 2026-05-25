---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Magical]]"]
cast: "`pf2:r`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your opponent uses a psychic manifestation against you.

**Requirements** You're in a psychic duel and are psychically centered.

You gain the benefit matching your psychic center against the triggering manifestation. Then your psychic center is expended.

**Armor of Insight (Perception)** Sensing the incoming attack, you make your mind resist psychic harm. You gain resistance equal to half your level (minimum 1) to mental damage against the triggering effect. This resistance is doubled if you're a master in Perception and tripled if you're legendary.

**Empathic Orbit (Diplomacy)** Displaying empathy, you sow doubt in your attacker to diminish their resolve for psychic combat. The opponent is [[Stupefied 1]] until the end of their next turn or [[Stupefied 2]] if you're legendary in Diplomacy.

**Ire's Spear (Intimidation)** Blazing anger surges in your mind, causing backlash to anyone who harms you. If the manifestation damages you, the opponent takes damage equal to the counteract rank of the manifestation it used against you. This damage is doubled if you're a master of Intimidation or tripled if you're legendary.

**Rational Labyrinth (Occultism)** Analytically breaking down the attack, you realign your mind's defenses into a puzzle designed to confound it. You gain a +2 status bonus to your Will save or Will DC, or a +4 status bonus if the effect has the emotion trait.

**Sensory Phantasm (Deception)** Using your guile, you send psychic illusions through your mental link to your foe, making yourself harder to pinpoint. You're [[Concealed]] against the opponent until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)

---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Deadly d10]]", "[[Magical]]", "[[Propulsive]]"]
price: "{'gp': 6500}"
usage: "held-in-one-plus-hands"
bulk: "1"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking frost composite shortbow* belonged to a legendary scout, Jelarial, who found herself in command of a company of elves fleeing Mierani north into the Crown of the World to escape the doom of Earthfall thousands of years ago. *Wintershot* resurfaced during the war to reclaim Kyonin from Tanglebriar several thousand years later, wielded by a succession of mysterious snipers whose movements through the woodland confounded the demons, so much so that it gave rise to rumors that Jelarial's ghost had returned to the south to aid her kin in a time of need.

When making a Strike with *Wintershot*, targets do not gain [[Concealment]] from the effects of mist or precipitation, and circumstance penalties to attacks of up to –2 imparted from strong winds are negated.

**Activate—Auroral Shine** `pf2:1` (cold, concentrate, light, primal)

**Frequency** once per 10 minutes

**Effect** Fire an arrow at a target. If you hit, instead of dealing damage with the arrow, the creature struck must attempt a DC 34 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is surrounded by shimmering lights akin to an aurora, causing it to become [[Dazzled]] for 2 rounds. If the creature was [[Invisible]], it becomes [[Concealed]] instead. If the creature was already concealed for any other reason, it is no longer concealed.
- **Failure** As success, but the creature also takes 2d6 persistent,cold damage, and the light affects the creature for 1 minute.
- **Critical Failure** As success, but the creature also takes 4d6 persistent,cold damage, and the light affects the creature for 10 minutes.

**Activate—Signal Flare** `pf2:1` (light, manipulate, primal)

**Frequency** once per day

**Effect** You pull back *Wintershot's* string and fire an arrow straight upward. The arrow soars to a height of 500 feet, or until it strikes a solid surface like a ceiling. When it reaches its apex, it explodes in a brilliant burst, creating a 100-foot radius area of bright light and dim light in the next 100 feet. In the night sky, this beacon can be seen clearly for miles. The beacon remains lit for up to 1 minute in a color of your choice. Alternately, you can fire a Signal Flare like a normal arrow to attempt to strike a Target—if it hits, the arrow inflicts normal damage and attempts to counteract one darkness effect of your choice that affects the area you hit with a counteract rank of 7th and a counteract modifier of +26.

**Source:** `= this.source` (`= this.source-type`)

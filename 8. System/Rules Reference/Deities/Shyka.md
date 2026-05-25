---
type: deity
source-type: "Remaster"
domains: "Decay, Fate, Time, Delirium"
favored-weapon: "Light-mace"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 3: [[Haste]], Rank 7: [[Time Beacon]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Eldest of entropy, reincarnation, and time, Shyka the Many is not a single entity but rather multiple beings who travel forward and backward through time. Each has sequentially held the title of Shyka, picking up the mantle and the knowledge that comes with it upon the passing (or disappearance) of a predecessor. Shyka visits so many overlapping temporal locations that other creatures encounter a random-seeming Shyka each time. This Eldest knows of the multiverse's birth as well as its death, having experienced both. Although Shyka claims to merely watch over the continuum of time, it's an open secret that the Eldest makes slight changes in line with their own goals—or requests that their worshippers do so, with abstruse promptings.

**Title** The Many

**Areas of Concern** Entropy, reincarnation, time

**Edicts** Learn from the past, leave hourglasses in unusual places, give random gifts, create ephemeral things

**Anathema** Willingly tread where time does not pass

**Religious Symbol** broken hourglass

**Sacred Animal** hive animals

**Sacred Colors** white

**Source:** `= this.source` (`= this.source-type`)

---
type: deity
source-type: "Remaster"
domains: "Darkness, Destruction, Nightmares, Nothingness"
favored-weapon: "War-flail"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 5: [[Wave Of Despair]], Rank 9: [[Detonate Magic]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ancient beyond mortal reckoning, Groetus is an entity who cannot be easily understood. He hangs in the sky above the Boneyard, a skull-faced moon constantly observing the passage of the souls below. Events can cause him to draw ominously closer to [[Pharasma]]'s Spire, or to retreat back to a safer distance, with little obvious rhyme or reason for these actions. He evinces little regard for anything but his singular aim: the dissolution of the universe.

**Title** God of the End Times

**Areas of Concern** apocalypse, empty places, oblivion, ruins

**Edicts** preach of the upcoming end times, destroy that which has outlived its usefulness, put the suffering out of their misery

**Anathema** artificially extend something's existence or life span, spread hope

**Religious Symbol** skull-faced moon

**Sacred Animal** none

**Sacred Color** none

**Source:** `= this.source` (`= this.source-type`)

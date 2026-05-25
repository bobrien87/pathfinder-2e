---
type: deity
source-type: "Remaster"
domains: "Might, Truth, Water, Wyrmkin"
favored-weapon: "War-flail"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Acidic Burst]], Rank 2: [[Animal Form]], Rank 3: [[Hypercognition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Once the mightiest of asura ranas, Geryon betrayed hundreds of Hell's original asura inhabitants to aid Asmodeus in claiming the plane, in the process earning himself the title the Source of Lies. His realm of Stygia, Hell's fifth layer, hews most closely to the nature of Hell before Asmodeus reshaped the plane, and it contains the sunken ruins of countless cities and libraries predating the war against Heaven. The archdevil hoards knowledge and secrets especially that which has been forbidden—while spreading falsehoods and heresies to mislead the ignorant, and his followers revel in the same.

**Title** The Serpent, Source of Lies

**Areas of Concern** Forbidden knowledge, heresy, snakes

**Edicts** Hoard knowledge, test the boundaries of taboo, spread falsehoods to dupe the foolhardy

**Anathema** Declare knowledge heresy or forbidden, break your word

**Religious Symbol** serpent's head

**Sacred Animal** snake

**Sacred Colors** purple, red

**Source:** `= this.source` (`= this.source-type`)

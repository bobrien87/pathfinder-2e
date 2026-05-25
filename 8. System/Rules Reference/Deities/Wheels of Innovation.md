---
type: deity
source-type: "Remaster"
domains: "Ambition, Change, Creation, Knowledge"
favored-weapon: "Polytool"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Temporary Tool]], Rank 4: [[Creation]], Rank 9: [[Metamorphosis]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

If necessity is the proverbial mother of invention, it can also count creativity, curiosity, inspiration, and hard work among its forebears. The divine entities of the Wheels of Innovation share a passion for motivating those who seek to breathe new life and fresh ideas into their fields of creation. These gods of invention and artistry currently believe the formation of this pantheon is their greatest idea to date.

Worship of this pantheon originated in urban centers around Golarion's Inner Sea region and in nations like Alkenstar, Numeria, and Rahadoum. Recently, it has also begun to blossom in more rural communities, as its adherents try to solve physical problems without relying on spellcasters or government officials. This has most firmly taken root in gnome, goblin, and halfling communities. Many of them profess that tinkering and experimentation are a far more positive—but no less exciting—way to seek entertainment as well.

**Pantheon Members** Aakriti, Bharnarol, Brigh, Casandalee, Nocticula, Torag

**Areas of Concern** innovators, inspiration, perseverance in the face of failures, and technology

**Edicts** devise solutions to problems through the creative use of items rather than magic or brute strength, encourage tinkering and experimentation, refuse to abandon a project at the first sign of failure

**Anathema** deprive others of their innovations unduly, stifle imagination

**Religious Symbol** two interlocking gears

**Source:** `= this.source` (`= this.source-type`)

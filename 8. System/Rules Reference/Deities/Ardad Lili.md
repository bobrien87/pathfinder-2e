---
type: deity
source-type: "Remaster"
domains: "Creation, Darkness, Wyrmkin, Passion"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Charm]], Rank 3: [[Enthrall]], Rank 4: [[Suggestion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

When mortals were young, before Asmodeus conquered Hell, Ardad Lili was already manipulating amorous and lustful mortals to swear fealty to her, amassing power from their souls. She fled the realm of Nirvana during the Exodus, taking up residence in Avernus and continuing to gather an army of damned souls and female devils who share her ambitions. The Serpent Muse has never forgotten the censures and cruel insults spewed by the other natives of Nirvana, and she seeks to someday rule not a layer of Hell, but a realm of the heavens. Ardad Lili draws followers who are as passionate as herself.

**Title** The End of Innocence

**Areas of Concern** Seduction, snakes, women

**Edicts** Manipulate others with false promises, aid women who have been unfairly maligned

**Anathema** Give someone more than you receive from them, allow yourself to be swayed by lust

**Religious Symbol** wings made of snake tails

**Sacred Animal** snake

**Sacred Colors** black, green

**Source:** `= this.source` (`= this.source-type`)

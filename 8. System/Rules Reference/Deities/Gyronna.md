---
type: deity
source-type: "Remaster"
domains: "Ambition, Nightmares, Pain, Zeal"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Ill Omen]], Rank 2: [[Paranoia]], Rank 6: [[Never Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The goddess Gyronna is also known as the Angry Hag, and for good reason.

**Title** The Angry Hag

**Areas of Concern** Extortion, hatred, spite

**Edicts** Expose hypocrisy (real or imagined) in others, make other creatures miserable, demand bribes to spare creatures from your torments

**Anathema** Allow others to slight you without retaliation, seek the approval of society, forgive those who have wronged you

**Religious Symbol** bloodshot eye

**Sacred Animal** black cat

**Sacred Colors** pink, white

**Source:** `= this.source` (`= this.source-type`)

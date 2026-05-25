---
type: deity
source-type: "Remaster"
domains: "Darkness, Dreams, Nightmares, Travel"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Tailwind]], Rank 4: [[Nightmare]], Rank 8: [[Dream Council]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Dream Eater

**Areas of Concern** Dream, hags, planar travel

**Edicts** Break down barriers between planes, instill nightmares in others, work with hags and their covens

**Anathema** Betray a hag without good cause, draw the ire of an Apocalypse Rider, relieve the nightmares of others

**Religious Symbol** jar containing a ghost

**Sacred Animal** black horse

**Sacred Colors** black, blue

**Source:** `= this.source` (`= this.source-type`)

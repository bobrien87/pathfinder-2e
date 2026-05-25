---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Trickery, Wealth"
favored-weapon: "Dagger"
divine-font: "Harm, Heal"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 3: [[Shared Invisibility]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Silent Blade

**Areas of Concern** Greed, opportunity, thievery

**Edicts** Seize any opportunity that would benefit you, solve your problems with violence, hide your true intentions

**Anathema** Steal from the poor, beg for help or mercy from a fellow worshipper of Thamir

**Religious Symbol** black dagger and circle

**Sacred Animal** raccoon

**Sacred Colors** black, brown

**Source:** `= this.source` (`= this.source-type`)

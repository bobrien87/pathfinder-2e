---
type: deity
source-type: "Remaster"
domains: "Magic, Nightmares, Pain, Trickery"
favored-weapon: "Katar"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Ill Omen]], Rank 3: [[Threefold Aspect]], Rank 6: [[Cursed Metamorphosis]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Mother of Witches

**Areas of Concern** Cruelty, deception, hags

**Edicts** Enact disproportionate vengeance, manipulate others to enact your plans, tear down your rivals through both subtlety and violence

**Anathema** Declare your schemes openly, harm an allied witch or hag

**Religious Symbol** eye on three sharp stones

**Sacred Animal** black widow spider

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
